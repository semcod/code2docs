# `code2docs.generators.coverage_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/coverage_gen.py`

## Classes

### `CoverageGenerator`

Generate docs/coverage.md — docstring coverage report.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate coverage.md content.
- `_render_summary(report)` — Render overall coverage summary.
- `_render_per_module(self)` — Render per-module coverage table.
- `_render_undocumented(self)` — List all undocumented public functions and classes.
