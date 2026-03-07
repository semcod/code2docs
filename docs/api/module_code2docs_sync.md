# `code2docs.sync`

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/__init__.py`

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

### `Updater`

Apply selective documentation updates based on detected changes.

#### Methods

- `__init__(self, config)`
- `apply(self, project_path, changes)` — Regenerate documentation for changed modules.

## Functions

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

- Calls: `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`
