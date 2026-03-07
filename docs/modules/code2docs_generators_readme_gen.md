# code2docs.generators.readme_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/readme_gen.py` | 260 lines

## Overview

README.md generator from AnalysisResult.

## Classes

### ReadmeGenerator

Generate README.md from AnalysisResult.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self` | `—` | — |
| `_build_context` | `self, project_name` | `—` | — |
| `_calc_avg_complexity` | `self` | `—` | — |
| `_build_module_tree` | `self` | `—` | — |
| `_build_manual` | `self, project_name, sections, context` | `—` | — |
| `_build_overview_section` | `project_name, context` | `—` | — |
| `_build_install_section` | `_project_name, context` | `—` | — |
| `_build_quickstart_section` | `_project_name, context` | `—` | — |
| `_build_api_section` | `_project_name, context` | `—` | — |
| `_build_structure_section` | `_project_name, context` | `—` | — |
| `_build_endpoints_section` | `_project_name, context` | `—` | — |
| `write` | `self, path, content` | `—` | — |

## Functions

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

**Calls:** `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 260 |
| Functions | 14 |
| Classes | 1 |
| Fan-out | 91 |
