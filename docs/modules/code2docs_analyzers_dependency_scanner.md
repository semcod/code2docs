# code2docs.analyzers.dependency_scanner

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/dependency_scanner.py` | 159 lines

## Overview

Scan project dependencies from requirements.txt, pyproject.toml, setup.py.

## Classes

### DependencyInfo

Information about a project dependency.

### ProjectDependencies

All detected project dependencies.

### DependencyScanner

Scan and parse project dependency files.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `scan` | `self, project_path` | `—` | — |
| `_parse_pyproject` | `self, path` | `—` | — |
| `_parse_pyproject_regex` | `self, path` | `—` | — |
| `_parse_setup_py` | `self, path` | `—` | — |
| `_parse_requirements_txt` | `self, path` | `—` | — |
| `_parse_dep_string` | `dep_str` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 159 |
| Functions | 6 |
| Classes | 3 |
| Fan-out | 55 |
