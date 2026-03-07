# `code2docs.analyzers.project_scanner`

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/project_scanner.py`

## Classes

### `ProjectScanner`

Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

#### Methods

- `__init__(self, config)`
- `_build_llm_config(self)` — Create code2llm Config tuned for documentation generation.
- `analyze(self, project_path)` — Analyze a project and return AnalysisResult for doc generation.

## Functions

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

- Calls: `ProjectScanner`, `scanner.analyze`
