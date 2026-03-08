# Getting Started with code2docs

## Prerequisites

- Python >=3.9
- pip (or your preferred package manager)

## Installation

```bash
pip install .
```

To install from source:

```bash
git clone <repository-url>
cd code2docs
pip install -e .
```

## Quick Start

### Command Line

```bash
# Generate full documentation for your project
code2docs ./path/to/your/project

# Preview what would be generated (no file writes)
code2docs ./path/to/your/project --dry-run

# Only regenerate README
code2docs ./path/to/your/project --readme-only
```

### Python API

```python
from analyzers.project_scanner import analyze_and_document

# Convenience function: analyze a project in one call.
result = analyze_and_document("project_path", config=...)
```

## What's Next

- 📖 [API Reference](api.md) — Full function and class documentation
- 🏗️ [Architecture](architecture.md) — System design and module relationships
- 📊 [Coverage Report](coverage.md) — Docstring coverage analysis
- 🔗 [Dependency Graph](dependency-graph.md) — Module dependency visualization
