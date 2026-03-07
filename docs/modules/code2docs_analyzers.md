# code2docs.analyzers

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/__init__.py` | 13 lines

## Overview

Analyzers — adapters to code2llm and custom detectors.

## Classes

### ProjectScanner

Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | — |
| `_build_llm_config` | `self` | `—` | — |
| `analyze` | `self, project_path` | `—` | — |

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

### DocstringInfo

Parsed docstring with sections.

### DocstringExtractor

Extract and parse docstrings from AnalysisResult.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `extract_all` | `self, result` | `—` | — |
| `parse` | `self, docstring` | `—` | — |
| `_extract_summary` | `lines` | `—` | — |
| `_classify_section` | `line` | `—` | — |
| `_parse_sections` | `self, lines, info` | `—` | — |
| `coverage_report` | `self, result` | `—` | — |

### Endpoint

Represents a detected web endpoint.

### EndpointDetector

Detects web endpoints from decorator patterns in source code.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `detect` | `self, result, project_path` | `—` | — |
| `_parse_decorator` | `self, decorator, func` | `—` | — |
| `_scan_django_urls` | `self, project_path` | `—` | — |

## Functions

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

**Calls:** `ProjectScanner`, `scanner.analyze`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 13 |
| Functions | 0 |
| Classes | 0 |
