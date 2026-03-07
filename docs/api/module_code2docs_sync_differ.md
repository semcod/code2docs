# `code2docs.sync.differ`

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/differ.py`

## Classes

### `ChangeInfo`

Describes a detected change.

#### Methods

- `__str__(self)`

### `Differ`

Detect changes between current source and previous state.

#### Methods

- `__init__(self, config)`
- `detect_changes(self, project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(self, project_path)` — Save current file hashes as state.
- `_load_state(self, state_path)` — Load previous state from file.
- `_compute_state(self, project)` — Compute file hashes for all Python files in the project.
- `_file_to_module(filepath, project)` — Convert file path to module name.
