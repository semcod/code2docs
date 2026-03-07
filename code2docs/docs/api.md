# code2docs — API Reference

> 38 modules | 228 functions | 51 classes

## Contents

- [Core](#core) (9 modules)
- [analyzers](#analyzers) (4 modules)
- [formatters](#formatters) (3 modules)
- [generators](#generators) (15 modules)
- [sync](#sync) (3 modules)

## Core

### `analyzers` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DependencyInfo` | 0 | Information about a project dependency. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L18) |
| `DependencyScanner` | 1 | Scan and parse project dependency files. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L37) |
| `ProjectDependencies` | 0 | All detected project dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L27) |
| `DocstringExtractor` | 3 | Extract and parse docstrings from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23) |
| `DocstringInfo` | 0 | Parsed docstring with sections. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12) |
| `Endpoint` | 0 | Represents a detected web endpoint. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13) |
| `EndpointDetector` | 1 | Detects web endpoints from decorator patterns in source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26) |
| `ProjectScanner` | 1 | Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11) |

**`DocstringExtractor` methods:**

- `extract_all(result)` — Extract docstrings for all functions and classes.
- `parse(docstring)` — Parse a docstring into structured sections (orchestrator).
- `coverage_report(result)` — Calculate docstring coverage statistics.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `analyze_and_document` | `analyze_and_document(project_path, config)` | 1 | Convenience function: analyze a project in one call. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39) |

### `base` [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `BaseGenerator` | 2 | Abstract base for all documentation generators. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L22) |
| `GenerateContext` | 0 | Shared context passed to all generators during a run. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L14) |

**`BaseGenerator` methods:**

- `should_run()` — Return True if this generator should execute.
- `run(ctx)` — Execute generation and write output.

### `cli` [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DefaultGroup` | 1 | Click Group that routes unknown subcommands to 'generate'. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L17) |

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `check` | `check(project_path, config_path, target)` | 1 | Health check — verify documentation completeness. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L106) |
| `diff` | `diff(project_path, config_path)` | 1 | Preview what would change without writing anything. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L115) |
| `generate` | `generate(project_path, config_path, readme_only, sections, ...)` | 6 | Generate documentation (default command). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L43) |
| `init` | `init(project_path, output)` | 1 | Initialize code2docs.yaml configuration file. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L90) |
| `main` | `main()` | 1 | code2docs — Auto-generate project documentation from source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L29) |
| `sync` | `sync(project_path, config_path, verbose, dry_run)` | 2 | Synchronize documentation with source code changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L65) |
| `watch` | `watch(project_path, config_path, verbose)` | 2 | Watch for file changes and auto-regenerate docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L78) |

### `config` [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Code2DocsConfig` | 2 | Main configuration for code2docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L82) |
| `DocsConfig` | 0 | Configuration for docs/ generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L33) |
| `ExamplesConfig` | 0 | Configuration for examples/ generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L42) |
| `LLMConfig` | 1 | Configuration for optional LLM-assisted documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L57) |
| `ReadmeConfig` | 0 | Configuration for README generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L20) |
| `SyncConfig` | 0 | Configuration for synchronization. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L49) |

**`Code2DocsConfig` methods:**

- `from_yaml(cls, path)` — Load configuration from code2docs.yaml.
- `to_yaml(path)` — Save configuration to YAML file.

### `formatters` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `MarkdownFormatter` | 12 | Helper for constructing Markdown documents. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6) |

**`MarkdownFormatter` methods:**

- `heading(text, level)` — Add a heading.
- `paragraph(text)` — Add a paragraph.
- `blockquote(text)` — Add a blockquote.
- `code_block(code, language)` — Add a fenced code block.
- `inline_code(text)` — Return inline code string.
- `bold(text)` — Return bold string.
- `link(text, url)` — Return a Markdown link.
- `list_item(text, indent)` — Add a list item.
- `table(headers, rows)` — Add a Markdown table.
- `separator()` — Add a horizontal rule.
- `blank()` — Add a blank line.
- `render()` — Render accumulated Markdown to string.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_badges` | `generate_badges(project_name, badge_types, stats, deps)` | 4 | Generate shields.io badge Markdown strings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7) |
| `extract_headings` | `extract_headings(content, max_depth)` | 6 | Extract headings from Markdown content. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30) |
| `generate_toc` | `generate_toc(markdown_content, max_depth)` | 3 | Generate a table of contents from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7) |

### `generators` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiChangelogAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L115) |
| `ApiReferenceAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L33) |
| `ArchitectureAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L67) |
| `ConfigDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L182) |
| `ContributingAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L199) |
| `CoverageAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L99) |
| `DepGraphAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L83) |
| `ExamplesAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L132) |
| `GettingStartedAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L165) |
| `MkDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L149) |
| `ModuleDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50) |
| `ReadmeGeneratorAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L13) |
| `SourceLinker` | 2 | Build source-code links (relative paths + optional GitHub/GitLab URLs). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11) |
| `ApiChange` | 1 | A single API change between two analysis snapshots. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16) |
| `ApiChangelogGenerator` | 2 | Generate API changelog by diffing current analysis with a saved snapshot. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30) |
| `ApiReferenceGenerator` | 1 | Generate docs/api.md — consolidated API reference. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13) |
| `ArchitectureGenerator` | 1 | Generate docs/architecture.md — architecture overview with diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12) |
| `ChangelogEntry` | 0 | A single changelog entry. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14) |
| `ChangelogGenerator` | 1 | Generate CHANGELOG.md from git log and analysis diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23) |
| `ConfigDocsGenerator` | 1 | Generate docs/configuration.md from Code2DocsConfig dataclass. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11) |
| `ContributingGenerator` | 1 | Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11) |
| `CoverageGenerator` | 1 | Generate docs/coverage.md — docstring coverage report. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11) |
| `DepGraphGenerator` | 1 | Generate docs/dependency-graph.md with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12) |
| `ExamplesGenerator` | 2 | Generate examples/ — usage examples from public API signatures. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L54) |
| `GettingStartedGenerator` | 1 | Generate docs/getting-started.md from entry points and dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12) |
| `MkDocsGenerator` | 2 | Generate mkdocs.yml from the docs/ directory structure. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13) |
| `ModuleDocsGenerator` | 1 | Generate docs/modules.md — consolidated module documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14) |
| `ReadmeGenerator` | 2 | Generate README.md from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L23) |

**`ApiChangelogAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ApiReferenceAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ArchitectureAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ConfigDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ContributingAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`CoverageAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`DepGraphAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ExamplesAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`GettingStartedAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`MkDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ModuleDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ReadmeGeneratorAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`SourceLinker` methods:**

- `source_link(file, line)` — Return a Markdown link to source, or empty string if unavailable.
- `file_link(file)` — Return a Markdown link to a file (no line number).

**`ApiChangelogGenerator` methods:**

- `generate(project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(project_path)` — Save current API state as snapshot for future diffs.

**`ExamplesGenerator` methods:**

- `generate_all()` — Generate all example files. Returns {filename: content}.
- `write_all(output_dir, files)` — Write all generated example files.

**`MkDocsGenerator` methods:**

- `generate(docs_dir)` — Generate mkdocs.yml content.
- `write(output_path, content)` — Write mkdocs.yml file.

**`ReadmeGenerator` methods:**

- `generate()` — Generate full README content.
- `write(path, content)` — Write README, respecting sync markers if existing file has them.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_docs` | `generate_docs(project_path, config)` | 5 | High-level function to generate all documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py#L35) |
| `generate_readme` | `generate_readme(project_path, output, sections, sync_markers, ...)` | 3 | Convenience function to generate a README. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L390) |

### `llm_helper` [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `LLMHelper` | 6 | Thin wrapper around litellm for documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py#L31) |

**`LLMHelper` methods:**

- `complete(prompt, system)` — Send a completion request. Returns None on any failure.
- `generate_project_description(project_name, modules_summary, entry_points)` — Generate a concise project description from analysis data.
- `generate_architecture_summary(project_name, layers, patterns, metrics)` — Generate a natural-language architecture overview.
- `generate_getting_started_summary(project_name, cli_commands, public_api)` — Generate a getting-started introduction.
- `enhance_module_docstring(module_name, functions, classes)` — Generate a module-level summary from its contents.

### `registry` [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `GeneratorRegistry` | 3 | Registry of documentation generators. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py#L10) |

**`GeneratorRegistry` methods:**

- `add(generator)` — Add a generator instance to the registry.
- `run_all(ctx)` — Run every registered generator that should execute.
- `run_only(name, ctx)` — Run a single generator by name.

### `sync` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ChangeInfo` | 0 | Describes a detected change. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15) |
| `Differ` | 2 | Detect changes between current source and previous state. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27) |
| `Updater` | 1 | Apply selective documentation updates based on detected changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10) |

**`Differ` methods:**

- `detect_changes(project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(project_path)` — Save current file hashes as state.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `start_watcher` | `start_watcher(project_path, config)` | 5 | Start watching project for file changes and auto-resync docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10) |

## analyzers

### `analyzers.dependency_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DependencyInfo` | 0 | Information about a project dependency. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L18) |
| `DependencyScanner` | 1 | Scan and parse project dependency files. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L37) |
| `ProjectDependencies` | 0 | All detected project dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L27) |

### `analyzers.docstring_extractor` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DocstringExtractor` | 3 | Extract and parse docstrings from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23) |
| `DocstringInfo` | 0 | Parsed docstring with sections. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12) |

**`DocstringExtractor` methods:**

- `extract_all(result)` — Extract docstrings for all functions and classes.
- `parse(docstring)` — Parse a docstring into structured sections (orchestrator).
- `coverage_report(result)` — Calculate docstring coverage statistics.

### `analyzers.endpoint_detector` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Endpoint` | 0 | Represents a detected web endpoint. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13) |
| `EndpointDetector` | 1 | Detects web endpoints from decorator patterns in source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26) |

### `analyzers.project_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ProjectScanner` | 1 | Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11) |

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `analyze_and_document` | `analyze_and_document(project_path, config)` | 1 | Convenience function: analyze a project in one call. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39) |

## formatters

### `formatters.badges` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_badges` | `generate_badges(project_name, badge_types, stats, deps)` | 4 | Generate shields.io badge Markdown strings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7) |

### `formatters.markdown` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `MarkdownFormatter` | 12 | Helper for constructing Markdown documents. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6) |

**`MarkdownFormatter` methods:**

- `heading(text, level)` — Add a heading.
- `paragraph(text)` — Add a paragraph.
- `blockquote(text)` — Add a blockquote.
- `code_block(code, language)` — Add a fenced code block.
- `inline_code(text)` — Return inline code string.
- `bold(text)` — Return bold string.
- `link(text, url)` — Return a Markdown link.
- `list_item(text, indent)` — Add a list item.
- `table(headers, rows)` — Add a Markdown table.
- `separator()` — Add a horizontal rule.
- `blank()` — Add a blank line.
- `render()` — Render accumulated Markdown to string.

### `formatters.toc` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `extract_headings` | `extract_headings(content, max_depth)` | 6 | Extract headings from Markdown content. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30) |
| `generate_toc` | `generate_toc(markdown_content, max_depth)` | 3 | Generate a table of contents from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7) |

## generators

### `generators._registry_adapters` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiChangelogAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L115) |
| `ApiReferenceAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L33) |
| `ArchitectureAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L67) |
| `ConfigDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L182) |
| `ContributingAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L199) |
| `CoverageAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L99) |
| `DepGraphAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L83) |
| `ExamplesAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L132) |
| `GettingStartedAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L165) |
| `MkDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L149) |
| `ModuleDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50) |
| `ReadmeGeneratorAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L13) |

**`ApiChangelogAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ApiReferenceAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ArchitectureAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ConfigDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ContributingAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`CoverageAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`DepGraphAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ExamplesAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`GettingStartedAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`MkDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ModuleDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ReadmeGeneratorAdapter` methods:**

- `should_run()`
- `run(ctx)`

### `generators._source_links` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `SourceLinker` | 2 | Build source-code links (relative paths + optional GitHub/GitLab URLs). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11) |

**`SourceLinker` methods:**

- `source_link(file, line)` — Return a Markdown link to source, or empty string if unavailable.
- `file_link(file)` — Return a Markdown link to a file (no line number).

### `generators.api_changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiChange` | 1 | A single API change between two analysis snapshots. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16) |
| `ApiChangelogGenerator` | 2 | Generate API changelog by diffing current analysis with a saved snapshot. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30) |

**`ApiChangelogGenerator` methods:**

- `generate(project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(project_path)` — Save current API state as snapshot for future diffs.

### `generators.api_reference_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiReferenceGenerator` | 1 | Generate docs/api.md — consolidated API reference. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13) |

### `generators.architecture_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ArchitectureGenerator` | 1 | Generate docs/architecture.md — architecture overview with diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12) |

### `generators.changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ChangelogEntry` | 0 | A single changelog entry. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14) |
| `ChangelogGenerator` | 1 | Generate CHANGELOG.md from git log and analysis diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23) |

### `generators.config_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ConfigDocsGenerator` | 1 | Generate docs/configuration.md from Code2DocsConfig dataclass. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11) |

### `generators.contributing_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ContributingGenerator` | 1 | Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11) |

### `generators.coverage_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `CoverageGenerator` | 1 | Generate docs/coverage.md — docstring coverage report. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11) |

### `generators.depgraph_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DepGraphGenerator` | 1 | Generate docs/dependency-graph.md with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12) |

### `generators.examples_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ExamplesGenerator` | 2 | Generate examples/ — usage examples from public API signatures. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L54) |

**`ExamplesGenerator` methods:**

- `generate_all()` — Generate all example files. Returns {filename: content}.
- `write_all(output_dir, files)` — Write all generated example files.

### `generators.getting_started_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `GettingStartedGenerator` | 1 | Generate docs/getting-started.md from entry points and dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12) |

### `generators.mkdocs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `MkDocsGenerator` | 2 | Generate mkdocs.yml from the docs/ directory structure. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13) |

**`MkDocsGenerator` methods:**

- `generate(docs_dir)` — Generate mkdocs.yml content.
- `write(output_path, content)` — Write mkdocs.yml file.

### `generators.module_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ModuleDocsGenerator` | 1 | Generate docs/modules.md — consolidated module documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14) |

### `generators.readme_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ReadmeGenerator` | 2 | Generate README.md from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L23) |

**`ReadmeGenerator` methods:**

- `generate()` — Generate full README content.
- `write(path, content)` — Write README, respecting sync markers if existing file has them.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_readme` | `generate_readme(project_path, output, sections, sync_markers, ...)` | 3 | Convenience function to generate a README. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L390) |

## sync

### `sync.differ` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ChangeInfo` | 0 | Describes a detected change. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15) |
| `Differ` | 2 | Detect changes between current source and previous state. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27) |

**`Differ` methods:**

- `detect_changes(project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(project_path)` — Save current file hashes as state.

### `sync.updater` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Updater` | 1 | Apply selective documentation updates based on detected changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10) |

### `sync.watcher` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `start_watcher` | `start_watcher(project_path, config)` | 5 | Start watching project for file changes and auto-resync docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10) |
