# `code2docs.generators`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/__init__.py`

## Classes

### `ApiChange`

A single API change between two analysis snapshots.

### `ApiChangelogGenerator`

Generate API changelog by diffing current analysis with a saved snapshot.

#### Methods

- `__init__(self, config, result)`
- `generate(self, project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(self, project_path)` — Save current API state as snapshot for future diffs.
- `_build_snapshot(self)` — Build a JSON-serializable snapshot of current API.
- `_load_snapshot(path)` — Load previous snapshot, or None if not found.
- `_diff(self, old, new)` — Compute list of API changes between old and new snapshots.
- `_diff_functions(old, new, changes)` — Diff function signatures.
- `_diff_classes(old, new, changes)` — Diff class definitions.
- `_render(project_name, changes, has_baseline)` — Render changelog as Markdown.

### `ApiReferenceGenerator`

Generate docs/api/ — per-module API reference from signatures.

#### Methods

- `__init__(self, config, result)`
- `generate_all(self)` — Generate API reference for all modules. Returns {filename: content}.
- `_generate_index(self)` — Generate API index page.
- `_generate_module_api(self, mod_name, mod_info)` — Generate API reference for a single module (orchestrator).
- `_render_api_header(self, mod_name, mod_info)` — Render module header with source info.
- `_render_api_classes(self, mod_name)` — Render classes with their method signatures.
- `_render_api_functions(self, mod_name)` — Render standalone functions with signatures and complexity.
- `_render_api_imports(self, mod_info)` — Render module imports list.
- `_get_class_methods(self, cls_info)` — Get FunctionInfo objects for class methods.
- `_format_signature(func)` — Format a function signature string.
- `write_all(self, output_dir, files)` — Write all generated API reference files.

### `ArchitectureGenerator`

Generate docs/architecture.md — architecture overview with diagrams.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate architecture documentation.
- `_generate_module_graph(self)` — Generate Mermaid module dependency graph.
- `_generate_class_diagram(self)` — Generate Mermaid class diagram for key classes.
- `_detect_layers(self)` — Detect architectural layers from module names.
- `_generate_metrics_table(self)` — Generate metrics summary table.

### `ChangelogEntry`

A single changelog entry.

### `ChangelogGenerator`

Generate CHANGELOG.md from git log and analysis diff.

#### Methods

- `__init__(self, config, result)`
- `generate(self, project_path, max_entries)` — Generate changelog content from git log.
- `_get_git_log(self, project_path, max_entries)` — Extract git log entries.
- `_classify_message(self, message)` — Classify commit message by conventional commit type.
- `_group_by_type(self, entries)` — Group entries by type.
- `_render(self, grouped)` — Render grouped changelog to Markdown.

### `CoverageGenerator`

Generate docs/coverage.md — docstring coverage report.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate coverage.md content.
- `_render_summary(report)` — Render overall coverage summary.
- `_render_per_module(self)` — Render per-module coverage table.
- `_render_undocumented(self)` — List all undocumented public functions and classes.

### `DepGraphGenerator`

Generate docs/dependency-graph.md with Mermaid diagrams.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate dependency-graph.md content.
- `_collect_edges(self)` — Build directed edges from module imports.
- `_import_matches(imp, module)` — Check if an import string refers to a known module.
- `_render_mermaid(self, edges)` — Render Mermaid graph from edges.
- `_render_matrix(self, edges)` — Render a coupling matrix as a Markdown table.
- `_calc_degrees(edges)` — Calculate in-degree and out-degree per module.
- `_render_degree_table(self, in_deg, out_deg)` — Render fan-in/fan-out table.

### `ExamplesGenerator`

Generate examples/ — usage examples from public API signatures.

#### Methods

- `__init__(self, config, result)`
- `generate_all(self)` — Generate all example files. Returns {filename: content}.
- `_generate_basic_usage(self)` — Generate basic_usage.py example (orchestrator).
- `_generate_import_section(self, project_name, public_classes, public_functions)` — Generate import statements for the example.
- `_generate_class_usage_section(self, public_classes)` — Generate class instantiation and method call examples.
- `_generate_function_usage_section(self, public_functions)` — Generate standalone function call examples.
- `_generate_entry_point_examples(self)` — Generate examples based on entry points.
- `_generate_class_examples(self, classes)` — Generate examples for major classes.
- `_get_major_classes(self)` — Get classes with most methods (likely most important).
- `_get_init_args(self, cls)` — Get __init__ args for a class.
- `_get_public_methods(self, cls)` — Get public methods of a class.
- `write_all(self, output_dir, files)` — Write all generated example files.

### `MkDocsGenerator`

Generate mkdocs.yml from the docs/ directory structure.

#### Methods

- `__init__(self, config, result)`
- `generate(self, docs_dir)` — Generate mkdocs.yml content.
- `_build_nav(self, docs_dir)` — Build navigation structure from docs tree and analysis.
- `write(self, output_path, content)` — Write mkdocs.yml file.

### `ModuleDocsGenerator`

Generate docs/modules/ — detailed per-module documentation.

#### Methods

- `__init__(self, config, result)`
- `generate_all(self)` — Generate documentation for all modules. Returns {filename: content}.
- `_generate_module(self, mod_name, mod_info)` — Generate detailed documentation for a single module (orchestrator).
- `_render_header(self, mod_name, mod_info)` — Render module title and source metadata.
- `_render_overview(self, mod_info)` — Render module overview from docstring.
- `_render_classes_section(self, mod_name)` — Render classes and their method tables.
- `_render_functions_section(self, mod_name)` — Render standalone functions with signatures and call info.
- `_render_dependencies_section(self, mod_info)` — Render imports split into internal and stdlib.
- `_render_metrics_section(self, mod_name, mod_info)` — Render metrics summary table.
- `_count_file_lines(self, file_path)` — Count lines in source file.
- `_calc_module_avg_cc(self, mod_name)` — Calculate average cyclomatic complexity for module functions.
- `_get_module_docstring(self, mod_info)` — Try to extract module-level docstring.
- `_get_module_classes(self, mod_name)`
- `_get_module_functions(self, mod_name)`
- `_get_class_methods(self, cls_info)`
- `_get_module_metrics(self, mod_name, mod_info)`
- `write_all(self, output_dir, files)` — Write all generated module docs.

### `ReadmeGenerator`

Generate README.md from AnalysisResult.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate full README content.
- `_build_context(self, project_name)` — Build template context from analysis result.
- `_calc_avg_complexity(self)` — Calculate average cyclomatic complexity.
- `_build_module_tree(self)` — Build text-based module tree.
- `_build_manual(self, project_name, sections, context)` — Fallback manual README builder (orchestrator).
- `_build_overview_section(project_name, context)` — Build overview section with badges and stats.
- `_build_install_section(_project_name, context)` — Build installation section from dependencies.
- `_build_quickstart_section(_project_name, context)` — Build quick start section from entry points.
- `_build_api_section(_project_name, context)` — Build API overview section with classes and functions.
- `_build_structure_section(_project_name, context)` — Build project structure section from module tree.
- `_build_endpoints_section(_project_name, context)` — Build endpoints section from detected routes.
- `write(self, path, content)` — Write README, respecting sync markers if existing file has them.

## Functions

### `generate_docs(project_path, config)`

High-level function to generate all documentation.

- Calls: `ProjectScanner`, `scanner.analyze`, `None.generate`, `None.generate`, `None.generate`, `Code2DocsConfig`, `None.generate_all`, `None.generate_all`, `None.generate`, `ReadmeGenerator`

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

- Calls: `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`
