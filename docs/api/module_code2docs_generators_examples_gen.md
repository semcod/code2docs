# `code2docs.generators.examples_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/examples_gen.py`

## Classes

### `ExamplesGenerator`

Generate examples/ — usage examples from public API signatures.

#### Methods

- `__init__(self, config, result)`
- `generate_all(self)` — Generate all example files. Returns {filename: content}.
- `_generate_basic_usage(self)` — Generate basic_usage.py example (orchestrator).
- `_generate_import_section(self, project_name, public_classes, public_functions)` — Generate import statements for the example.
- `_generate_class_usage_section(self, public_classes)` — Generate class instantiation and method call examples.
- `_generate_function_usage_section(self, public_functions)` — Generate standalone function call examples.
- `_generate_entry_point_examples(self)` — Generate examples based on entry points.
- `_generate_class_examples(self, classes)` — Generate examples for major classes.
- `_get_major_classes(self)` — Get classes with most methods (likely most important).
- `_get_init_args(self, cls)` — Get __init__ args for a class.
- `_get_public_methods(self, cls)` — Get public methods of a class.
- `write_all(self, output_dir, files)` — Write all generated example files.
