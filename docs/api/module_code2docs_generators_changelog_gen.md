# `code2docs.generators.changelog_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/changelog_gen.py`

## Classes

### `ChangelogEntry`

A single changelog entry.

### `ChangelogGenerator`

Generate CHANGELOG.md from git log and analysis diff.

#### Methods

- `__init__(self, config, result)`
- `generate(self, project_path, max_entries)` — Generate changelog content from git log.
- `_get_git_log(self, project_path, max_entries)` — Extract git log entries.
- `_classify_message(self, message)` — Classify commit message by conventional commit type.
- `_group_by_type(self, entries)` — Group entries by type.
- `_render(self, grouped)` — Render grouped changelog to Markdown.
