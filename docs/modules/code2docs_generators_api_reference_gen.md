# code2docs.generators.api_reference_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/api_reference_gen.py` | 162 lines

## Overview

API reference documentation generator — per-module API docs.

## Classes

### ApiReferenceGenerator

Generate docs/api/ — per-module API reference from signatures.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate_all` | `self` | `—` | — |
| `_generate_index` | `self` | `—` | — |
| `_generate_module_api` | `self, mod_name, mod_info` | `—` | — |
| `_render_api_header` | `self, mod_name, mod_info` | `—` | — |
| `_render_api_classes` | `self, mod_name` | `—` | — |
| `_render_api_functions` | `self, mod_name` | `—` | — |
| `_render_api_imports` | `self, mod_info` | `—` | — |
| `_get_class_methods` | `self, cls_info` | `—` | — |
| `_format_signature` | `func` | `—` | — |
| `write_all` | `self, output_dir, files` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 162 |
| Functions | 11 |
| Classes | 1 |
| Fan-out | 66 |
