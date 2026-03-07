# code2docs.formatters

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/__init__.py` | 7 lines

## Overview

Formatters — Markdown rendering, badges, TOC generation.

## Classes

### MarkdownFormatter

Helper for constructing Markdown documents.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self` | `—` | — |
| `heading` | `self, text, level` | `—` | — |
| `paragraph` | `self, text` | `—` | — |
| `blockquote` | `self, text` | `—` | — |
| `code_block` | `self, code, language` | `—` | — |
| `inline_code` | `self, text` | `—` | — |
| `bold` | `self, text` | `—` | — |
| `link` | `self, text, url` | `—` | — |
| `list_item` | `self, text, indent` | `—` | — |
| `table` | `self, headers, rows` | `—` | — |
| `separator` | `self` | `—` | — |
| `blank` | `self` | `—` | — |
| `render` | `self` | `—` | — |

## Functions

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

**Calls:** `None.join`, `code2docs.formatters.badges._make_badge`, `badges.append`

**Called by:** `code2docs.generators.readme_gen.ReadmeGenerator._build_context`, `code2docs.generators.readme_gen.ReadmeGenerator._build_context`

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

**Calls:** `quote`, `quote`, `hasattr`, `stats.get`

**Called by:** `code2docs.formatters.badges.generate_badges`, `code2docs.formatters.badges.generate_badges`

### `generate_toc(markdown_content, max_depth)`

Generate a table of contents from Markdown headings.

Args:
    markdown_content: Full Markdown document.
    max_depth: Maximum heading level to include (1-6).

Returns:
    TOC as Markdown string.

**Calls:** `code2docs.formatters.toc.extract_headings`, `lines.append`, `None.join`, `lines.append`

### `extract_headings(content, max_depth)`

Extract headings from Markdown content.

Returns list of (level, text, anchor) tuples.

**Calls:** `content.splitlines`, `None.startswith`, `re.match`, `len`, `line.strip`, `match.group`, `None.strip`, `code2docs.formatters.toc._slugify`, `headings.append`, `match.group`

**Called by:** `code2docs.formatters.toc.generate_toc`, `code2docs.formatters.toc.generate_toc`

### `_slugify(text)`

Convert heading text to GitHub-compatible anchor slug.

**Calls:** `text.lower`, `re.sub`, `re.sub`, `slug.strip`

**Called by:** `code2docs.formatters.toc.extract_headings`, `code2docs.formatters.toc.extract_headings`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 7 |
| Functions | 0 |
| Classes | 0 |
