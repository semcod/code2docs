# code2docs

![version](https://img.shields.io/badge/version-0.2.8-blue) ![python](https://img.shields.io/badge/python-%3E%3D3.9-blue) ![docs](https://img.shields.io/badge/docs-auto--generated-blueviolet)

> Auto-generate and sync project documentation from source code analysis.

**code2docs** uses [code2llm](https://github.com/wronai/code2llm)'s `AnalysisResult` to produce human-readable documentation: README.md, API references, module docs, usage examples, and architecture diagrams.

```
code2llm  →  AnalysisResult  →  .toon / .mmd / context.md   (for LLM)
code2docs →  AnalysisResult  →  README.md / docs/ / examples/  (for humans)
```

## Installation

```bash
pip install code2docs
```

Or from source:

```bash
git clone https://github.com/wronai/code2docs
cd code2docs
pip install -e .
```

### Optional extras

```bash
pip install code2docs[watch]    # file watcher (watchdog)
pip install code2docs[mkdocs]   # MkDocs integration
pip install code2docs[dev]      # development tools
```

## Quick Start

```bash
# Generate full documentation for a project
code2docs ./my-project

# Generate only README
code2docs ./my-project --readme-only

# Sync (regenerate only changed modules)
code2docs sync ./my-project

# Watch mode (auto-resync on file changes)
code2docs watch ./my-project

# Initialize config file
code2docs init ./my-project

# Dry-run (show what would be generated)
code2docs ./my-project --dry-run
```

### Python API

```python
from code2docs import generate_readme, generate_docs, Code2DocsConfig

# Generate README
generate_readme("./my-project", output="README.md")

# Generate full docs with custom config
config = Code2DocsConfig(project_name="mylib", verbose=True)
docs = generate_docs("./my-project", config=config)
```

## Generated Output

```
<project>/
├── README.md                      # Main README (auto-generated sections)
├── docs/
│   ├── index.md                   # Documentation index
│   ├── architecture.md            # Architecture + Mermaid diagrams
│   ├── api/
│   │   ├── index.md               # API overview
│   │   ├── module_analyzer.md     # Per-module API reference
│   │   └── ...
│   └── modules/
│       ├── analyzer.md            # Detailed module documentation
│       └── ...
├── examples/
│   ├── basic_usage.py             # Auto-generated usage example
│   ├── class_examples.py          # Class usage examples
│   └── ...
└── code2docs.yaml                 # Generator configuration
```

## Configuration

Create `code2docs.yaml` in your project root (or run `code2docs init`):

```yaml
project:
  name: my-project
  source: ./
  output: ./docs/

readme:
  sections:
    - overview
    - install
    - quickstart
    - api
    - structure
    - endpoints
  badges:
    - version
    - python
    - coverage
    - complexity
  sync_markers: true

docs:
  api_reference: true
  module_docs: true
  architecture: true
  changelog: true

examples:
  auto_generate: true
  from_entry_points: true

sync:
  strategy: markers    # markers | full | git-diff
  watch: false
  ignore:
    - "tests/"
    - "__pycache__"
```

## Sync Markers

code2docs can update only specific sections of an existing README using markers:

```markdown
<!-- code2docs:start --># code2docs

![version](https://img.shields.io/badge/version-0.2.8-blue) ![python](https://img.shields.io/badge/python-%3E%3D3.9-blue) ![coverage](https://img.shields.io/badge/coverage-unknown-lightgrey) ![functions](https://img.shields.io/badge/functions-153-green)
> **153** functions | **30** classes | **28** files | CC̄ = 0.0

## Installation

```bash
pip install code2docs
```
Requires Python >=3.9

### Dependencies

- `code2llm` >=0.5.0
- `jinja2` >=3.1
- `click` >=8.0
- `pyyaml` >=6.0

## Quick Start

```python
# Entry point: code2docs.__getattr__
# Entry point: code2docs.sync.updater.Updater.__init__
# Entry point: code2docs.sync.updater.Updater.apply
```

## API Overview

### Classes

- **`Updater`** — Apply selective documentation updates based on detected changes.
- **`MarkdownFormatter`** — Helper for constructing Markdown documents.
- **`ReadmeGenerator`** — Generate README.md from AnalysisResult.
- **`ChangeInfo`** — Describes a detected change.
- **`Differ`** — Detect changes between current source and previous state.
- **`CoverageGenerator`** — Generate docs/coverage.md — docstring coverage report.
- **`DepGraphGenerator`** — Generate docs/dependency-graph.md with Mermaid diagrams.
- **`ModuleDocsGenerator`** — Generate docs/modules/ — detailed per-module documentation.
- **`ApiReferenceGenerator`** — Generate docs/api/ — per-module API reference from signatures.
- **`ChangelogEntry`** — A single changelog entry.
- **`ChangelogGenerator`** — Generate CHANGELOG.md from git log and analysis diff.
- **`MkDocsGenerator`** — Generate mkdocs.yml from the docs/ directory structure.
- **`ExamplesGenerator`** — Generate examples/ — usage examples from public API signatures.
- **`ApiChange`** — A single API change between two analysis snapshots.
- **`ApiChangelogGenerator`** — Generate API changelog by diffing current analysis with a saved snapshot.
- **`ArchitectureGenerator`** — Generate docs/architecture.md — architecture overview with diagrams.
- **`DefaultGroup`** — Click Group that routes unknown subcommands to 'generate'.
- **`ReadmeConfig`** — Configuration for README generation.
- **`DocsConfig`** — Configuration for docs/ generation.
- **`ExamplesConfig`** — Configuration for examples/ generation.
- **`SyncConfig`** — Configuration for synchronization.
- **`Code2DocsConfig`** — Main configuration for code2docs.
- **`ProjectScanner`** — Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.
- **`DependencyInfo`** — Information about a project dependency.
- **`ProjectDependencies`** — All detected project dependencies.
- **`DependencyScanner`** — Scan and parse project dependency files.
- **`DocstringInfo`** — Parsed docstring with sections.
- **`DocstringExtractor`** — Extract and parse docstrings from AnalysisResult.
- **`Endpoint`** — Represents a detected web endpoint.
- **`EndpointDetector`** — Detects web endpoints from decorator patterns in source code.

### Functions

- `start_watcher(project_path, config)` — Start watching project for file changes and auto-resync docs.
- `generate_badges(project_name, badge_types, stats, deps)` — Generate shields.io badge Markdown strings.
- `generate_toc(markdown_content, max_depth)` — Generate a table of contents from Markdown headings.
- `extract_headings(content, max_depth)` — Extract headings from Markdown content.
- `generate_readme(project_path, output, sections, sync_markers, config)` — Convenience function to generate a README.
- `generate_docs(project_path, config)` — High-level function to generate all documentation.
- `main()` — code2docs — Auto-generate project documentation from source code.
- `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run)` — Generate documentation (default command).
- `sync(project_path, config_path, verbose, dry_run)` — Synchronize documentation with source code changes.
- `watch(project_path, config_path, verbose)` — Watch for file changes and auto-regenerate docs.
- `init(project_path, output)` — Initialize code2docs.yaml configuration file.
- `analyze_and_document(project_path, config)` — Convenience function: analyze a project in one call.

## Project Structure

📦 `code2docs` (1 functions)
📄 `code2docs.__main__`
📦 `code2docs.analyzers`
📄 `code2docs.analyzers.dependency_scanner` (6 functions, 3 classes)
📄 `code2docs.analyzers.docstring_extractor` (6 functions, 2 classes)
📄 `code2docs.analyzers.endpoint_detector` (3 functions, 2 classes)
📄 `code2docs.analyzers.project_scanner` (4 functions, 1 classes)
📄 `code2docs.cli` (10 functions, 1 classes)
📄 `code2docs.config` (2 functions, 5 classes)
📦 `code2docs.formatters`
📄 `code2docs.formatters.badges` (2 functions)
📄 `code2docs.formatters.markdown` (13 functions, 1 classes)
📄 `code2docs.formatters.toc` (3 functions)
📦 `code2docs.generators` (1 functions)
📄 `code2docs.generators.api_changelog_gen` (9 functions, 2 classes)
📄 `code2docs.generators.api_reference_gen` (11 functions, 1 classes)
📄 `code2docs.generators.architecture_gen` (6 functions, 1 classes)
📄 `code2docs.generators.changelog_gen` (6 functions, 2 classes)
📄 `code2docs.generators.coverage_gen` (5 functions, 1 classes)
📄 `code2docs.generators.depgraph_gen` (8 functions, 1 classes)
📄 `code2docs.generators.examples_gen` (12 functions, 1 classes)
📄 `code2docs.generators.mkdocs_gen` (4 functions, 1 classes)
📄 `code2docs.generators.module_docs_gen` (17 functions, 1 classes)
📄 `code2docs.generators.readme_gen` (14 functions, 1 classes)
📦 `code2docs.sync`
📄 `code2docs.sync.differ` (7 functions, 2 classes)
📄 `code2docs.sync.updater` (2 functions, 1 classes)
📄 `code2docs.sync.watcher` (1 functions)


<!-- code2docs:end -->
```

Content outside markers is preserved.

## Architecture

```
code2docs/
├── cli.py                    # CLI (click-based)
├── config.py                 # Configuration (code2docs.yaml)
├── analyzers/                # Adapters to code2llm + custom detectors
│   ├── project_scanner.py    # Wrapper on code2llm.ProjectAnalyzer
│   ├── endpoint_detector.py  # Flask/FastAPI/Django route extraction
│   ├── docstring_extractor.py
│   └── dependency_scanner.py
├── generators/               # Documentation generators
│   ├── readme_gen.py         # README.md generator
│   ├── api_reference_gen.py  # docs/api/ reference from signatures
│   ├── module_docs_gen.py    # docs/modules/ per-module docs
│   ├── examples_gen.py       # examples/ from signatures
│   ├── changelog_gen.py      # CHANGELOG from git log
│   └── architecture_gen.py   # Architecture + Mermaid diagrams
├── templates/                # Jinja2 templates
├── sync/                     # Change detection & selective regeneration
│   ├── differ.py
│   ├── updater.py
│   └── watcher.py
└── formatters/               # Markdown, badges, TOC
```

## Requirements

- Python >= 3.9
- [code2llm](https://github.com/wronai/code2llm) >= 0.5.0
- Jinja2 >= 3.1
- Click >= 8.0
- PyYAML >= 6.0

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.

## Author

Created by **Tom Sapletta** - [tom@sapletta.com](mailto:tom@sapletta.com)
