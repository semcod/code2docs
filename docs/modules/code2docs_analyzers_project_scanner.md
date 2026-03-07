# code2docs.analyzers.project_scanner

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/project_scanner.py` | 42 lines

## Overview

Wrapper around code2llm's ProjectAnalyzer for documentation purposes.

## Classes

### ProjectScanner

Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | — |
| `_build_llm_config` | `self` | `—` | — |
| `analyze` | `self, project_path` | `—` | — |

## Functions

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

**Calls:** `ProjectScanner`, `scanner.analyze`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 42 |
| Functions | 4 |
| Classes | 1 |
| Fan-in | 2 |
| Fan-out | 6 |
