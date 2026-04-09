"""Changelog generator from git log and API diff."""

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


@dataclass
class ChangelogEntry:
    """A single changelog entry."""
    date: str
    hash: str
    author: str
    message: str
    type: str = "other"  # feat, fix, refactor, docs, test, chore, other


class ChangelogGenerator:
    """Generate CHANGELOG.md from git log and analysis diff."""

    CONVENTIONAL_TYPES = {
        "feat": "Features",
        "fix": "Bug Fixes",
        "refactor": "Refactoring",
        "docs": "Documentation",
        "test": "Tests",
        "perf": "Performance",
        "chore": "Chores",
        "ci": "CI/CD",
        "style": "Style",
        "build": "Build",
    }

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self, project_path: Optional[str] = None, max_entries: int = 100) -> str:
        """Generate changelog content from git log."""
        project = Path(project_path or self.result.project_path)

        entries = self._get_git_log(project, max_entries)
        if not entries:
            return "# Changelog\n\nNo git history available.\n"

        grouped = self._group_by_type(entries)
        return self._render(grouped)

    def _get_git_log(self, project_path: Path, max_entries: int) -> List[ChangelogEntry]:
        """Extract git log entries."""
        try:
            result = subprocess.run(
                ["git", "log", f"--max-count={max_entries}",
                 "--format=%H|%ad|%an|%s", "--date=short"],
                cwd=str(project_path),
                capture_output=True, text=True, timeout=10,
            )
            if result.returncode != 0:
                return []
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return []

        entries = []
        for line in result.stdout.strip().splitlines():
            parts = line.split("|", 3)
            if len(parts) == 4:
                entry = ChangelogEntry(
                    hash=parts[0][:8],
                    date=parts[1],
                    author=parts[2],
                    message=parts[3],
                    type=self._classify_message(parts[3]),
                )
                entries.append(entry)

        return entries

    def _classify_message(self, message: str) -> str:
        """Classify commit message by conventional commit type."""
        lower = message.lower()
        for prefix in self.CONVENTIONAL_TYPES:
            if lower.startswith(f"{prefix}:") or lower.startswith(f"{prefix}("):
                return prefix
        return "other"

    def _group_by_type(self, entries: List[ChangelogEntry]) -> Dict[str, List[ChangelogEntry]]:
        """Group entries by type."""
        grouped: Dict[str, List[ChangelogEntry]] = {}
        for entry in entries:
            grouped.setdefault(entry.type, []).append(entry)
        return grouped

    def _render(self, grouped: Dict[str, List[ChangelogEntry]]) -> str:
        """Render grouped changelog to Markdown."""
        lines = ["# Changelog\n"]

        # Show by type
        for type_key, type_label in self.CONVENTIONAL_TYPES.items():
            entries = grouped.get(type_key, [])
            if entries:
                lines.append(f"## {type_label}\n")
                for entry in entries:
                    lines.append(
                        f"- {entry.message} (`{entry.hash}` — {entry.date})"
                    )
                lines.append("")

        # Other
        other = grouped.get("other", [])
        if other:
            lines.append("## Other\n")
            for entry in other:
                lines.append(f"- {entry.message} (`{entry.hash}` — {entry.date})")
            lines.append("")

        return "\n".join(lines)
