"""Tests for code2docs configuration."""

import tempfile
from pathlib import Path


from code2docs.config import Code2DocsConfig


class TestCode2DocsConfig:
    def test_defaults(self):
        config = Code2DocsConfig()
        assert config.source == "./"
        assert config.output == "./docs/"
        assert config.readme_output == "./README.md"
        assert config.verbose is False
        assert config.exclude_tests is True

    def test_readme_defaults(self):
        config = Code2DocsConfig()
        assert "overview" in config.readme.sections
        assert "api" in config.readme.sections
        assert config.readme.sync_markers is True

    def test_yaml_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config = Code2DocsConfig(
                project_name="test-project",
                source="./src",
                verbose=True,
            )
            yaml_path = str(Path(tmpdir) / "code2docs.yaml")
            config.to_yaml(yaml_path)

            loaded = Code2DocsConfig.from_yaml(yaml_path)
            assert loaded.project_name == "test-project"
            assert loaded.source == "./src"
            assert loaded.verbose is True

    def test_from_yaml_missing_file(self):
        config = Code2DocsConfig.from_yaml("/nonexistent/path.yaml")
        assert config.project_name == ""

    def test_sync_config_defaults(self):
        config = Code2DocsConfig()
        assert config.sync.strategy == "markers"
        assert config.sync.watch is False
        assert "tests/" in config.sync.ignore
