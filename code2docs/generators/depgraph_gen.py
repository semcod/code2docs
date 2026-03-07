"""Dependency graph generator — Mermaid diagram from coupling matrix."""

import ast
from pathlib import Path
from typing import Dict, List, Set, Tuple

from code2llm.api import AnalysisResult, ModuleInfo

from ..config import Code2DocsConfig


class DepGraphGenerator:
    """Generate docs/dependency-graph.md with Mermaid diagrams."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self) -> str:
        """Generate dependency-graph.md content."""
        project_name = self.config.project_name or "Project"
        edges = self._collect_edges()
        in_degree, out_degree = self._calc_degrees(edges)

        lines = [
            f"# {project_name} — Dependency Graph\n",
            f"> {len(self.result.modules)} modules, "
            f"{len(edges)} dependency edges\n",
            "## Module Dependencies\n",
            self._render_mermaid(edges),
            "",
            "## Coupling Matrix\n",
            self._render_matrix(edges),
            "",
            "## Fan-in / Fan-out\n",
            self._render_degree_table(in_degree, out_degree),
            "",
        ]
        return "\n".join(lines)

    def _collect_edges(self) -> List[Tuple[str, str]]:
        """Build directed edges from module imports.

        Uses ModuleInfo.imports when available, otherwise extracts
        imports from the source file via AST.
        """
        edges: Set[Tuple[str, str]] = set()
        module_names = set(self.result.modules.keys())

        for mod_name, mod_info in self.result.modules.items():
            imports = mod_info.imports
            if not imports:
                imports = self._extract_imports_from_file(mod_info.file)
            for imp in imports:
                for other in module_names:
                    if mod_name != other and self._import_matches(imp, other):
                        edges.add((mod_name, other))
        return sorted(edges)

    @staticmethod
    def _extract_imports_from_file(file_path: str) -> List[str]:
        """Parse source file AST to extract import targets."""
        try:
            source = Path(file_path).read_text(encoding="utf-8")
            tree = ast.parse(source)
        except Exception:
            return []

        imports: List[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
        return imports

    @staticmethod
    def _import_matches(imp: str, module: str) -> bool:
        """Check if an import string refers to a known module."""
        return imp == module or imp.startswith(module + ".")

    def _render_mermaid(self, edges: List[Tuple[str, str]]) -> str:
        """Render Mermaid graph from edges."""
        lines = ["```mermaid", "graph LR"]
        for src, tgt in edges:
            s = src.split(".")[-1]
            t = tgt.split(".")[-1]
            lines.append(f"    {s} --> {t}")
        if not edges:
            lines.append("    note[No internal dependencies]")
        lines.append("```")
        return "\n".join(lines)

    def _render_matrix(self, edges: List[Tuple[str, str]]) -> str:
        """Render a coupling matrix as a Markdown table."""
        mods = sorted(self.result.modules.keys())
        if not mods:
            return "_No modules._"
        short = {m: m.split(".")[-1] for m in mods}
        edge_set = set(edges)

        header = "| | " + " | ".join(short[m] for m in mods) + " |"
        sep = "| --- | " + " | ".join("---" for _ in mods) + " |"
        rows = [header, sep]
        for src in mods:
            cells = []
            for tgt in mods:
                if src == tgt:
                    cells.append("·")
                elif (src, tgt) in edge_set:
                    cells.append("→")
                else:
                    cells.append("")
            rows.append(f"| **{short[src]}** | " + " | ".join(cells) + " |")
        return "\n".join(rows)

    @staticmethod
    def _calc_degrees(edges: List[Tuple[str, str]]) -> Tuple[Dict[str, int], Dict[str, int]]:
        """Calculate in-degree and out-degree per module."""
        in_deg: Dict[str, int] = {}
        out_deg: Dict[str, int] = {}
        for src, tgt in edges:
            out_deg[src] = out_deg.get(src, 0) + 1
            in_deg[tgt] = in_deg.get(tgt, 0) + 1
        return in_deg, out_deg

    def _render_degree_table(self, in_deg: Dict[str, int], out_deg: Dict[str, int]) -> str:
        """Render fan-in/fan-out table."""
        mods = sorted(self.result.modules.keys())
        lines = [
            "| Module | Fan-in | Fan-out |",
            "|--------|--------|---------|",
        ]
        for m in mods:
            fi = in_deg.get(m, 0)
            fo = out_deg.get(m, 0)
            lines.append(f"| `{m}` | {fi} | {fo} |")
        return "\n".join(lines)
