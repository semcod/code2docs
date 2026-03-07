# code2docs.generators

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/__init__.py` | 53 lines

## Overview

Documentation generators — produce Markdown, examples, and diagrams.

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

### CoverageGenerator

Generate docs/coverage.md — docstring coverage report.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self` | `—` | — |
| `_render_summary` | `report` | `—` | — |
| `_render_per_module` | `self` | `—` | — |
| `_render_undocumented` | `self` | `—` | — |

### DepGraphGenerator

Generate docs/dependency-graph.md with Mermaid diagrams.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self` | `—` | — |
| `_collect_edges` | `self` | `—` | — |
| `_import_matches` | `imp, module` | `—` | — |
| `_render_mermaid` | `self, edges` | `—` | — |
| `_render_matrix` | `self, edges` | `—` | — |
| `_calc_degrees` | `edges` | `—` | — |
| `_render_degree_table` | `self, in_deg, out_deg` | `—` | — |

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

### MkDocsGenerator

Generate mkdocs.yml from the docs/ directory structure.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self, docs_dir` | `—` | — |
| `_build_nav` | `self, docs_dir` | `—` | — |
| `write` | `self, output_path, content` | `—` | — |

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

### ArchitectureGenerator

Generate docs/architecture.md — architecture overview with diagrams.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self` | `—` | — |
| `_generate_module_graph` | `self` | `—` | — |
| `_generate_class_diagram` | `self` | `—` | — |
| `_detect_layers` | `self` | `—` | — |
| `_generate_metrics_table` | `self` | `—` | — |

## Functions

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

**Calls:** `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`

### `generate_docs(project_path, config)`

High-level function to generate all documentation.

**Calls:** `ProjectScanner`, `scanner.analyze`, `None.generate`, `None.generate`, `None.generate`, `Code2DocsConfig`, `None.generate_all`, `None.generate_all`, `None.generate`, `ReadmeGenerator`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 53 |
| Functions | 1 |
| Classes | 0 |
| Fan-out | 15 |
