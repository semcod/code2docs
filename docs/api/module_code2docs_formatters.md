# `code2docs.formatters`

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/__init__.py`

## Classes

### `MarkdownFormatter`

Helper for constructing Markdown documents.

#### Methods

- `__init__(self)`
- `heading(self, text, level)` — Add a heading.
- `paragraph(self, text)` — Add a paragraph.
- `blockquote(self, text)` — Add a blockquote.
- `code_block(self, code, language)` — Add a fenced code block.
- `inline_code(self, text)` — Return inline code string.
- `bold(self, text)` — Return bold string.
- `link(self, text, url)` — Return a Markdown link.
- `list_item(self, text, indent)` — Add a list item.
- `table(self, headers, rows)` — Add a Markdown table.
- `separator(self)` — Add a horizontal rule.
- `blank(self)` — Add a blank line.
- `render(self)` — Render accumulated Markdown to string.

## Functions

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

- Calls: `quote`, `quote`, `hasattr`, `stats.get`

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

- Calls: `None.join`, `code2docs.formatters.badges._make_badge`, `badges.append`

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
