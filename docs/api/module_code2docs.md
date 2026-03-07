# `code2docs`

> Source: `/home/tom/github/wronai/code2docs/code2docs/__init__.py`

## Classes

### `DependencyInfo`

Information about a project dependency.

### `DependencyScanner`

Scan and parse project dependency files.

#### Methods

- `scan(self, project_path)` — Scan project for dependency information.
- `_parse_pyproject(self, path)` — Parse pyproject.toml for dependencies.
- `_parse_pyproject_regex(self, path)` — Fallback regex-based pyproject.toml parser.
- `_parse_setup_py(self, path)` — Parse setup.py for dependencies (regex-based, no exec).
- `_parse_requirements_txt(self, path)` — Parse requirements.txt.
- `_parse_dep_string(dep_str)` — Parse a dependency string like 'package>=1.0'.

### `ProjectDependencies`

All detected project dependencies.

### `DocstringExtractor`

Extract and parse docstrings from AnalysisResult.

#### Methods

- `extract_all(self, result)` — Extract docstrings for all functions and classes.
- `parse(self, docstring)` — Parse a docstring into structured sections (orchestrator).
- `_extract_summary(lines)` — Extract the first-line summary.
- `_classify_section(line)` — Classify a line as a section header, or return None.
- `_parse_sections(self, lines, info)` — Walk remaining lines, dispatching content to the right section.
- `coverage_report(self, result)` — Calculate docstring coverage statistics.

### `DocstringInfo`

Parsed docstring with sections.

### `Endpoint`

Represents a detected web endpoint.

### `EndpointDetector`

Detects web endpoints from decorator patterns in source code.

#### Methods

- `detect(self, result, project_path)` — Detect all endpoints from the analysis result.
- `_parse_decorator(self, decorator, func)` — Try to parse a route decorator string.
- `_scan_django_urls(self, project_path)` — Scan urls.py files for Django URL patterns.

### `ProjectScanner`

Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

#### Methods

- `__init__(self, config)`
- `_build_llm_config(self)` — Create code2llm Config tuned for documentation generation.
- `analyze(self, project_path)` — Analyze a project and return AnalysisResult for doc generation.

### `DefaultGroup`

Inherits from: `click.Group`

Click Group that routes unknown subcommands to 'generate'.

#### Methods

- `parse_args(self, ctx, args)`

### `Code2DocsConfig`

Main configuration for code2docs.

#### Methods

- `from_yaml(cls, path)` — Load configuration from code2docs.yaml.
- `to_yaml(self, path)` — Save configuration to YAML file.

### `DocsConfig`

Configuration for docs/ generation.

### `ExamplesConfig`

Configuration for examples/ generation.

### `ReadmeConfig`

Configuration for README generation.

### `SyncConfig`

Configuration for synchronization.

### `MarkdownFormatter`

Helper for constructing Markdown documents.

#### Methods

- `__init__(self)`
- `heading(self, text, level)` — Add a heading.
- `paragraph(self, text)` — Add a paragraph.
- `blockquote(self, text)` — Add a blockquote.
- `code_block(self, code, language)` — Add a fenced code block.
- `inline_code(self, text)` — Return inline code string.
- `bold(self, text)` — Return bold string.
- `link(self, text, url)` — Return a Markdown link.
- `list_item(self, text, indent)` — Add a list item.
- `table(self, headers, rows)` — Add a Markdown table.
- `separator(self)` — Add a horizontal rule.
- `blank(self)` — Add a blank line.
- `render(self)` — Render accumulated Markdown to string.

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

### `ChangeInfo`

Describes a detected change.

#### Methods

- `__str__(self)`

### `Differ`

Detect changes between current source and previous state.

#### Methods

- `__init__(self, config)`
- `detect_changes(self, project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(self, project_path)` — Save current file hashes as state.
- `_load_state(self, state_path)` — Load previous state from file.
- `_compute_state(self, project)` — Compute file hashes for all Python files in the project.
- `_file_to_module(filepath, project)` — Convert file path to module name.

### `Updater`

Apply selective documentation updates based on detected changes.

#### Methods

- `__init__(self, config)`
- `apply(self, project_path, changes)` — Regenerate documentation for changed modules.

## Functions

### `__getattr__(name)`

Lazy import heavy modules on first access.

- Calls: `AttributeError`

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

- Calls: `ProjectScanner`, `scanner.analyze`

### `_load_config(project_path, config_path)`

Load configuration, auto-detecting code2docs.yaml if present.

- Calls: `None.resolve`, `Code2DocsConfig`, `Code2DocsConfig.from_yaml`, `candidate.exists`, `Path`, `Code2DocsConfig.from_yaml`, `str`

### `_run_generate(project_path, config, readme_only, dry_run)`

Run full documentation generation.

- Calls: `None.resolve`, `click.echo`, `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `readme_gen.generate`, `docs_dir.mkdir`, `DepGraphGenerator`, `depgraph_gen.generate`, `CoverageGenerator`

### `_run_sync(project_path, config, dry_run)`

Run sync — regenerate only changed documentation.

- Calls: `None.resolve`, `click.echo`, `Differ`, `differ.detect_changes`, `click.echo`, `Updater`, `updater.apply`, `click.echo`, `str`, `click.echo`

### `_run_watch(project_path, config)`

Run file watcher for auto-resync.

- Calls: `None.resolve`, `click.echo`, `code2docs.sync.watcher.start_watcher`, `str`, `click.echo`, `sys.exit`, `Path`

### `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run)`

Generate documentation (default command).

- Calls: `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_generate`

### `init(project_path, output)`

Initialize code2docs.yaml configuration file.

- Calls: `main.command`, `click.argument`, `click.option`, `None.resolve`, `Code2DocsConfig`, `config.to_yaml`, `click.echo`, `str`, `click.Path`, `Path`

### `main()`

code2docs — Auto-generate project documentation from source code.

- Calls: `click.group`

### `sync(project_path, config_path, verbose, dry_run)`

Synchronize documentation with source code changes.

- Calls: `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_sync`, `click.Path`

### `watch(project_path, config_path, verbose)`

Watch for file changes and auto-regenerate docs.

- Calls: `main.command`, `click.argument`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_watch`, `click.Path`

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

- Calls: `quote`, `quote`, `hasattr`, `stats.get`

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

- Calls: `None.join`, `code2docs.formatters.badges._make_badge`, `badges.append`

### `_slugify(text)`

Convert heading text to GitHub-compatible anchor slug.

- Calls: `text.lower`, `re.sub`, `re.sub`, `slug.strip`

### `extract_headings(content, max_depth)`

Extract headings from Markdown content.

Returns list of (level, text, anchor) tuples.

- Calls: `content.splitlines`, `None.startswith`, `re.match`, `len`, `line.strip`, `match.group`, `None.strip`, `code2docs.formatters.toc._slugify`, `headings.append`, `match.group`

### `generate_toc(markdown_content, max_depth)`

Generate a table of contents from Markdown headings.

Args:
    markdown_content: Full Markdown document.
    max_depth: Maximum heading level to include (1-6).

Returns:
    TOC as Markdown string.

- Calls: `code2docs.formatters.toc.extract_headings`, `lines.append`, `None.join`, `lines.append`

### `generate_docs(project_path, config)`

High-level function to generate all documentation.

- Calls: `ProjectScanner`, `scanner.analyze`, `None.generate`, `None.generate`, `None.generate`, `Code2DocsConfig`, `None.generate_all`, `None.generate_all`, `None.generate`, `ReadmeGenerator`

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

- Calls: `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

- Calls: `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`
