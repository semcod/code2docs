# code2docs.generators.examples_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/examples_gen.py` | 198 lines

## Overview

Auto-generate usage examples from public signatures and entry points.

## Classes

### ExamplesGenerator

Generate examples/ — usage examples from public API signatures.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate_all` | `self` | `—` | — |
| `_generate_basic_usage` | `self` | `—` | — |
| `_generate_import_section` | `self, project_name, public_classes, public_functions` | `—` | — |
| `_generate_class_usage_section` | `self, public_classes` | `—` | — |
| `_generate_function_usage_section` | `self, public_functions` | `—` | — |
| `_generate_entry_point_examples` | `self` | `—` | — |
| `_generate_class_examples` | `self, classes` | `—` | — |
| `_get_major_classes` | `self` | `—` | — |
| `_get_init_args` | `self, cls` | `—` | — |
| `_get_public_methods` | `self, cls` | `—` | — |
| `write_all` | `self, output_dir, files` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 198 |
| Functions | 12 |
| Classes | 1 |
| Fan-out | 71 |
