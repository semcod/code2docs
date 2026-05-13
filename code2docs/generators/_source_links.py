"""Helper for generating source code links in documentation."""

from pathlib import Path
from typing import Optional

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


class SourceLinker:
    """Build source-code links (relative paths + optional GitHub/GitLab URLs)."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self._repo_url = config.repo_url.rstrip("/") if config.repo_url else ""
        self._project_root = Path(result.project_path).resolve()
        # Detect git root (may be parent of project_path)
        self._git_root = self._find_git_root(self._project_root)
        self._branch = self._detect_branch()

    def source_link(self, file: str, line: Optional[int] = None) -> str:
        """Return a Markdown link to source, or empty string if unavailable."""
        rel = self._relative_path(file)
        if not rel:
            return ""

        if self._repo_url:
            url = f"{self._repo_url}/blob/{self._branch}/{rel}"
            if line:
                url += f"#L{line}"
            return f"[source]({url})"

        # Fallback: plain relative path (works in local MkDocs/GitHub rendering)
        anchor = f"#L{line}" if line else ""
        return f"[source]({rel}{anchor})"

    def file_link(self, file: str) -> str:
        """Return a Markdown link to a file (no line number)."""
        return self.source_link(file)

    def _relative_path(self, file: str) -> Optional[str]:
        """Convert absolute file path to relative (from git root or project root)."""
        try:
            abs_path = Path(file).resolve()
            # Try relative to git root first (for correct GitHub URLs)
            if self._git_root:
                return str(abs_path.relative_to(self._git_root))
            return str(abs_path.relative_to(self._project_root))
        except ValueError:
            return None

    @staticmethod
    def _find_git_root(start: Path) -> Optional[Path]:
        """Walk up to find .git directory."""
        current = start
        for _ in range(10):
            if (current / ".git").exists():
                return current
            parent = current.parent
            if parent == current:
                break
            current = parent
        return None

    @staticmethod
    def _detect_branch() -> str:
        """Detect current git branch, default to 'main'."""
        import subprocess

        try:
            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
            return branch or "main"
        except (subprocess.CalledProcessError, FileNotFoundError):
            return "main"
