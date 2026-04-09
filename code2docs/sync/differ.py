"""Detect changes in source code for selective documentation regeneration."""

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from ..config import Code2DocsConfig

STATE_FILE = ".code2docs.state"


@dataclass
class ChangeInfo:
    """Describes a detected change."""
    module: str
    file: str
    change_type: str  # added, modified, deleted
    old_hash: str = ""
    new_hash: str = ""

    def __str__(self) -> str:
        return f"[{self.change_type}] {self.module} ({self.file})"


class Differ:
    """Detect changes between current source and previous state."""

    def __init__(self, config: Optional[Code2DocsConfig] = None):
        self.config = config or Code2DocsConfig()

    def detect_changes(self, project_path: str) -> List[ChangeInfo]:
        """Compare current file hashes with saved state. Return list of changes."""
        project = Path(project_path).resolve()
        state_path = project / STATE_FILE

        old_state = self._load_state(state_path)
        new_state = self._compute_state(project)

        changes: List[ChangeInfo] = []

        # Detect modified and added
        for filepath, new_hash in new_state.items():
            old_hash = old_state.get(filepath, "")
            if not old_hash:
                changes.append(ChangeInfo(
                    module=self._file_to_module(filepath, project),
                    file=filepath,
                    change_type="added",
                    new_hash=new_hash,
                ))
            elif old_hash != new_hash:
                changes.append(ChangeInfo(
                    module=self._file_to_module(filepath, project),
                    file=filepath,
                    change_type="modified",
                    old_hash=old_hash,
                    new_hash=new_hash,
                ))

        # Detect deleted
        for filepath, old_hash in old_state.items():
            if filepath not in new_state:
                changes.append(ChangeInfo(
                    module=self._file_to_module(filepath, project),
                    file=filepath,
                    change_type="deleted",
                    old_hash=old_hash,
                ))

        return changes

    def save_state(self, project_path: str) -> None:
        """Save current file hashes as state."""
        project = Path(project_path).resolve()
        state = self._compute_state(project)
        state_path = project / STATE_FILE
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    def _load_state(self, state_path: Path) -> Dict[str, str]:
        """Load previous state from file."""
        if not state_path.exists():
            return {}
        try:
            return json.loads(state_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}

    def _compute_state(self, project: Path) -> Dict[str, str]:
        """Compute file hashes for all Python files in the project."""
        state: Dict[str, str] = {}
        ignore_patterns = self.config.sync.ignore if self.config else []

        for py_file in project.rglob("*.py"):
            rel = str(py_file.relative_to(project))

            # Check ignore patterns
            if any(pattern.rstrip("/") in rel for pattern in ignore_patterns):
                continue

            try:
                content = py_file.read_bytes()
                file_hash = hashlib.sha256(content).hexdigest()[:16]
                state[rel] = file_hash
            except OSError:
                continue

        return state

    @staticmethod
    def _file_to_module(filepath: str, project: Path) -> str:
        """Convert file path to module name."""
        p = Path(filepath)
        if p.is_absolute():
            try:
                p = p.relative_to(project)
            except ValueError:
                pass
        parts = list(p.parts)
        if parts and parts[-1] == "__init__.py":
            parts = parts[:-1]
        elif parts:
            parts[-1] = parts[-1].replace(".py", "")
        return ".".join(parts)
