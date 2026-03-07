# code2docs.formatters.toc

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/toc.py` | 63 lines

## Overview

Table of contents generator from Markdown headings.

## Functions

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
| Lines | 63 |
| Functions | 3 |
| Classes | 0 |
| Fan-in | 4 |
| Fan-out | 18 |
