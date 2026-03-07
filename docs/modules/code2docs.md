# code2docs

> Source: `/home/tom/github/wronai/code2docs/code2docs/__init__.py` | 32 lines

## Overview

code2docs - Auto-generate and sync project documentation from source code.

Uses code2llm's AnalysisResult to produce human-readable documentation:
README.md, API references, module docs, examples, and architecture diagrams.

## Classes

### Updater

Apply selective documentation updates based on detected changes.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | — |
| `apply` | `self, project_path, changes` | `—` | — |

### MarkdownFormatter

Helper for constructing Markdown documents.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self` | `—` | — |
| `heading` | `self, text, level` | `—` | — |
| `paragraph` | `self, text` | `—` | — |
| `blockquote` | `self, text` | `—` | — |
| `code_block` | `self, code, language` | `—` | — |
| `inline_code` | `self, text` | `—` | — |
| `bold` | `self, text` | `—` | — |
| `link` | `self, text, url` | `—` | — |
| `list_item` | `self, text, indent` | `—` | — |
| `table` | `self, headers, rows` | `—` | — |
| `separator` | `self` | `—` | — |
| `blank` | `self` | `—` | — |
| `render` | `self` | `—` | — |

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

### ChangeInfo

Describes a detected change.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__str__` | `self` | `—` | — |

### Differ

Detect changes between current source and previous state.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | — |
| `detect_changes` | `self, project_path` | `—` | — |
| `save_state` | `self, project_path` | `—` | — |
| `_load_state` | `self, state_path` | `—` | — |
| `_compute_state` | `self, project` | `—` | — |
| `_file_to_module` | `filepath, project` | `—` | — |

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

### DefaultGroup

*Bases:* `click.Group`

Click Group that routes unknown subcommands to 'generate'.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `parse_args` | `self, ctx, args` | `—` | — |

### ReadmeConfig

Configuration for README generation.

### DocsConfig

Configuration for docs/ generation.

### ExamplesConfig

Configuration for examples/ generation.

### SyncConfig

Configuration for synchronization.

### Code2DocsConfig

Main configuration for code2docs.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `from_yaml` | `cls, path` | `—` | — |
| `to_yaml` | `self, path` | `—` | — |

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

### `__getattr__(name)`

Lazy import heavy modules on first access.

**Calls:** `AttributeError`

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

**Calls:** `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`

**Called by:** `code2docs.cli._run_watch`, `code2docs.cli._run_watch`

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

**Calls:** `None.join`, `code2docs.formatters.badges._make_badge`, `badges.append`

**Called by:** `code2docs.generators.readme_gen.ReadmeGenerator._build_context`, `code2docs.generators.readme_gen.ReadmeGenerator._build_context`

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

**Calls:** `quote`, `quote`, `hasattr`, `stats.get`

**Called by:** `code2docs.formatters.badges.generate_badges`, `code2docs.formatters.badges.generate_badges`

### `generate_toc(markdown_content, max_depth)`

Generate a table of contents from Markdown headings.

Args:
    markdown_content: Full Markdown document.
    max_depth: Maximum heading level to include (1-6).

Returns:
    TOC as Markdown string.

**Calls:** `code2docs.formatters.toc.extract_headings`, `lines.append`, `None.join`, `lines.append`

### `extract_headings(content, max_depth)`

Extract headings from Markdown content.

Returns list of (level, text, anchor) tuples.

**Calls:** `content.splitlines`, `None.startswith`, `re.match`, `len`, `line.strip`, `match.group`, `None.strip`, `code2docs.formatters.toc._slugify`, `headings.append`, `match.group`

**Called by:** `code2docs.formatters.toc.generate_toc`, `code2docs.formatters.toc.generate_toc`

### `_slugify(text)`

Convert heading text to GitHub-compatible anchor slug.

**Calls:** `text.lower`, `re.sub`, `re.sub`, `slug.strip`

**Called by:** `code2docs.formatters.toc.extract_headings`, `code2docs.formatters.toc.extract_headings`

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

**Calls:** `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`

### `generate_docs(project_path, config)`

High-level function to generate all documentation.

**Calls:** `ProjectScanner`, `scanner.analyze`, `None.generate`, `None.generate`, `None.generate`, `Code2DocsConfig`, `None.generate_all`, `None.generate_all`, `None.generate`, `ReadmeGenerator`

### `main()`

code2docs — Auto-generate project documentation from source code.

**Calls:** `click.group`

### `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run)`

Generate documentation (default command).

**Calls:** `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_generate`

### `sync(project_path, config_path, verbose, dry_run)`

Synchronize documentation with source code changes.

**Calls:** `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_sync`, `click.Path`

### `watch(project_path, config_path, verbose)`

Watch for file changes and auto-regenerate docs.

**Calls:** `main.command`, `click.argument`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_watch`, `click.Path`

### `init(project_path, output)`

Initialize code2docs.yaml configuration file.

**Calls:** `main.command`, `click.argument`, `click.option`, `None.resolve`, `Code2DocsConfig`, `config.to_yaml`, `click.echo`, `str`, `click.Path`, `Path`

### `_load_config(project_path, config_path)`

Load configuration, auto-detecting code2docs.yaml if present.

**Calls:** `None.resolve`, `Code2DocsConfig`, `Code2DocsConfig.from_yaml`, `candidate.exists`, `Path`, `Code2DocsConfig.from_yaml`, `str`

**Called by:** `code2docs.cli.generate`, `code2docs.cli.sync`, `code2docs.cli.watch`, `code2docs.cli.generate`, `code2docs.cli.sync`, `code2docs.cli.watch`

### `_run_generate(project_path, config, readme_only, dry_run)`

Run full documentation generation.

**Calls:** `None.resolve`, `click.echo`, `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `readme_gen.generate`, `docs_dir.mkdir`, `DepGraphGenerator`, `depgraph_gen.generate`, `CoverageGenerator`

**Called by:** `code2docs.cli.generate`, `code2docs.cli.generate`

### `_run_sync(project_path, config, dry_run)`

Run sync — regenerate only changed documentation.

**Calls:** `None.resolve`, `click.echo`, `Differ`, `differ.detect_changes`, `click.echo`, `Updater`, `updater.apply`, `click.echo`, `str`, `click.echo`

**Called by:** `code2docs.cli.sync`, `code2docs.cli.sync`

### `_run_watch(project_path, config)`

Run file watcher for auto-resync.

**Calls:** `None.resolve`, `click.echo`, `code2docs.sync.watcher.start_watcher`, `str`, `click.echo`, `sys.exit`, `Path`

**Called by:** `code2docs.cli.watch`, `code2docs.cli.watch`

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

**Calls:** `ProjectScanner`, `scanner.analyze`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 32 |
| Functions | 1 |
| Classes | 0 |
| Fan-out | 1 |
