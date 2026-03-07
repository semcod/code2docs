# `code2docs.generators.module_docs_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/module_docs_gen.py`

## Classes

### `ModuleDocsGenerator`

Generate docs/modules/ — detailed per-module documentation.

#### Methods

- `__init__(self, config, result)`
- `generate_all(self)` — Generate documentation for all modules. Returns {filename: content}.
- `_generate_module(self, mod_name, mod_info)` — Generate detailed documentation for a single module (orchestrator).
- `_render_header(self, mod_name, mod_info)` — Render module title and source metadata.
- `_render_overview(self, mod_info)` — Render module overview from docstring.
- `_render_classes_section(self, mod_name)` — Render classes and their method tables.
- `_render_functions_section(self, mod_name)` — Render standalone functions with signatures and call info.
- `_render_dependencies_section(self, mod_info)` — Render imports split into internal and stdlib.
- `_render_metrics_section(self, mod_name, mod_info)` — Render metrics summary table.
- `_count_file_lines(self, file_path)` — Count lines in source file.
- `_calc_module_avg_cc(self, mod_name)` — Calculate average cyclomatic complexity for module functions.
- `_get_module_docstring(self, mod_info)` — Try to extract module-level docstring.
- `_get_module_classes(self, mod_name)`
- `_get_module_functions(self, mod_name)`
- `_get_class_methods(self, cls_info)`
- `_get_module_metrics(self, mod_name, mod_info)`
- `write_all(self, output_dir, files)` — Write all generated module docs.
