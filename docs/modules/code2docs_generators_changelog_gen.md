# code2docs.generators.changelog_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/changelog_gen.py` | 121 lines

## Overview

Changelog generator from git log and API diff.

## Classes

### ChangelogEntry

A single changelog entry.

### ChangelogGenerator

Generate CHANGELOG.md from git log and analysis diff.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self, project_path, max_entries` | `—` | — |
| `_get_git_log` | `self, project_path, max_entries` | `—` | — |
| `_classify_message` | `self, message` | `—` | — |
| `_group_by_type` | `self, entries` | `—` | — |
| `_render` | `self, grouped` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 121 |
| Functions | 6 |
| Classes | 2 |
| Fan-out | 28 |
