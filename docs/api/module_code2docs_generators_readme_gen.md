# `code2docs.generators.readme_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/readme_gen.py`

## Classes

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

## Functions

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

- Calls: `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`
