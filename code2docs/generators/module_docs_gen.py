"""Module documentation generator — single consolidated modules.md."""

import ast
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from code2llm.api import AnalysisResult, FunctionInfo, ClassInfo, ModuleInfo

from ..config import Code2DocsConfig
from ._source_links import SourceLinker


class ModuleDocsGenerator:
    """Generate docs/modules.md — consolidated module documentation."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self._linker = SourceLinker(config, result)

    def generate(self) -> str:
        """Generate a single modules.md with all modules grouped by package."""
        lines = self._build_header()
        lines.extend(self._build_overview_table())
        lines.extend(self._build_detail_sections())
        return "\n".join(lines)

    def _build_header(self) -> List[str]:
        """Build document header with project stats."""
        project = self.config.project_name or Path(self.result.project_path).name
        return [
            f"# {project} — Module Reference\n",
            f"> {len(self.result.modules)} modules | "
            f"{len(self.result.functions)} functions | "
            f"{len(self.result.classes)} classes\n",
        ]

    def _build_overview_table(self) -> List[str]:
        """Build overview table of all modules."""
        lines = [
            "## Module Overview\n",
            "| Module | Lines | Functions | Classes | CC avg | Description | Source |",
            "|--------|-------|-----------|---------|--------|-------------|--------|",
        ]
        for mod_name, mod_info in sorted(self.result.modules.items()):
            row = self._build_module_row(mod_name, mod_info)
            if row:
                lines.append(row)
        lines.append("")
        return lines

    def _build_module_row(self, mod_name: str, mod_info: ModuleInfo) -> str:
        """Build a single row for the overview table."""
        if mod_name.startswith("_"):
            return ""
        file_lines = self._count_file_lines(mod_info.file)
        func_count = self._count_module_functions(mod_name)
        class_count = self._count_module_classes(mod_name)
        if not func_count and not class_count:
            return ""
        avg_cc = self._calc_module_avg_cc(mod_name)
        cc_str = str(avg_cc) if avg_cc else "—"
        doc = self._get_module_docstring(mod_info)
        doc_short = doc.splitlines()[0][:60] if doc else "—"
        src = self._linker.file_link(mod_info.file)
        return (
            f"| `{mod_name}` | {file_lines} | {func_count} | "
            f"{class_count} | {cc_str} | {doc_short} | {src} |"
        )

    def _count_module_functions(self, mod_name: str) -> int:
        """Count public functions in a module."""
        return len([
            f for f in self.result.functions.values()
            if f.module == mod_name and not f.is_method
        ])

    def _count_module_classes(self, mod_name: str) -> int:
        """Count classes in a module."""
        return len([
            c for c in self.result.classes.values()
            if c.module == mod_name
        ])

    def _build_detail_sections(self) -> List[str]:
        """Build detailed sections for each module group."""
        lines = []
        groups = self._group_modules()
        for group_name, modules in groups.items():
            group_lines = self._build_group_section(group_name, modules)
            lines.extend(group_lines)
        return lines

    def _build_group_section(self, group_name: str, modules: List[str]) -> List[str]:
        """Build a single group section."""
        non_trivial = [
            (m, self.result.modules[m]) for m in modules
            if self._has_content(m)
        ]
        if not non_trivial:
            return []
        lines = [f"## {group_name}\n"]
        for mod_name, mod_info in non_trivial:
            lines.append(self._render_module_detail(mod_name, mod_info))
        return lines

    def _group_modules(self) -> Dict[str, List[str]]:
        """Group module names by top-level package."""
        groups: Dict[str, List[str]] = defaultdict(list)
        for mod_name in sorted(self.result.modules.keys()):
            parts = mod_name.split(".")
            if parts[0].startswith("_"):
                continue
            group = parts[0] if len(parts) > 1 else "Core"
            groups[group].append(mod_name)
        return dict(groups)

    def _has_content(self, mod_name: str) -> bool:
        """Check if module has public functions or classes."""
        return any(
            (not f.is_method and not f.name.startswith("_"))
            for f in self.result.functions.values()
            if f.module == mod_name
        ) or any(
            not c.name.startswith("_")
            for c in self.result.classes.values()
            if c.module == mod_name
        )

    def _render_module_detail(self, mod_name: str, mod_info: ModuleInfo) -> str:
        """Render a single module's detail section."""
        src = self._linker.file_link(mod_info.file)
        heading = f"### `{mod_name}` {src}" if src else f"### `{mod_name}`"
        lines = [f"{heading}\n"]

        doc = self._get_module_docstring(mod_info)
        if doc:
            lines.append(f"{doc.splitlines()[0]}\n")

        module_classes = self._get_module_classes(mod_name)
        if module_classes:
            lines.extend(self._render_classes_detail(module_classes))

        module_functions = self._get_module_functions(mod_name)
        if module_functions:
            lines.extend(self._render_functions_detail(module_functions))

        return "\n".join(lines)

    def _get_module_classes(self, mod_name: str) -> Dict[str, ClassInfo]:
        """Get public classes for a module."""
        return {
            k: v for k, v in self.result.classes.items()
            if v.module == mod_name and not v.name.startswith("_")
        }

    def _get_module_functions(self, mod_name: str) -> Dict[str, FunctionInfo]:
        """Get public functions for a module."""
        return {
            k: v for k, v in self.result.functions.items()
            if v.module == mod_name and not v.is_method and not v.name.startswith("_")
        }

    def _render_classes_detail(self, module_classes: Dict[str, ClassInfo]) -> List[str]:
        """Render classes with their method summaries."""
        lines = []
        for cls_name, cls_info in sorted(module_classes.items()):
            bases = f" ({', '.join(cls_info.bases)})" if cls_info.bases else ""
            src = self._linker.source_link(cls_info.file, cls_info.line)
            lines.append(f"**`{cls_info.name}`**{bases} {src}")
            if cls_info.docstring:
                lines.append(f": {cls_info.docstring.splitlines()[0]}")
            lines.append("")
            methods = self._get_public_methods(cls_info)
            if methods:
                lines.append("| Method | Args | Returns | CC |")
                lines.append("|--------|------|---------|----|")
                for m in methods:
                    args = ", ".join(a for a in m.args[:4] if a != "self")
                    ret = m.returns or "—"
                    cc = m.complexity.get("cyclomatic_complexity",
                                          m.complexity.get("cyclomatic", "—"))
                    lines.append(f"| `{m.name}` | `{args}` | `{ret}` | {cc} |")
                lines.append("")
        return lines

    def _render_functions_detail(self, module_functions: Dict[str, FunctionInfo]) -> List[str]:
        """Render standalone functions list."""
        lines = []
        for func_name, func_info in sorted(module_functions.items()):
            args = ", ".join(a for a in func_info.args if a != "self")
            ret = f" → {func_info.returns}" if func_info.returns else ""
            doc_line = ""
            if func_info.docstring:
                doc_line = f" — {func_info.docstring.splitlines()[0]}"
            src = self._linker.source_link(func_info.file, func_info.line)
            lines.append(f"- `{func_info.name}({args}){ret}`{doc_line} {src}")
        lines.append("")
        return lines

    def _get_public_methods(self, cls_info: ClassInfo) -> List[FunctionInfo]:
        """Get public (non-dunder) methods."""
        methods = []
        for method_name in cls_info.methods:
            short = method_name.split(".")[-1]
            if short.startswith("_"):
                continue
            for key in [method_name, f"{cls_info.qualified_name}.{short}"]:
                if key in self.result.functions:
                    methods.append(self.result.functions[key])
                    break
        return methods

    def _count_file_lines(self, file_path: str) -> int:
        """Count lines in source file."""
        try:
            path = Path(file_path)
            if path.exists():
                return len(path.read_text(encoding="utf-8").splitlines())
        except (OSError, UnicodeDecodeError):
            pass
        return 0

    def _calc_module_avg_cc(self, mod_name: str) -> float:
        """Calculate average cyclomatic complexity for module functions."""
        complexities = []
        for func in self.result.functions.values():
            if func.module == mod_name:
                cc = func.complexity.get(
                    "cyclomatic_complexity", func.complexity.get("cyclomatic", 0)
                )
                if cc > 0:
                    complexities.append(cc)
        return round(sum(complexities) / len(complexities), 1) if complexities else 0.0

    def _get_module_docstring(self, mod_info: ModuleInfo) -> str:
        """Try to extract module-level docstring."""
        try:
            path = Path(mod_info.file)
            if path.exists():
                tree = ast.parse(path.read_text(encoding="utf-8"))
                return ast.get_docstring(tree) or ""
        except Exception:
            pass
        return ""
