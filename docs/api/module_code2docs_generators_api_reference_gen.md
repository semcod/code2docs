# `code2docs.generators.api_reference_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/api_reference_gen.py`

## Classes

### `ApiReferenceGenerator`

Generate docs/api/ — per-module API reference from signatures.

#### Methods

- `__init__(self, config, result)`
- `generate_all(self)` — Generate API reference for all modules. Returns {filename: content}.
- `_generate_index(self)` — Generate API index page.
- `_generate_module_api(self, mod_name, mod_info)` — Generate API reference for a single module (orchestrator).
- `_render_api_header(self, mod_name, mod_info)` — Render module header with source info.
- `_render_api_classes(self, mod_name)` — Render classes with their method signatures.
- `_render_api_functions(self, mod_name)` — Render standalone functions with signatures and complexity.
- `_render_api_imports(self, mod_info)` — Render module imports list.
- `_get_class_methods(self, cls_info)` — Get FunctionInfo objects for class methods.
- `_format_signature(func)` — Format a function signature string.
- `write_all(self, output_dir, files)` — Write all generated API reference files.
