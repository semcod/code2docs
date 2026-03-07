# `code2docs.generators.architecture_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/architecture_gen.py`

## Classes

### `ArchitectureGenerator`

Generate docs/architecture.md — architecture overview with diagrams.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate architecture documentation.
- `_generate_module_graph(self)` — Generate Mermaid module dependency graph.
- `_generate_class_diagram(self)` — Generate Mermaid class diagram for key classes.
- `_detect_layers(self)` — Detect architectural layers from module names.
- `_generate_metrics_table(self)` — Generate metrics summary table.
