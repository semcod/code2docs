# `code2docs.analyzers`

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/__init__.py`

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

## Functions

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

- Calls: `ProjectScanner`, `scanner.analyze`
