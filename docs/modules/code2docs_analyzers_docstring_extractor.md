# code2docs.analyzers.docstring_extractor

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/docstring_extractor.py` | 119 lines

## Overview

Extract and analyze docstrings from source code.

## Classes

### DocstringInfo

Parsed docstring with sections.

### DocstringExtractor

Extract and parse docstrings from AnalysisResult.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `extract_all` | `self, result` | `—` | — |
| `parse` | `self, docstring` | `—` | — |
| `_extract_summary` | `lines` | `—` | — |
| `_classify_section` | `line` | `—` | — |
| `_parse_sections` | `self, lines, info` | `—` | — |
| `coverage_report` | `self, result` | `—` | — |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 119 |
| Functions | 6 |
| Classes | 2 |
| Fan-out | 35 |
