"""API changelog generator — diff function/class signatures between versions."""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig

SNAPSHOT_FILE = ".code2docs.api_snapshot.json"


@dataclass
class ApiChange:
    """A single API change between two analysis snapshots."""
    kind: str          # added, removed, changed
    item_type: str     # function, class, method
    name: str
    old_signature: str = ""
    new_signature: str = ""
    detail: str = ""

    @property
    def emoji(self) -> str:
        return {"added": "🆕", "removed": "🗑️", "changed": "✏️"}.get(self.kind, "•")


class ApiChangelogGenerator:
    """Generate API changelog by diffing current analysis with a saved snapshot."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self, project_path: str) -> str:
        """Generate api-changelog.md by comparing with previous snapshot."""
        project = Path(project_path).resolve()
        snapshot_path = project / SNAPSHOT_FILE

        old_snapshot = self._load_snapshot(snapshot_path)
        new_snapshot = self._build_snapshot()
        changes = self._diff(old_snapshot, new_snapshot)

        project_name = self.config.project_name or project.name
        return self._render(project_name, changes, old_snapshot is not None)

    def save_snapshot(self, project_path: str) -> None:
        """Save current API state as snapshot for future diffs."""
        project = Path(project_path).resolve()
        snapshot = self._build_snapshot()
        path = project / SNAPSHOT_FILE
        path.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")

    def _build_snapshot(self) -> Dict:
        """Build a JSON-serializable snapshot of current API."""
        functions = {}
        for name, func in self.result.functions.items():
            if func.is_private:
                continue
            sig = f"{func.name}({', '.join(func.args)})"
            if func.returns:
                sig += f" → {func.returns}"
            functions[name] = {
                "signature": sig,
                "is_method": func.is_method,
                "module": func.module,
                "docstring_hash": str(hash(func.docstring or ""))[:8],
            }

        classes = {}
        for name, cls in self.result.classes.items():
            classes[name] = {
                "bases": cls.bases,
                "methods": sorted(cls.methods),
                "module": cls.module,
            }

        return {"functions": functions, "classes": classes}

    @staticmethod
    def _load_snapshot(path: Path) -> Optional[Dict]:
        """Load previous snapshot, or None if not found."""
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return None

    def _diff(self, old: Optional[Dict], new: Dict) -> List[ApiChange]:
        """Compute list of API changes between old and new snapshots."""
        if old is None:
            return []

        changes: List[ApiChange] = []
        self._diff_functions(old.get("functions", {}), new.get("functions", {}), changes)
        self._diff_classes(old.get("classes", {}), new.get("classes", {}), changes)
        return sorted(changes, key=lambda c: (c.kind, c.name))

    @staticmethod
    def _diff_functions(old: Dict, new: Dict, changes: List[ApiChange]) -> None:
        """Diff function signatures."""
        all_names = set(old.keys()) | set(new.keys())
        for name in all_names:
            old_fn = old.get(name)
            new_fn = new.get(name)
            item_type = "method" if (new_fn or old_fn or {}).get("is_method") else "function"

            if old_fn and not new_fn:
                changes.append(ApiChange(
                    kind="removed", item_type=item_type, name=name,
                    old_signature=old_fn["signature"],
                ))
            elif new_fn and not old_fn:
                changes.append(ApiChange(
                    kind="added", item_type=item_type, name=name,
                    new_signature=new_fn["signature"],
                ))
            elif old_fn["signature"] != new_fn["signature"]:
                changes.append(ApiChange(
                    kind="changed", item_type=item_type, name=name,
                    old_signature=old_fn["signature"],
                    new_signature=new_fn["signature"],
                    detail="signature changed",
                ))

    @staticmethod
    def _diff_classes(old: Dict, new: Dict, changes: List[ApiChange]) -> None:
        """Diff class definitions."""
        all_names = set(old.keys()) | set(new.keys())
        for name in all_names:
            old_cls = old.get(name)
            new_cls = new.get(name)

            if old_cls and not new_cls:
                changes.append(ApiChange(
                    kind="removed", item_type="class", name=name,
                ))
            elif new_cls and not old_cls:
                changes.append(ApiChange(
                    kind="added", item_type="class", name=name,
                ))
            else:
                diffs = []
                if set(old_cls.get("bases", [])) != set(new_cls.get("bases", [])):
                    diffs.append("bases changed")
                old_methods = set(old_cls.get("methods", []))
                new_methods = set(new_cls.get("methods", []))
                added = new_methods - old_methods
                removed = old_methods - new_methods
                if added:
                    diffs.append(f"added methods: {', '.join(sorted(added))}")
                if removed:
                    diffs.append(f"removed methods: {', '.join(sorted(removed))}")
                if diffs:
                    changes.append(ApiChange(
                        kind="changed", item_type="class", name=name,
                        detail="; ".join(diffs),
                    ))

    @staticmethod
    def _render(project_name: str, changes: List[ApiChange], has_baseline: bool) -> str:
        """Render changelog as Markdown."""
        lines = [f"# {project_name} — API Changelog\n"]

        if not has_baseline:
            lines.append(
                "> No previous API snapshot found. Run `code2docs generate` to create a baseline.\n"
                "> Future runs will show changes here.\n"
            )
            return "\n".join(lines)

        if not changes:
            lines.append("✅ **No API changes detected since last snapshot.**\n")
            return "\n".join(lines)

        lines.append(f"> {len(changes)} change(s) detected\n")

        # Group by kind
        for kind_label, kind_key in [("Added", "added"), ("Changed", "changed"), ("Removed", "removed")]:
            group = [c for c in changes if c.kind == kind_key]
            if not group:
                continue
            lines.append(f"## {kind_label}\n")
            for c in group:
                sig = c.new_signature or c.old_signature or c.name
                lines.append(f"- {c.emoji} **{c.item_type}** `{sig}`")
                if c.detail:
                    lines.append(f"  - {c.detail}")
                if c.kind == "changed" and c.old_signature and c.new_signature:
                    lines.append(f"  - was: `{c.old_signature}`")
            lines.append("")

        return "\n".join(lines)
