"""Real collection and README generation respect configured source boundaries."""

from copy import deepcopy

import pytest
import yaml
from click.testing import CliRunner
from code2llm.api import Config

from code2docs.analyzers.project_scanner import ProjectScanner
from code2docs.cli import main
from code2docs.config import Code2DocsConfig


def sample(root):
    for relative, name in [
        ("canonical.py", "CanonicalEngine"),
        ("artifacts/copy.py", "ArtifactCopy"),
        ("scratch_copy.py", "ScratchCopy"),
        ("generated/copy.py", "GeneratedCopy"),
        (".subactor/cache/copy.py", "CacheCopy"),
        (".worktrees/ticket-999/copy.py", "WorktreeCopy"),
        ("venv/copy.py", "EnvironmentCopy"),
    ]:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f'class {name}:\n    """{name} API."""\n    def run(self):\n        return 1\n'
        )


@pytest.mark.parametrize("export_enabled", [False, True])
def test_actual_collection_applies_custom_exclusions_with_or_without_export(
    tmp_path, export_enabled
):
    sample(tmp_path)
    config = Code2DocsConfig()
    config.code2llm.enabled = export_enabled
    config.code2llm.exclude_patterns = ["artifacts", "*scratch*", "generated"]
    scanner = ProjectScanner(config)
    result = scanner.analyze(str(tmp_path))
    names = {item.name for item in result.classes.values()}
    assert names == {"CanonicalEngine"}


def test_scanner_preserves_native_defaults_and_does_not_mutate_configuration():
    defaults = deepcopy(Config().filters.exclude_patterns)
    config = Code2DocsConfig()
    configured = ["artifacts", "**/generated/**", "artifacts"]
    config.code2llm.exclude_patterns = configured
    scanner = ProjectScanner(config)
    assert config.code2llm.exclude_patterns == configured
    assert Config().filters.exclude_patterns == defaults
    assert set(defaults) <= set(scanner._llm_config.filters.exclude_patterns)
    assert scanner._llm_config.filters.exclude_patterns.count("artifacts") == 1
    scanner._llm_config.filters.exclude_patterns.append("scanner-only")
    assert "scanner-only" not in config.code2llm.exclude_patterns
    assert "scanner-only" not in Config().filters.exclude_patterns


def test_empty_configured_exclusions_keep_native_filter_defaults():
    config = Code2DocsConfig()
    config.code2llm.exclude_patterns = []
    assert (
        ProjectScanner(config)._llm_config.filters.exclude_patterns
        == Config().filters.exclude_patterns
    )


def test_readme_only_cli_uses_yaml_exclusions_and_keeps_sync_markers(tmp_path, monkeypatch):
    sample(tmp_path)
    path = tmp_path / "code2docs.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "project": {"name": "fixture", "readme_output": "manual/README.md"},
                "llm": {"enabled": False},
                "code2llm": {
                    "enabled": False,
                    "exclude_patterns": ["artifacts", "*scratch*", "generated"],
                },
                "readme": {"sections": ["api", "structure"], "sync_markers": True},
            }
        )
    )
    monkeypatch.setattr("code2docs.autoupdate.check_for_updates", lambda *args: None)
    result = CliRunner().invoke(
        main, ["generate", str(tmp_path), "--config", str(path), "--readme-only"]
    )
    assert result.exit_code == 0, result.output
    content = (tmp_path / "manual/README.md").read_text()
    assert "CanonicalEngine" in content
    for excluded in [
        "ArtifactCopy",
        "ScratchCopy",
        "GeneratedCopy",
        "CacheCopy",
        "WorktreeCopy",
        "EnvironmentCopy",
    ]:
        assert excluded not in content
    from code2docs.generators.readme_gen import MARKER_START, MARKER_END

    assert MARKER_START in content and MARKER_END in content
    assert not (tmp_path / "project").exists()
