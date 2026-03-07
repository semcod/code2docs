# code2docs.generators.module_docs_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/module_docs_gen.py` | 220 lines

## Overview

Per-module detailed documentation generator.

## Classes

### ModuleDocsGenerator

Generate docs/modules/ — detailed per-module documentation.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate_all` | `self` | `—` | — |
| `_generate_module` | `self, mod_name, mod_info` | `—` | — |
| `_render_header` | `self, mod_name, mod_info` | `—` | — |
| `_render_overview` | `self, mod_info` | `—` | — |
| `_render_classes_section` | `self, mod_name` | `—` | — |
| `_render_functions_section` | `self, mod_name` | `—` | — |
| `_render_dependencies_section` | `self, mod_info` | `—` | — |
| `_render_metrics_section` | `self, mod_name, mod_info` | `—` | — |
| `_count_file_lines` | `self, file_path` | `—` | — |
| `_calc_module_avg_cc` | `self, mod_name` | `—` | — |
| `_get_module_docstring` | `self, mod_info` | `—` | — |
| `_get_module_classes` | `self, mod_name` | `—` | — |
| `_get_module_functions` | `self, mod_name` | `—` | — |
| `_get_class_methods` | `self, cls_info` | `—` | — |
| `_get_module_metrics` | `self, mod_name, mod_info` | `—` | — |
| `write_all` | `self, output_dir, files` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 220 |
| Functions | 17 |
| Classes | 1 |
| Fan-out | 103 |
