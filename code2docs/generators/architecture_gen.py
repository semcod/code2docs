"""Architecture documentation generator with Mermaid diagrams."""

from pathlib import Path
from typing import Dict, List, Set

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..llm_helper import LLMHelper


class ArchitectureGenerator:
    """Generate docs/architecture.md — architecture overview with diagrams."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self.llm = LLMHelper(config.llm)

    def generate(self) -> str:
        """Generate architecture documentation."""
        project_name = self.config.project_name or Path(self.result.project_path).name

        lines = [
            f"# {project_name} — Architecture\n",
            f"> {len(self.result.modules)} modules | "
            f"{len(self.result.functions)} functions | "
            f"{len(self.result.classes)} classes\n",
        ]

        # Data flow / pipeline overview (LLM-enhanced if available)
        lines.append(self._generate_pipeline_overview(project_name))
        llm_summary = self._generate_llm_summary(project_name)
        if llm_summary:
            lines.append("")
            lines.append(llm_summary)
        lines.append("")

        # Layered architecture with descriptions
        layers = self._detect_layers()
        if layers:
            lines.append("## Architecture Layers\n")
            lines.append(self._generate_layer_diagram(layers))
            lines.append("")
            for layer_name, modules in layers.items():
                lines.append(f"### {layer_name}\n")
                for mod in modules:
                    mod_info = self.result.modules.get(mod)
                    doc = ""
                    mod_doc = getattr(mod_info, "docstring", None) if mod_info else None
                    if mod_doc:
                        doc = f" — {mod_doc.splitlines()[0]}"
                    lines.append(f"- `{mod}`{doc}")
                lines.append("")

        # Module dependency graph
        lines.append("## Module Dependency Graph\n")
        lines.append(self._generate_module_graph())
        lines.append("")

        # Key classes (top 10 by method count)
        lines.append("## Key Classes\n")
        lines.append(self._generate_class_diagram())
        lines.append("")

        # Patterns detected
        if self.result.patterns:
            lines.append("## Detected Patterns\n")
            for pattern in self.result.patterns:
                lines.append(
                    f"- **{pattern.name}** ({pattern.type}) — "
                    f"confidence: {pattern.confidence:.0%}, "
                    f"functions: {', '.join(f'`{f}`' for f in pattern.functions[:5])}"
                )
            lines.append("")

        # Public entry points only (filter out dunders and class methods)
        public_eps = self._get_public_entry_points()
        if public_eps:
            lines.append("## Public Entry Points\n")
            for ep, doc in public_eps:
                lines.append(f"- `{ep}`{doc}")
            lines.append("")

        # Metrics summary
        lines.append("## Metrics Summary\n")
        lines.append(self._generate_metrics_table())

        return "\n".join(lines)

    def _generate_pipeline_overview(self, project_name: str) -> str:
        """Generate a data-flow pipeline overview."""
        lines = [
            "## How It Works\n",
            f"`{project_name}` analyzes source code via a multi-stage pipeline:\n",
            "```",
            "Source files  ──►  code2llm (tree-sitter + AST)  ──►  AnalysisResult",
            "                                                          │",
            "              ┌───────────────────────────────────────────┘",
            "              ▼",
            "    ┌─────────────────────┐",
            "    │   12 Generators     │",
            "    │  ─────────────────  │",
            "    │  README.md          │",
            "    │  docs/api/          │",
            "    │  docs/modules/      │",
            "    │  docs/architecture   │",
            "    │  docs/coverage      │",
            "    │  examples/          │",
            "    │  mkdocs.yml         │",
            "    │  CONTRIBUTING.md    │",
            "    └─────────────────────┘",
            "```\n",
            "**Analysis algorithms:**\n",
            "1. **AST parsing** — language-specific parsers (tree-sitter) extract syntax trees",
            "2. **Cyclomatic complexity** — counts independent code paths per function",
            "3. **Fan-in / fan-out** — measures module coupling (how many modules import/are imported by each)",
            "4. **Docstring extraction** — parses Google/NumPy/Sphinx-style docstrings into structured data",
            "5. **Pattern detection** — identifies design patterns (Factory, Singleton, Observer, etc.)",
            "6. **Dependency scanning** — reads pyproject.toml / requirements.txt / setup.py",
        ]
        return "\n".join(lines)

    @staticmethod
    def _generate_layer_diagram(layers: Dict[str, List[str]]) -> str:
        """Generate Mermaid layer diagram."""
        lines = ["```mermaid", "graph TD"]
        for i, (layer, modules) in enumerate(layers.items()):
            safe_id = layer.replace(" ", "_").replace("/", "_")
            count = len(modules)
            lines.append(f"    {safe_id}[\"{layer}<br/>{count} modules\"]")
        # Connect layers top-down
        layer_ids = [l.replace(" ", "_").replace("/", "_") for l in layers]
        for i in range(len(layer_ids) - 1):
            lines.append(f"    {layer_ids[i]} --> {layer_ids[i+1]}")
        lines.append("```")
        return "\n".join(lines)

    def _get_public_entry_points(self) -> List[tuple]:
        """Get filtered public entry points with descriptions."""
        results = []
        for ep in (self.result.entry_points or []):
            parts = ep.split(".")
            # Skip dunders, private, and class methods
            if any(seg.startswith("_") or (seg[0].isupper() if seg else False) for seg in parts):
                continue
            func = self.result.functions.get(ep)
            doc = ""
            if func and func.docstring:
                doc = f" — {func.docstring.splitlines()[0]}"
            results.append((ep, doc))
        return results

    def _generate_llm_summary(self, project_name: str) -> str:
        """Generate LLM-enhanced architecture summary. Returns '' if unavailable."""
        if not self.llm.available:
            return ""
        layers = self._detect_layers()
        layers_str = "\n".join(
            f"- {name}: {len(mods)} modules" for name, mods in layers.items()
        )
        patterns_str = "\n".join(
            f"- {p.name} ({p.type}, confidence={p.confidence:.0%})"
            for p in self.result.patterns
        ) or "None detected"
        stats = self.result.stats or {}
        metrics_str = (
            f"Modules: {len(self.result.modules)}, "
            f"Functions: {len(self.result.functions)}, "
            f"Classes: {len(self.result.classes)}, "
            f"Patterns: {len(self.result.patterns)}"
        )
        result = self.llm.generate_architecture_summary(
            project_name, layers_str, patterns_str, metrics_str
        )
        if result:
            return f"### Architecture Overview\n\n{result}"
        return ""

    def _generate_module_graph(self) -> str:
        """Generate Mermaid module dependency graph."""
        lines = ["```mermaid", "graph LR"]

        # Build dependency edges from module imports
        edges: Set[tuple] = set()
        for mod_name, mod_info in self.result.modules.items():
            short_name = mod_name.split(".")[-1]
            for imp in mod_info.imports:
                # Only show internal dependencies
                imp_module = imp.split(".")[0] if "." in imp else imp
                for other_mod in self.result.modules:
                    other_short = other_mod.split(".")[-1]
                    if imp_module in other_mod and mod_name != other_mod:
                        edges.add((short_name, other_short))

        for src, tgt in sorted(edges):
            lines.append(f"    {src} --> {tgt}")

        if not edges:
            lines.append("    note[No internal dependencies detected]")

        lines.append("```")
        return "\n".join(lines)

    def _generate_class_diagram(self) -> str:
        """Generate Mermaid class diagram for key classes."""
        lines = ["```mermaid", "classDiagram"]

        # Show top classes by method count
        top_classes = sorted(
            self.result.classes.values(),
            key=lambda c: len(c.methods),
            reverse=True,
        )[:15]

        for cls in top_classes:
            lines.append(f"    class {cls.name} {{")
            methods = cls.methods[:8]
            for method_name in methods:
                func = self.result.functions.get(
                    f"{cls.qualified_name}.{method_name}"
                ) or self.result.functions.get(method_name)
                if func:
                    args = ", ".join(func.args[:3])
                    ret = func.returns or "None"
                    prefix = "-" if func.is_private else "+"
                    lines.append(f"        {prefix}{func.name}({args}) {ret}")
                else:
                    lines.append(f"        +{method_name}()")
            if len(cls.methods) > 8:
                lines.append(f"        ... +{len(cls.methods) - 8} more")
            lines.append("    }")

            # Inheritance
            for base in cls.bases:
                if base in [c.name for c in top_classes]:
                    lines.append(f"    {base} <|-- {cls.name}")

        lines.append("```")
        return "\n".join(lines)

    def _detect_layers(self) -> Dict[str, List[str]]:
        """Detect architectural layers from module names."""
        layers: Dict[str, List[str]] = {}
        layer_keywords = {
            "Core": ["core", "base", "common", "utils", "lib"],
            "API / CLI": ["cli", "api", "rest", "routes", "views", "endpoints"],
            "Analysis": ["analysis", "analyzer", "parser", "scanner", "detector"],
            "Export / Output": ["export", "output", "format", "render", "template"],
            "Config": ["config", "settings", "constants"],
            "Tests": ["test", "tests", "spec"],
        }

        for mod_name in sorted(self.result.modules.keys()):
            lower = mod_name.lower()
            assigned = False
            for layer, keywords in layer_keywords.items():
                if any(kw in lower for kw in keywords):
                    layers.setdefault(layer, []).append(mod_name)
                    assigned = True
                    break
            if not assigned:
                layers.setdefault("Other", []).append(mod_name)

        return {k: v for k, v in layers.items() if v}

    def _generate_metrics_table(self) -> str:
        """Generate metrics summary table."""
        stats = self.result.stats or {}
        lines = [
            "| Metric | Value |",
            "|--------|-------|",
            f"| Modules | {len(self.result.modules)} |",
            f"| Functions | {len(self.result.functions)} |",
            f"| Classes | {len(self.result.classes)} |",
            f"| CFG Nodes | {stats.get('nodes_created', len(self.result.nodes))} |",
            f"| Patterns | {len(self.result.patterns)} |",
        ]

        # Average complexity
        complexities = [
            f.complexity.get("cyclomatic_complexity", f.complexity.get("cyclomatic", 0))
            for f in self.result.functions.values()
            if f.complexity.get("cyclomatic_complexity", f.complexity.get("cyclomatic", 0)) > 0
        ]
        if complexities:
            avg = round(sum(complexities) / len(complexities), 1)
            lines.append(f"| Avg Complexity | {avg} |")

        if stats.get("analysis_time_seconds"):
            lines.append(f"| Analysis Time | {stats['analysis_time_seconds']}s |")

        lines.append("")
        return "\n".join(lines)
