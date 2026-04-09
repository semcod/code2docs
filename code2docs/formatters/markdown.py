"""Markdown formatting utilities."""

from typing import List


class MarkdownFormatter:
    """Helper for constructing Markdown documents."""

    def __init__(self):
        self.lines: List[str] = []

    def heading(self, text: str, level: int = 1) -> "MarkdownFormatter":
        """Add a heading."""
        self.lines.append(f"{'#' * level} {text}\n")
        return self

    def paragraph(self, text: str) -> "MarkdownFormatter":
        """Add a paragraph."""
        self.lines.append(f"{text}\n")
        return self

    def blockquote(self, text: str) -> "MarkdownFormatter":
        """Add a blockquote."""
        self.lines.append(f"> {text}\n")
        return self

    def code_block(self, code: str, language: str = "") -> "MarkdownFormatter":
        """Add a fenced code block."""
        self.lines.append(f"```{language}")
        self.lines.append(code)
        self.lines.append("```\n")
        return self

    def inline_code(self, text: str) -> str:
        """Return inline code string."""
        return f"`{text}`"

    def bold(self, text: str) -> str:
        """Return bold string."""
        return f"**{text}**"

    def link(self, text: str, url: str) -> str:
        """Return a Markdown link."""
        return f"[{text}]({url})"

    def list_item(self, text: str, indent: int = 0) -> "MarkdownFormatter":
        """Add a list item."""
        prefix = "  " * indent
        self.lines.append(f"{prefix}- {text}")
        return self

    def table(self, headers: List[str], rows: List[List[str]]) -> "MarkdownFormatter":
        """Add a Markdown table."""
        self.lines.append("| " + " | ".join(headers) + " |")
        self.lines.append("| " + " | ".join("---" for _ in headers) + " |")
        for row in rows:
            self.lines.append("| " + " | ".join(str(c) for c in row) + " |")
        self.lines.append("")
        return self

    def separator(self) -> "MarkdownFormatter":
        """Add a horizontal rule."""
        self.lines.append("---\n")
        return self

    def blank(self) -> "MarkdownFormatter":
        """Add a blank line."""
        self.lines.append("")
        return self

    def render(self) -> str:
        """Render accumulated Markdown to string."""
        return "\n".join(self.lines)
