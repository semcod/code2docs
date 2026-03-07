"""Docstring coverage report generator."""

from typing import Dict, List

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..analyzers.docstring_extractor import DocstringExtractor


class CoverageGenerator:
    """Generate docs/coverage.md — docstring coverage report."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self._extractor = DocstringExtractor()

    def generate(self) -> str:
        """Generate coverage.md content."""
        project_name = self.config.project_name or "Project"
        report = self._extractor.coverage_report(self.result)

        lines = [
            f"# {project_name} — Docstring Coverage\n",
            self._render_summary(report),
            "",
            "## Per-Module Breakdown\n",
            self._render_per_module(),
            "",
            "## Undocumented Items\n",
            self._render_undocumented(),
            "",
        ]
        return "\n".join(lines)

    @staticmethod
    def _render_summary(report: Dict[str, float]) -> str:
        """Render overall coverage summary."""
        overall = report.get("overall_coverage", 0)
        badge = "🟢" if overall >= 80 else "🟡" if overall >= 50 else "🔴"
        lines = [
            f"{badge} **Overall coverage: {overall:.1f}%**\n",
            "| Category | Documented | Total | Coverage |",
            "|----------|-----------|-------|----------|",
            f"| Functions | {report['functions_documented']} | {report['functions_total']} | {report['functions_coverage']:.1f}% |",
            f"| Classes | {report['classes_documented']} | {report['classes_total']} | {report['classes_coverage']:.1f}% |",
        ]
        return "\n".join(lines)

    def _render_per_module(self) -> str:
        """Render per-module coverage table (orchestrator)."""
        stats = self._collect_module_stats()
        return self._format_coverage_table(stats)

    def _collect_module_stats(self) -> List[Dict]:
        """Collect coverage data per module."""
        rows = []
        for mod_name in sorted(self.result.modules.keys()):
            funcs = [f for f in self.result.functions.values()
                     if f.module == mod_name and not f.is_method]
            classes = [c for c in self.result.classes.values()
                       if c.module == mod_name]
            total = len(funcs) + len(classes)
            doc_funcs = sum(1 for f in funcs if f.docstring)
            doc_classes = sum(1 for c in classes if c.docstring)
            documented = doc_funcs + doc_classes
            pct = (documented / total * 100) if total else 100.0
            rows.append({
                "module": mod_name,
                "doc_funcs": doc_funcs, "total_funcs": len(funcs),
                "doc_classes": doc_classes, "total_classes": len(classes),
                "pct": pct,
            })
        return rows

    @staticmethod
    def _format_coverage_table(stats: List[Dict]) -> str:
        """Format coverage stats as a Markdown table."""
        lines = [
            "| Module | Functions | Classes | Coverage |",
            "|--------|-----------|---------|----------|",
        ]
        for row in stats:
            badge = "🟢" if row["pct"] >= 80 else "🟡" if row["pct"] >= 50 else "🔴"
            lines.append(
                f"| `{row['module']}` | {row['doc_funcs']}/{row['total_funcs']} "
                f"| {row['doc_classes']}/{row['total_classes']} "
                f"| {badge} {row['pct']:.0f}% |"
            )
        return "\n".join(lines)

    def _render_undocumented(self) -> str:
        """List all undocumented public functions and classes."""
        items: List[str] = []
        for name, func in sorted(self.result.functions.items()):
            if not func.docstring and not func.is_private and not func.is_method:
                items.append(f"- `{name}` ({func.file}:{func.line})")
        for name, cls in sorted(self.result.classes.items()):
            if not cls.docstring:
                items.append(f"- `{name}` ({cls.file}:{cls.line})")
        if not items:
            return "_All public items are documented._ ✅"
        return "\n".join(items)
