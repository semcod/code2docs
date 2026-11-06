"""Export filtering retains hidden/glob patterns and entries beyond the tenth."""

from types import SimpleNamespace

from code2llm.cli_analysis import _build_filter_config
from code2llm.cli_parser import create_parser
from code2llm.core.file_filter import FastFileFilter

from code2docs.config import Code2DocsConfig
from code2docs.generators.code2llm_gen import Code2LlmGenerator


def test_export_passes_complete_patterns_through_actual_cli_filter(tmp_path):
    config = Code2DocsConfig()
    patterns = [f"copy{n}" for n in range(12)] + [
        ".subactor",
        "**/generated/**",
        "*scratch*",
        "copy0",
    ]
    config.code2llm.exclude_patterns = list(patterns)
    generator = Code2LlmGenerator(config, SimpleNamespace(project_path=str(tmp_path)))
    command = generator._build_base_cmd(tmp_path, tmp_path / "project", config.code2llm)
    generator._add_exclude_patterns(command, config.code2llm, tmp_path)
    args = create_parser().parse_args(command[3:])
    assert args.exclude == list(dict.fromkeys(patterns))
    assert config.code2llm.exclude_patterns == patterns
    filters = _build_filter_config(args)
    file_filter = FastFileFilter(filters, tmp_path)
    assert file_filter.should_process(str(tmp_path / "canonical.py"))
    for relative in [
        "copy11/mirror.py",
        ".subactor/cache/mirror.py",
        "pkg/generated/mirror.py",
        "scratch_copy.py",
    ]:
        assert not file_filter.should_process(str(tmp_path / relative)), relative


def test_export_preserves_existing_simple_gitignore_subproject_skips(tmp_path):
    (tmp_path / ".gitignore").write_text("legacy-cache/\n!keep.py\n")
    config = Code2DocsConfig()
    config.code2llm.exclude_patterns = ["**/generated/**"]
    command = []
    generator = Code2LlmGenerator(config, SimpleNamespace(project_path=str(tmp_path)))
    generator._add_exclude_patterns(command, config.code2llm, tmp_path)
    assert command[:2] == ["--exclude", "**/generated/**"]
    assert command[command.index("--skip-subprojects") + 1 :] == ["legacy-cache"]
