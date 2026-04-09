"""Tests for BaseGenerator, GeneratorRegistry, and adapter integration."""

from pathlib import Path


from code2llm.core.models import (
    AnalysisResult, FunctionInfo, ClassInfo, ModuleInfo,
)
from code2docs.config import Code2DocsConfig
from code2docs.base import BaseGenerator, GenerateContext
from code2docs.registry import GeneratorRegistry


def _make_config() -> Code2DocsConfig:
    return Code2DocsConfig(project_name="testproject")


def _make_result() -> AnalysisResult:
    result = AnalysisResult(project_path="/tmp/mockproject")
    result.modules = {
        "mylib.core": ModuleInfo(
            name="mylib.core", file="/tmp/mockproject/mylib/core.py",
            imports=["os", "mylib.utils"],
            functions=["mylib.core.process"], classes=["mylib.core.Engine"],
        ),
    }
    result.functions = {
        "mylib.core.process": FunctionInfo(
            name="process", qualified_name="mylib.core.process",
            file="/tmp/mockproject/mylib/core.py", line=10,
            module="mylib.core", args=["data", "config"],
            returns="Dict", docstring="Process data.",
        ),
    }
    result.classes = {
        "mylib.core.Engine": ClassInfo(
            name="Engine", qualified_name="mylib.core.Engine",
            file="/tmp/mockproject/mylib/core.py", line=30,
            module="mylib.core", docstring="Main engine.",
            bases=["BaseEngine"], methods=["run", "stop"],
        ),
    }
    return result


class _DummyGenerator(BaseGenerator):
    """Concrete test generator."""
    name = "dummy"

    def __init__(self, config, result, *, run_flag=True, output="dummy ok"):
        super().__init__(config, result)
        self._run_flag = run_flag
        self._output = output
        self.ran = False

    def should_run(self, *, readme_only=False):
        return self._run_flag and not readme_only

    def run(self, ctx):
        self.ran = True
        return self._output


class _AlwaysGenerator(BaseGenerator):
    name = "always"

    def should_run(self, *, readme_only=False):
        return True

    def run(self, ctx):
        return "✅ always"


# --------------- BaseGenerator ---------------

class TestBaseGenerator:
    def test_subclass_instantiation(self):
        gen = _DummyGenerator(_make_config(), _make_result())
        assert gen.name == "dummy"
        assert gen.config.project_name == "testproject"

    def test_should_run_respects_flag(self):
        gen = _DummyGenerator(_make_config(), _make_result(), run_flag=False)
        assert not gen.should_run()

    def test_should_run_readme_only(self):
        gen = _DummyGenerator(_make_config(), _make_result())
        assert gen.should_run(readme_only=False)
        assert not gen.should_run(readme_only=True)


# --------------- GenerateContext ---------------

class TestGenerateContext:
    def test_defaults(self):
        ctx = GenerateContext(project=Path("/tmp"), docs_dir=Path("/tmp/docs"))
        assert ctx.dry_run is False
        assert ctx.verbose is False

    def test_custom(self):
        ctx = GenerateContext(
            project=Path("/tmp"), docs_dir=Path("/tmp/docs"),
            dry_run=True, verbose=True,
        )
        assert ctx.dry_run is True
        assert ctx.verbose is True


# --------------- GeneratorRegistry ---------------

class TestGeneratorRegistry:
    def test_add_and_run_all(self):
        config, result = _make_config(), _make_result()
        reg = GeneratorRegistry()
        gen = _DummyGenerator(config, result)
        reg.add(gen)
        ctx = GenerateContext(project=Path("/tmp"), docs_dir=Path("/tmp/docs"))
        reg.run_all(ctx)
        assert gen.ran

    def test_skips_disabled_generator(self):
        config, result = _make_config(), _make_result()
        reg = GeneratorRegistry()
        gen = _DummyGenerator(config, result, run_flag=False)
        reg.add(gen)
        ctx = GenerateContext(project=Path("/tmp"), docs_dir=Path("/tmp/docs"))
        reg.run_all(ctx)
        assert not gen.ran

    def test_readme_only_filters(self):
        config, result = _make_config(), _make_result()
        reg = GeneratorRegistry()
        dummy = _DummyGenerator(config, result)
        always = _AlwaysGenerator(config, result)
        reg.add(always)
        reg.add(dummy)
        ctx = GenerateContext(project=Path("/tmp"), docs_dir=Path("/tmp/docs"))
        reg.run_all(ctx, readme_only=True)
        assert not dummy.ran  # skipped because readme_only
        # always should have run (it ignores readme_only)

    def test_run_only(self):
        config, result = _make_config(), _make_result()
        reg = GeneratorRegistry()
        d1 = _DummyGenerator(config, result, output="d1")
        d1.name = "first"
        d2 = _DummyGenerator(config, result, output="d2")
        d2.name = "second"
        reg.add(d1)
        reg.add(d2)
        ctx = GenerateContext(project=Path("/tmp"), docs_dir=Path("/tmp/docs"))
        reg.run_only("second", ctx)
        assert not d1.ran
        assert d2.ran

    def test_run_preserves_order(self):
        config, result = _make_config(), _make_result()
        order = []

        class _OrderGen(BaseGenerator):
            def should_run(self, *, readme_only=False):
                return True
            def run(self, ctx):
                order.append(self.name)
                return self.name

        g1 = _OrderGen(config, result)
        g1.name = "first"
        g2 = _OrderGen(config, result)
        g2.name = "second"
        g3 = _OrderGen(config, result)
        g3.name = "third"

        reg = GeneratorRegistry()
        reg.add(g1)
        reg.add(g2)
        reg.add(g3)
        ctx = GenerateContext(project=Path("/tmp"), docs_dir=Path("/tmp/docs"))
        reg.run_all(ctx)
        assert order == ["first", "second", "third"]


# --------------- Adapter Integration ---------------

class TestAdapters:
    def test_all_adapters_importable(self):
        from code2docs.generators._registry_adapters import ALL_ADAPTERS
        assert len(ALL_ADAPTERS) >= 9

    def test_all_adapters_have_names(self):
        from code2docs.generators._registry_adapters import ALL_ADAPTERS
        config, result = _make_config(), _make_result()
        names = set()
        for cls in ALL_ADAPTERS:
            inst = cls(config, result)
            assert inst.name, f"{cls.__name__} has no name"
            names.add(inst.name)
        assert len(names) == len(ALL_ADAPTERS), "Duplicate adapter names"

    def test_readme_adapter_always_runs(self):
        from code2docs.generators._registry_adapters import ReadmeGeneratorAdapter
        config, result = _make_config(), _make_result()
        adapter = ReadmeGeneratorAdapter(config, result)
        assert adapter.should_run(readme_only=True)
        assert adapter.should_run(readme_only=False)

    def test_non_readme_adapters_skip_readme_only(self):
        from code2docs.generators._registry_adapters import ALL_ADAPTERS, ReadmeGeneratorAdapter
        config, result = _make_config(), _make_result()
        for cls in ALL_ADAPTERS:
            if cls is ReadmeGeneratorAdapter:
                continue
            inst = cls(config, result)
            assert not inst.should_run(readme_only=True), \
                f"{cls.__name__} should not run in readme_only mode"
