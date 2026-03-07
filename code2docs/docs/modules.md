# code2docs — Module Reference

> 38 modules | 229 functions | 51 classes

## Module Overview

| Module | Lines | Functions | Classes | CC avg | Description | Source |
|--------|-------|-----------|---------|--------|-------------|--------|
| `analyzers.dependency_scanner` | 159 | 0 | 3 | 4.5 | Scan project dependencies from requirements.txt, pyproject.t | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py) |
| `analyzers.docstring_extractor` | 140 | 0 | 2 | 3.5 | Extract and analyze docstrings from source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py) |
| `analyzers.endpoint_detector` | 113 | 0 | 2 | 4.0 | Detect web framework endpoints (Flask, FastAPI, Django) from | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py) |
| `analyzers.project_scanner` | 42 | 1 | 1 | 1.2 | Wrapper around code2llm's ProjectAnalyzer for documentation  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py) |
| `base` | 46 | 0 | 2 | 1.0 | Base generator interface and generation context. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py) |
| `cli` | 316 | 13 | 1 | 3.4 | CLI interface for code2docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py) |
| `code2docs` | 32 | 1 | 0 | 4.0 | code2docs - Auto-generate and sync project documentation fro | [source](https://github.com/wronai/code2docs/blob/main/code2docs/__init__.py) |
| `config` | 240 | 0 | 6 | 3.2 | Configuration for code2docs documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py) |
| `formatters.badges` | 52 | 2 | 0 | 7.5 | Badge generation using shields.io URLs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py) |
| `formatters.markdown` | 73 | 0 | 1 | 1.2 | Markdown formatting utilities. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py) |
| `formatters.toc` | 63 | 3 | 0 | 3.3 | Table of contents generator from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py) |
| `generators` | 59 | 1 | 0 | 5.0 | Documentation generators — produce Markdown, examples, and d | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py) |
| `generators._registry_adapters` | 228 | 0 | 12 | 1.7 | Registry adapters — wrap existing generators into BaseGenera | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py) |
| `generators._source_links` | 76 | 0 | 1 | 3.0 | Helper for generating source code links in documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py) |
| `generators.api_changelog_gen` | 196 | 0 | 2 | 5.4 | API changelog generator — diff function/class signatures bet | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py) |
| `generators.api_reference_gen` | 163 | 0 | 1 | 8.7 | API reference documentation generator — single consolidated  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py) |
| `generators.architecture_gen` | 294 | 0 | 1 | 6.9 | Architecture documentation generator with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py) |
| `generators.changelog_gen` | 121 | 0 | 2 | 3.5 | Changelog generator from git log and API diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py) |
| `generators.config_docs_gen` | 125 | 0 | 1 | 4.2 | Configuration documentation generator. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py) |
| `generators.contributing_gen` | 136 | 0 | 1 | 2.5 | CONTRIBUTING.md generator from project tooling detection. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py) |
| `generators.coverage_gen` | 104 | 0 | 1 | 4.4 | Docstring coverage report generator. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py) |
| `generators.depgraph_gen` | 140 | 0 | 1 | 3.9 | Dependency graph generator — Mermaid diagram from coupling m | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py) |
| `generators.examples_gen` | 399 | 0 | 1 | 5.6 | Auto-generate usage examples from public signatures and entr | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py) |
| `generators.getting_started_gen` | 166 | 0 | 1 | 5.8 | Getting Started guide generator. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py) |
| `generators.mkdocs_gen` | 70 | 0 | 1 | 2.2 | MkDocs configuration generator — auto-generate mkdocs.yml fr | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py) |
| `generators.module_docs_gen` | 198 | 0 | 1 | 8.0 | Module documentation generator — single consolidated modules | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py) |
| `generators.readme_gen` | 463 | 1 | 1 | 5.7 | README.md generator from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py) |
| `llm_helper` | 161 | 1 | 1 | 2.3 | LLM helper — optional LLM-assisted documentation generation  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py) |
| `registry` | 39 | 0 | 1 | 2.5 | Generator registry — pluggable generator system. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py) |
| `sync.differ` | 125 | 0 | 2 | 3.6 | Detect changes in source code for selective documentation re | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py) |
| `sync.updater` | 51 | 0 | 1 | 3.0 | Selectively regenerate documentation for changed modules. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py) |
| `sync.watcher` | 75 | 1 | 0 | 5.0 | File watcher for auto-resync on source changes (requires wat | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py) |

## Core

### `base` [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py)

Base generator interface and generation context.

**`BaseGenerator`** (ABC) [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L22)
: Abstract base for all documentation generators.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 1 |

**`GenerateContext`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L14)
: Shared context passed to all generators during a run.

### `cli` [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py)

CLI interface for code2docs.

**`DefaultGroup`** (click.Group) [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L17)
: Click Group that routes unknown subcommands to 'generate'.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `parse_args` | `ctx, args` | `—` | 4 |

- `check(project_path, config_path, target)` — Health check — verify documentation completeness. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L106)
- `diff(project_path, config_path)` — Preview what would change without writing anything. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L115)
- `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model)` — Generate documentation (default command). [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L43)
- `init(project_path, output)` — Initialize code2docs.yaml configuration file. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L90)
- `main()` — code2docs — Auto-generate project documentation from source code. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L29)
- `sync(project_path, config_path, verbose, dry_run)` — Synchronize documentation with source code changes. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L65)
- `watch(project_path, config_path, verbose)` — Watch for file changes and auto-regenerate docs. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L78)

### `config` [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py)

Configuration for code2docs documentation generation.

**`Code2DocsConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L82)
: Main configuration for code2docs.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `from_yaml` | `cls, path` | `—` | 9 |
| `to_yaml` | `path` | `—` | 1 |

**`DocsConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L33)
: Configuration for docs/ generation.

**`ExamplesConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L42)
: Configuration for examples/ generation.

**`LLMConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L57)
: Configuration for optional LLM-assisted documentation generation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `from_env` | `cls` | `—` | 1 |

**`ReadmeConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L20)
: Configuration for README generation.

**`SyncConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L49)
: Configuration for synchronization.

### `generators` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py)

Documentation generators — produce Markdown, examples, and diagrams.

- `generate_docs(project_path, config)` — High-level function to generate all documentation. [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py#L35)

### `llm_helper` [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py)

LLM helper — optional LLM-assisted documentation generation via litellm.

**`LLMHelper`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py#L31)
: Thin wrapper around litellm for documentation generation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `complete` | `prompt, system` | `—` | 7 |
| `generate_project_description` | `project_name, modules_summary, entry_points` | `—` | 1 |
| `generate_architecture_summary` | `project_name, layers, patterns` | `—` | 1 |
| `generate_getting_started_summary` | `project_name, cli_commands, public_api` | `—` | 1 |
| `enhance_module_docstring` | `module_name, functions, classes` | `—` | 1 |

### `registry` [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py)

Generator registry — pluggable generator system.

**`GeneratorRegistry`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py#L10)
: Registry of documentation generators.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `add` | `generator` | `—` | 1 |
| `run_all` | `ctx` | `—` | 4 |
| `run_only` | `name, ctx` | `—` | 4 |

## analyzers

### `analyzers.dependency_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py)

Scan project dependencies from requirements.txt, pyproject.toml, setup.py.

**`DependencyInfo`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L18)
: Information about a project dependency.

**`DependencyScanner`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L37)
: Scan and parse project dependency files.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `scan` | `project_path` | `—` | 4 |

**`ProjectDependencies`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L27)
: All detected project dependencies.

### `analyzers.docstring_extractor` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py)

Extract and analyze docstrings from source code.

**`DocstringExtractor`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23)
: Extract and parse docstrings from AnalysisResult.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `extract_all` | `result` | `—` | 5 |
| `parse` | `docstring` | `—` | 2 |
| `coverage_report` | `result` | `—` | 8 |

**`DocstringInfo`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12)
: Parsed docstring with sections.

### `analyzers.endpoint_detector` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py)

Detect web framework endpoints (Flask, FastAPI, Django) from AST analysis.

**`Endpoint`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13)
: Represents a detected web endpoint.

**`EndpointDetector`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26)
: Detects web endpoints from decorator patterns in source code.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `detect` | `result, project_path` | `—` | 5 |

### `analyzers.project_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py)

Wrapper around code2llm's ProjectAnalyzer for documentation purposes.

**`ProjectScanner`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11)
: Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `analyze` | `project_path` | `—` | 1 |

- `analyze_and_document(project_path, config)` — Convenience function: analyze a project in one call. [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39)

## formatters

### `formatters.badges` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py)

Badge generation using shields.io URLs.

- `generate_badges(project_name, badge_types, stats, deps)` — Generate shields.io badge Markdown strings. [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7)

### `formatters.markdown` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py)

Markdown formatting utilities.

**`MarkdownFormatter`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6)
: Helper for constructing Markdown documents.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `heading` | `text, level` | `—` | 1 |
| `paragraph` | `text` | `—` | 1 |
| `blockquote` | `text` | `—` | 1 |
| `code_block` | `code, language` | `—` | 1 |
| `inline_code` | `text` | `—` | 1 |
| `bold` | `text` | `—` | 1 |
| `link` | `text, url` | `—` | 1 |
| `list_item` | `text, indent` | `—` | 1 |
| `table` | `headers, rows` | `—` | 4 |
| `separator` | `` | `—` | 1 |
| `blank` | `` | `—` | 1 |
| `render` | `` | `—` | 1 |

### `formatters.toc` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py)

Table of contents generator from Markdown headings.

- `extract_headings(content, max_depth)` — Extract headings from Markdown content. [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30)
- `generate_toc(markdown_content, max_depth)` — Generate a table of contents from Markdown headings. [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7)

## generators

### `generators._registry_adapters` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py)

Registry adapters — wrap existing generators into BaseGenerator interface.

**`ApiChangelogAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L115)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ApiReferenceAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L33)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`ArchitectureAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L67)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`ConfigDocsAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L182)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ContributingAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L199)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`CoverageAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L99)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`DepGraphAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L83)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ExamplesAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L132)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`GettingStartedAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L165)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`MkDocsAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L149)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ModuleDocsAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`ReadmeGeneratorAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L13)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 3 |

### `generators._source_links` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py)

Helper for generating source code links in documentation.

**`SourceLinker`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11)
: Build source-code links (relative paths + optional GitHub/GitLab URLs).

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `source_link` | `file, line` | `—` | 5 |
| `file_link` | `file` | `—` | 1 |

### `generators.api_changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py)

API changelog generator — diff function/class signatures between versions.

**`ApiChange`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16)
: A single API change between two analysis snapshots.

**`ApiChangelogGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30)
: Generate API changelog by diffing current analysis with a saved snapshot.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `project_path` | `—` | 2 |
| `save_snapshot` | `project_path` | `—` | 1 |

### `generators.api_reference_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py)

API reference documentation generator — single consolidated api.md.

**`ApiReferenceGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13)
: Generate docs/api.md — consolidated API reference.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 11 |

### `generators.architecture_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py)

Architecture documentation generator with Mermaid diagrams.

**`ArchitectureGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12)
: Generate docs/architecture.md — architecture overview with diagrams.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 13 |

### `generators.changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py)

Changelog generator from git log and API diff.

**`ChangelogEntry`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14)
: A single changelog entry.

**`ChangelogGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23)
: Generate CHANGELOG.md from git log and analysis diff.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `project_path, max_entries` | `—` | 3 |

### `generators.config_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py)

Configuration documentation generator.

**`ConfigDocsGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11)
: Generate docs/configuration.md from Code2DocsConfig dataclass.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 4 |

### `generators.contributing_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py)

CONTRIBUTING.md generator from project tooling detection.

**`ContributingGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11)
: Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |

### `generators.coverage_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py)

Docstring coverage report generator.

**`CoverageGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11)
: Generate docs/coverage.md — docstring coverage report.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |

### `generators.depgraph_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py)

Dependency graph generator — Mermaid diagram from coupling matrix.

**`DepGraphGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12)
: Generate docs/dependency-graph.md with Mermaid diagrams.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |

### `generators.examples_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py)

Auto-generate usage examples from public signatures and entry points.

**`ExamplesGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L54)
: Generate examples/ — usage examples from public API signatures.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate_all` | `` | `—` | 1 |
| `write_all` | `output_dir, files` | `—` | 2 |

### `generators.getting_started_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py)

Getting Started guide generator.

**`GettingStartedGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12)
: Generate docs/getting-started.md from entry points and dependencies.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 3 |

### `generators.mkdocs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py)

MkDocs configuration generator — auto-generate mkdocs.yml from docs tree.

**`MkDocsGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13)
: Generate mkdocs.yml from the docs/ directory structure.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `docs_dir` | `—` | 2 |
| `write` | `output_path, content` | `—` | 1 |

### `generators.module_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py)

Module documentation generator — single consolidated modules.md.

**`ModuleDocsGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14)
: Generate docs/modules.md — consolidated module documentation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 18 |

### `generators.readme_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py)

README.md generator from AnalysisResult.

**`ReadmeGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L23)
: Generate README.md from AnalysisResult.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 3 |
| `write` | `path, content` | `—` | 4 |

- `generate_readme(project_path, output, sections, sync_markers, config)` — Convenience function to generate a README. [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L446)

## sync

### `sync.differ` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py)

Detect changes in source code for selective documentation regeneration.

**`ChangeInfo`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15)
: Describes a detected change.

**`Differ`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27)
: Detect changes between current source and previous state.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `detect_changes` | `project_path` | `—` | 6 |
| `save_state` | `project_path` | `—` | 1 |

### `sync.updater` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py)

Selectively regenerate documentation for changed modules.

**`Updater`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10)
: Apply selective documentation updates based on detected changes.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `apply` | `project_path, changes` | `—` | 4 |

### `sync.watcher` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py)

File watcher for auto-resync on source changes (requires watchdog).

- `start_watcher(project_path, config)` — Start watching project for file changes and auto-resync docs. [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10)
