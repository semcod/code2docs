# `code2docs.generators.mkdocs_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/mkdocs_gen.py`

## Classes

### `MkDocsGenerator`

Generate mkdocs.yml from the docs/ directory structure.

#### Methods

- `__init__(self, config, result)`
- `generate(self, docs_dir)` — Generate mkdocs.yml content.
- `_build_nav(self, docs_dir)` — Build navigation structure from docs tree and analysis.
- `write(self, output_path, content)` — Write mkdocs.yml file.
