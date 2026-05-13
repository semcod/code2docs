"""Table of contents generator from Markdown headings."""

import re
from typing import List, Tuple


def generate_toc(markdown_content: str, max_depth: int = 3) -> str:
    """Generate a table of contents from Markdown headings.

    Args:
        markdown_content: Full Markdown document.
        max_depth: Maximum heading level to include (1-6).

    Returns:
        TOC as Markdown string.
    """
    headings = extract_headings(markdown_content, max_depth)
    if not headings:
        return ""

    lines = ["## Table of Contents\n"]
    for level, text, anchor in headings:
        indent = "  " * (level - 1)
        lines.append(f"{indent}- [{text}](#{anchor})")

    lines.append("")
    return "\n".join(lines)


def extract_headings(content: str, max_depth: int = 3) -> List[Tuple[int, str, str]]:
    """Extract headings from Markdown content.

    Returns list of (level, text, anchor) tuples.
    """
    headings: List[Tuple[int, str, str]] = []
    in_code_block = False

    for line in content.splitlines():
        # Skip code blocks
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if match:
            level = len(match.group(1))
            if level <= max_depth:
                text = match.group(2).strip()
                anchor = _slugify(text)
                headings.append((level, text, anchor))

    return headings


def _slugify(text: str) -> str:
    """Convert heading text to GitHub-compatible anchor slug."""
    slug = text.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug
