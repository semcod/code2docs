# code2docs.generators.depgraph_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/depgraph_gen.py` | 112 lines

## Overview

Dependency graph generator — Mermaid diagram from coupling matrix.

## Classes

### DepGraphGenerator

Generate docs/dependency-graph.md with Mermaid diagrams.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | — |
| `generate` | `self` | `—` | — |
| `_collect_edges` | `self` | `—` | — |
| `_import_matches` | `imp, module` | `—` | — |
| `_render_mermaid` | `self, edges` | `—` | — |
| `_render_matrix` | `self, edges` | `—` | — |
| `_calc_degrees` | `edges` | `—` | — |
| `_render_degree_table` | `self, in_deg, out_deg` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 112 |
| Functions | 8 |
| Classes | 1 |
| Fan-out | 42 |
