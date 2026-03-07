# code2docs.sync

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/__init__.py` | 6 lines

## Overview

Sync — detect changes and selectively regenerate documentation.

## Classes

### Updater

Apply selective documentation updates based on detected changes.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | — |
| `apply` | `self, project_path, changes` | `—` | — |

### ChangeInfo

Describes a detected change.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__str__` | `self` | `—` | — |

### Differ

Detect changes between current source and previous state.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | — |
| `detect_changes` | `self, project_path` | `—` | — |
| `save_state` | `self, project_path` | `—` | — |
| `_load_state` | `self, state_path` | `—` | — |
| `_compute_state` | `self, project` | `—` | — |
| `_file_to_module` | `filepath, project` | `—` | — |

## Functions

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

**Calls:** `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`

**Called by:** `code2docs.cli._run_watch`, `code2docs.cli._run_watch`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 6 |
| Functions | 0 |
| Classes | 0 |
