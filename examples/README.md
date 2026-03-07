# code2docs Examples

This directory contains runnable examples demonstrating various features of code2docs.

## Quick Start

```bash
# Run any example
python examples/01_cli_usage.py
python examples/02_configuration.py
# etc.
```

## Examples Overview

### 01_cli_usage.py - CLI Usage
Learn how to use code2docs from the command line:
- Basic documentation generation
- Dry runs and preview mode
- Watch mode for auto-regeneration
- Running CLI programmatically via Python

### 02_configuration.py - Configuration
Set up code2docs with custom settings:
- Programmatic configuration
- YAML configuration files
- Advanced configuration options

### 03_programmatic_api.py - Programmatic API
Use code2docs in your Python code:
- Basic programmatic usage
- Full documentation pipeline
- Working with analysis results
- Conditional documentation generation

### 04_sync_and_watch.py - Sync and Watch
Keep docs in sync with code changes:
- Detecting changes
- Incremental updates
- File watcher with auto-regeneration
- Git integration

### 05_custom_generators.py - Custom Generators
Build your own documentation generators:
- Creating custom generators
- Metrics report generator
- API changelog generator
- Extending base generator classes

### 06_formatters.py - Formatters and Utilities
Working with markdown formatting:
- Markdown formatting utilities
- Badge generation
- Table of contents generation
- Building complex documents

### 07_web_frameworks.py - Web Framework Integration
Document Flask/FastAPI endpoints:
- Detecting endpoints
- Generating API documentation
- Working with Flask/FastAPI apps

## Running Examples

Each example file contains runnable code. Uncomment the function calls at the bottom of each file to run them:

```python
if __name__ == "__main__":
    # Run specific examples
    # detect_changes_example("./my_project")
    # update_docs_incrementally("./my_project")
    pass
```

## Prerequisites

Install code2docs in your environment:

```bash
pip install code2docs
```

Or install from source:

```bash
pip install -e .
```

## More Resources

- [Full Documentation](../README.md)
- [API Reference](../docs/API.md)
- [Configuration Guide](../docs/CONFIGURATION.md)
