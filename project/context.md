# System Architecture Analysis

## Overview

- **Project**: code2docs
- **Language**: python
- **Files**: 34
- **Lines**: 7585
- **Functions**: 258
- **Classes**: 57
- **Avg CC**: 4.4
- **Critical (CC≥10)**: 28

## Architecture

### code2docs/ (7 files, 900L, 34 functions)

- `cli.py` — 319L, 14 methods, CC↑10
- `config.py` — 297L, 5 methods, CC↑10
- `llm_helper.py` — 161L, 7 methods, CC↑7
- `__init__.py` — 32L, 1 methods, CC↑4
- `registry.py` — 39L, 4 methods, CC↑4
- _2 more files_

### code2docs/analyzers/ (5 files, 633L, 27 functions)

- `dependency_scanner.py` — 325L, 10 methods, CC↑9
- `docstring_extractor.py` — 140L, 10 methods, CC↑8
- `endpoint_detector.py` — 113L, 3 methods, CC↑5
- `project_scanner.py` — 42L, 4 methods, CC↑2
- `__init__.py` — 13L, 0 methods, CC↑0

### code2docs/formatters/ (4 files, 195L, 18 functions)

- `badges.py` — 52L, 2 methods, CC↑11
- `toc.py` — 63L, 3 methods, CC↑6
- `markdown.py` — 73L, 13 methods, CC↑4
- `__init__.py` — 7L, 0 methods, CC↑0

### code2docs/generators/ (18 files, 3807L, 169 functions)

- `readme_gen.py` — 477L, 18 methods, CC↑29
- `api_reference_gen.py` — 163L, 7 methods, CC↑25
- `module_docs_gen.py` — 198L, 9 methods, CC↑25
- `examples_gen.py` — 443L, 15 methods, CC↑22
- `code2llm_gen.py` — 206L, 6 methods, CC↑17
- _13 more files_

### code2docs/sync/ (4 files, 257L, 10 functions)

- `differ.py` — 125L, 7 methods, CC↑6
- `watcher.py` — 75L, 1 methods, CC↑5
- `updater.py` — 51L, 2 methods, CC↑4
- `__init__.py` — 6L, 0 methods, CC↑0

### root/ (1 files, 18L, 0 functions)

- `project.sh` — 18L, 0 methods, CC↑0

## Key Exports

- **ReadmeGenerator** (class, CC̄=6.2)
  - `_extract_project_metadata` CC=29 ⚠ split
- **ApiReferenceGenerator** (class, CC̄=8.7)
  - `_render_module_section` CC=25 ⚠ split
- **ModuleDocsGenerator** (class, CC̄=8.0)
  - `generate` CC=18 ⚠ split
  - `_render_module_detail` CC=25 ⚠ split
- **ExamplesGenerator** (class, CC̄=6.1)
  - `_generate_advanced` CC=22 ⚠ split
- **Code2LlmGenerator** (class, CC̄=6.2)
  - `_run_code2llm` CC=17 ⚠ split
- **parse_gitignore** (function, CC=15) ⚠ split
- **OrgReadmeGenerator** (class, CC̄=5.2)
  - `_extract_description` CC=17 ⚠ split
- **ContributingGenerator** (class, CC̄=4.6)
  - `_render_code_style` CC=16 ⚠ split
- **GettingStartedGenerator** (class, CC̄=7.1)
  - `_render_first_usage` CC=15 ⚠ split
  - `_generate_intro` CC=16 ⚠ split
- **IndexHtmlAdapter** (class, CC̄=6.0)
  - `_generate_html` CC=15 ⚠ split
- **ApiChangelogGenerator** (class, CC̄=5.4)
- **ArchitectureGenerator** (class, CC̄=6.9)
- **DependencyScanner** (class, CC̄=6.0)

## Hotspots (High Fan-Out)

- **_run_check** — fan-out=24: Run documentation health check.
- **ReadmeGenerator._extract_project_metadata** — fan-out=23: Extract project metadata (author, license, version) from pyproject.toml or git.
- **start_watcher** — fan-out=22: Start watching project for file changes and auto-resync docs.

Requires watchdog
- **ApiReferenceGenerator._render_module_section** — fan-out=21: Render a module as a subsection within the consolidated doc.
- **OrgReadmeGenerator._extract_description** — fan-out=20: Extract short description from project (max 5 lines).
- **ModuleDocsGenerator.generate** — fan-out=19: Generate a single modules.md with all modules grouped by package.
- **Code2DocsConfig.from_yaml** — fan-out=19: Load configuration from code2docs.yaml.

## Refactoring Priorities

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | Split ModuleDocsGenerator._render_module_detail (CC=25 → target CC<10) | high | low |
| 2 | Split ApiReferenceGenerator._render_module_section (CC=25 → target CC<10) | high | low |
| 3 | Split ReadmeGenerator._extract_project_metadata (CC=29 → target CC<10) | high | low |
| 4 | Split GettingStartedGenerator._render_first_usage (CC=15 → target CC<10) | medium | low |
| 5 | Split GettingStartedGenerator._generate_intro (CC=16 → target CC<10) | medium | low |
| 6 | Split parse_gitignore (CC=15 → target CC<10) | medium | low |
| 7 | Split Code2LlmGenerator._run_code2llm (CC=17 → target CC<10) | medium | low |
| 8 | Split ModuleDocsGenerator.generate (CC=18 → target CC<10) | medium | low |
| 9 | Split OrgReadmeGenerator._extract_description (CC=17 → target CC<10) | medium | low |
| 10 | Split ExamplesGenerator._generate_advanced (CC=22 → target CC<10) | medium | low |

## Context for LLM

When suggesting changes:
1. Start from hotspots and high-CC functions
2. Follow refactoring priorities above
3. Maintain public API surface — keep backward compatibility
4. Prefer minimal, incremental changes

