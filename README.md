# code2docs

![version](https://img.shields.io/badge/version-0.1.5-blue) ![python](https://img.shields.io/badge/python-%3E%3D3.9-blue) ![docs](https://img.shields.io/badge/docs-auto--generated-blueviolet)

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
<!-- code2docs:start -->
... auto-generated content ...
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
