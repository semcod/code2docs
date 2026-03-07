# `code2docs.analyzers.dependency_scanner`

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/dependency_scanner.py`

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
