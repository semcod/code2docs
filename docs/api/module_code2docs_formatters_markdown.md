# `code2docs.formatters.markdown`

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/markdown.py`

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
