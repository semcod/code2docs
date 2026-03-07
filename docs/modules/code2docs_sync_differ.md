# code2docs.sync.differ

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/differ.py` | 125 lines

## Overview

Detect changes in source code for selective documentation regeneration.

## Classes

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

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 125 |
| Functions | 7 |
| Classes | 2 |
| Fan-out | 39 |
