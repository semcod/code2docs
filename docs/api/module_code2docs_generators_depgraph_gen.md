# `code2docs.generators.depgraph_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/depgraph_gen.py`

## Classes

### `DepGraphGenerator`

Generate docs/dependency-graph.md with Mermaid diagrams.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate dependency-graph.md content.
- `_collect_edges(self)` — Build directed edges from module imports.
- `_import_matches(imp, module)` — Check if an import string refers to a known module.
- `_render_mermaid(self, edges)` — Render Mermaid graph from edges.
- `_render_matrix(self, edges)` — Render a coupling matrix as a Markdown table.
- `_calc_degrees(edges)` — Calculate in-degree and out-degree per module.
- `_render_degree_table(self, in_deg, out_deg)` — Render fan-in/fan-out table.
