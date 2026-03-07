# `code2docs.generators.api_changelog_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/api_changelog_gen.py`

## Classes

### `ApiChange`

A single API change between two analysis snapshots.

### `ApiChangelogGenerator`

Generate API changelog by diffing current analysis with a saved snapshot.

#### Methods

- `__init__(self, config, result)`
- `generate(self, project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(self, project_path)` — Save current API state as snapshot for future diffs.
- `_build_snapshot(self)` — Build a JSON-serializable snapshot of current API.
- `_load_snapshot(path)` — Load previous snapshot, or None if not found.
- `_diff(self, old, new)` — Compute list of API changes between old and new snapshots.
- `_diff_functions(old, new, changes)` — Diff function signatures.
- `_diff_classes(old, new, changes)` — Diff class definitions.
- `_render(project_name, changes, has_baseline)` — Render changelog as Markdown.
