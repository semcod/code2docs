# `code2docs.analyzers.docstring_extractor`

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/docstring_extractor.py`

## Classes

### `DocstringExtractor`

Extract and parse docstrings from AnalysisResult.

#### Methods

- `extract_all(self, result)` — Extract docstrings for all functions and classes.
- `parse(self, docstring)` — Parse a docstring into structured sections (orchestrator).
- `_extract_summary(lines)` — Extract the first-line summary.
- `_classify_section(line)` — Classify a line as a section header, or return None.
- `_parse_sections(self, lines, info)` — Walk remaining lines, dispatching content to the right section.
- `coverage_report(self, result)` — Calculate docstring coverage statistics.

### `DocstringInfo`

Parsed docstring with sections.
