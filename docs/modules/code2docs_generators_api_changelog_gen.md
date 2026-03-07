# code2docs.generators.api_changelog_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/api_changelog_gen.py` | 196 lines

## Overview

API changelog generator — diff function/class signatures between versions.

## Classes

### ApiChange

A single API change between two analysis snapshots.

### ApiChangelogGenerator

Generate API changelog by diffing current analysis with a saved snapshot.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self, project_path` | `—` | — |
| `save_snapshot` | `self, project_path` | `—` | — |
| `_build_snapshot` | `self` | `—` | — |
| `_load_snapshot` | `path` | `—` | — |
| `_diff` | `self, old, new` | `—` | — |
| `_diff_functions` | `old, new, changes` | `—` | — |
| `_diff_classes` | `old, new, changes` | `—` | — |
| `_render` | `project_name, changes, has_baseline` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 196 |
| Functions | 9 |
| Classes | 2 |
| Fan-out | 80 |
