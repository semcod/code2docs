"""Tests for analyzers (docstring_extractor, dependency_scanner, endpoint_detector)."""

import tempfile
from pathlib import Path

import pytest

from code2docs.analyzers.docstring_extractor import DocstringExtractor
from code2docs.analyzers.dependency_scanner import DependencyScanner
from code2docs.analyzers.endpoint_detector import EndpointDetector


class TestDocstringExtractor:
    def test_parse_simple(self):
        ext = DocstringExtractor()
        info = ext.parse("Do something useful.")
        assert info.summary == "Do something useful."

    def test_parse_with_params(self):
        ext = DocstringExtractor()
        doc = """Process the data.

        Args:
            x: The input value
            y: The output value

        Returns:
            Processed result
        """
        info = ext.parse(doc)
        assert info.summary == "Process the data."
        assert "x" in info.params
        assert "y" in info.params
        assert info.returns == "Processed result"

    def test_parse_empty(self):
        ext = DocstringExtractor()
        info = ext.parse("")
        assert info.raw == ""
        assert info.summary == ""

    def test_coverage_report(self):
        from code2llm.core.models import AnalysisResult, FunctionInfo, ClassInfo
        result = AnalysisResult()
        result.functions = {
            "a": FunctionInfo(name="a", qualified_name="a", file="f.py", line=1, docstring="Doc"),
            "b": FunctionInfo(name="b", qualified_name="b", file="f.py", line=2, docstring=None),
        }
        result.classes = {
            "C": ClassInfo(name="C", qualified_name="C", file="f.py", line=1, docstring="Doc"),
        }
        ext = DocstringExtractor()
        report = ext.coverage_report(result)
        assert report["functions_total"] == 2
        assert report["functions_documented"] == 1
        assert report["classes_documented"] == 1
        assert report["overall_coverage"] == pytest.approx(66.67, rel=0.1)


class TestDependencyScanner:
    def test_parse_requirements_txt(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            req_path = Path(tmpdir) / "requirements.txt"
            req_path.write_text("click>=8.0\njinja2>=3.1\npyyaml\n")

            scanner = DependencyScanner()
            deps = scanner.scan(tmpdir)
            assert len(deps.dependencies) == 3
            assert deps.dependencies[0].name == "click"
            assert deps.source_file == "requirements.txt"

    def test_parse_pyproject_toml(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            toml_path = Path(tmpdir) / "pyproject.toml"
            toml_path.write_text("""
[project]
name = "test-pkg"
requires-python = ">=3.9"
dependencies = [
    "click>=8.0",
    "jinja2>=3.1",
]
""")
            scanner = DependencyScanner()
            deps = scanner.scan(tmpdir)
            assert len(deps.dependencies) == 2
            assert deps.python_version == ">=3.9"
            assert deps.source_file == "pyproject.toml"

    def test_empty_project(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            scanner = DependencyScanner()
            deps = scanner.scan(tmpdir)
            assert len(deps.dependencies) == 0


class TestEndpointDetector:
    def test_parse_flask_decorator(self):
        from code2llm.core.models import FunctionInfo
        detector = EndpointDetector()
        func = FunctionInfo(
            name="index", qualified_name="app.index",
            file="app.py", line=10,
            decorators=["@app.route('/api/users')"],
            args=["request"],
        )
        ep = detector._parse_decorator(func.decorators[0], func)
        assert ep is not None
        assert ep.path == "/api/users"
        assert ep.framework == "flask"
        assert ep.method == "GET"

    def test_parse_fastapi_decorator(self):
        from code2llm.core.models import FunctionInfo
        detector = EndpointDetector()
        func = FunctionInfo(
            name="create_user", qualified_name="app.create_user",
            file="app.py", line=20,
            decorators=["@app.post('/api/users')"],
            args=["user"],
        )
        ep = detector._parse_decorator(func.decorators[0], func)
        assert ep is not None
        assert ep.path == "/api/users"
        assert ep.framework == "fastapi"
        assert ep.method == "POST"

    def test_no_match(self):
        from code2llm.core.models import FunctionInfo
        detector = EndpointDetector()
        func = FunctionInfo(
            name="helper", qualified_name="mod.helper",
            file="mod.py", line=1,
            decorators=["@staticmethod"],
            args=[],
        )
        ep = detector._parse_decorator(func.decorators[0], func)
        assert ep is None
