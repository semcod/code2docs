"""Validate generated markdown: checks local links/images, table shape, duplicate headings."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Optional
from urllib.parse import urlparse

_LINK_RE = re.compile(r'!?\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
_FENCE_RE = re.compile(r"^(```|~~~)")
_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")


@dataclass
class MarkdownIssue:
    """A single validation issue in a markdown file."""

    file: str
    line: int
    kind: str
    message: str

    def __str__(self) -> str:
        return f"{self.file}:{self.line} [{self.kind}] {self.message}"


@dataclass
class ValidationReport:
    """Aggregate result of markdown validation."""

    issues: List[MarkdownIssue] = field(default_factory=list)
    files_checked: int = 0

    @property
    def ok(self) -> bool:
        return not self.issues

    def by_kind(self, kind: str) -> List[MarkdownIssue]:
        return [i for i in self.issues if i.kind == kind]

    def summary(self) -> str:
        if self.ok:
            return f"✅ {self.files_checked} file(s) checked, no issues"
        kinds: dict = {}
        for issue in self.issues:
            kinds[issue.kind] = kinds.get(issue.kind, 0) + 1
        parts = ", ".join(f"{k}={v}" for k, v in sorted(kinds.items()))
        return f"❌ {len(self.issues)} issue(s) across {self.files_checked} file(s): {parts}"


def validate_markdown_file(
    md_path: Path, project_root: Optional[Path] = None
) -> List[MarkdownIssue]:
    """Validate a single markdown file.

    Checks:
    - Local links/images resolve to existing files (skips URLs and in-page anchors).
    - Tables have consistent column count.
    - Duplicate headings at the same level are flagged.
    """
    md_path = Path(md_path)
    if not md_path.exists():
        return [MarkdownIssue(str(md_path), 0, "missing", "file does not exist")]
    root = Path(project_root) if project_root else md_path.parent
    try:
        lines = md_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return [MarkdownIssue(str(md_path), 0, "read_error", str(exc))]
    issues: List[MarkdownIssue] = []
    issues.extend(_check_links(md_path, root, lines))
    issues.extend(_check_tables(md_path, lines))
    issues.extend(_check_headings(md_path, lines))
    return issues


def validate_markdown_tree(
    root: Path,
    patterns: Iterable[str] = ("*.md",),
    ignore: Iterable[str] = ("node_modules", "venv", ".venv", "vendor", ".git", "__pycache__"),
) -> ValidationReport:
    """Validate every markdown file under ``root`` matching ``patterns``."""
    root = Path(root)
    ignore_set = set(ignore)
    report = ValidationReport()
    seen: set = set()
    for pattern in patterns:
        for md_file in root.rglob(pattern):
            if any(part in ignore_set for part in md_file.parts):
                continue
            if md_file in seen:
                continue
            seen.add(md_file)
            report.files_checked += 1
            report.issues.extend(validate_markdown_file(md_file, project_root=root))
    return report


def _strip_code_fences(lines: List[str]) -> List[bool]:
    """Return a per-line boolean: True if the line is inside a fenced code block."""
    inside = False
    mask: List[bool] = []
    for line in lines:
        if _FENCE_RE.match(line.strip()):
            mask.append(True)
            inside = not inside
            continue
        mask.append(inside)
    return mask


def _check_links(md_path: Path, root: Path, lines: List[str]) -> List[MarkdownIssue]:
    issues: List[MarkdownIssue] = []
    in_code = _strip_code_fences(lines)
    for lineno, line in enumerate(lines, 1):
        if in_code[lineno - 1]:
            continue
        for match in _LINK_RE.finditer(line):
            target = match.group(2).strip()
            if not target or target.startswith("#"):
                continue
            parsed = urlparse(target)
            if parsed.scheme in ("http", "https", "mailto", "ftp", "tel", "data"):
                continue
            if parsed.scheme and parsed.scheme not in ("file",):
                continue
            rel = parsed.path
            if not rel:
                continue
            if rel.startswith("/"):
                resolved = root / rel.lstrip("/")
            else:
                resolved = (md_path.parent / rel).resolve()
            if not resolved.exists():
                issues.append(
                    MarkdownIssue(
                        str(md_path), lineno, "broken_link", f"link target not found: {target}"
                    )
                )
    return issues


def _check_tables(md_path: Path, lines: List[str]) -> List[MarkdownIssue]:
    issues: List[MarkdownIssue] = []
    in_code = _strip_code_fences(lines)
    i = 0
    while i < len(lines):
        if in_code[i]:
            i += 1
            continue
        line = lines[i]
        if "|" in line and i + 1 < len(lines) and _TABLE_SEP_RE.match(lines[i + 1]):
            header_cols = _count_cells(line)
            sep_cols = _count_cells(lines[i + 1])
            if header_cols != sep_cols:
                issues.append(
                    MarkdownIssue(
                        str(md_path),
                        i + 2,
                        "table_shape",
                        f"separator has {sep_cols} cells, header has {header_cols}",
                    )
                )
            j = i + 2
            while j < len(lines) and not in_code[j] and lines[j].strip() and "|" in lines[j]:
                cells = _count_cells(lines[j])
                if cells != header_cols:
                    issues.append(
                        MarkdownIssue(
                            str(md_path),
                            j + 1,
                            "table_shape",
                            f"row has {cells} cells, expected {header_cols}",
                        )
                    )
                j += 1
            i = j
        else:
            i += 1
    return issues


def _count_cells(row: str) -> int:
    stripped = row.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return len(stripped.split("|"))


def _check_headings(md_path: Path, lines: List[str]) -> List[MarkdownIssue]:
    issues: List[MarkdownIssue] = []
    in_code = _strip_code_fences(lines)
    seen: dict = {}
    for lineno, line in enumerate(lines, 1):
        if in_code[lineno - 1]:
            continue
        match = _HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip().lower()
        key = (level, title)
        if key in seen:
            issues.append(
                MarkdownIssue(
                    str(md_path),
                    lineno,
                    "duplicate_heading",
                    f'H{level} "{match.group(2).strip()}" already at line {seen[key]}',
                )
            )
        else:
            seen[key] = lineno
    return issues
