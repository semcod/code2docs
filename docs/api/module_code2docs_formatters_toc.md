# `code2docs.formatters.toc`

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/toc.py`

## Functions

### `_slugify(text)`

Convert heading text to GitHub-compatible anchor slug.

- Calls: `text.lower`, `re.sub`, `re.sub`, `slug.strip`

### `extract_headings(content, max_depth)`

Extract headings from Markdown content.

Returns list of (level, text, anchor) tuples.

- Calls: `content.splitlines`, `None.startswith`, `re.match`, `len`, `line.strip`, `match.group`, `None.strip`, `code2docs.formatters.toc._slugify`, `headings.append`, `match.group`

### `generate_toc(markdown_content, max_depth)`

Generate a table of contents from Markdown headings.

Args:
    markdown_content: Full Markdown document.
    max_depth: Maximum heading level to include (1-6).

Returns:
    TOC as Markdown string.

- Calls: `code2docs.formatters.toc.extract_headings`, `lines.append`, `None.join`, `lines.append`
