"""API reference documentation generator — single consolidated api.md."""

from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from code2llm.api import AnalysisResult, FunctionInfo, ClassInfo, ModuleInfo

from ..config import Code2DocsConfig
from ._source_links import SourceLinker


class ApiReferenceGenerator:
    """Generate docs/api.md — consolidated API reference."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self._linker = SourceLinker(config, result)

    def generate(self) -> str:
        """Generate a single api.md with all public API grouped by package."""
        project = self.config.project_name or Path(self.result.project_path).name
        total_funcs = len(self.result.functions)
        total_classes = len(self.result.classes)

        lines = [
            f"# {project} — API Reference\n",
            f"> {len(self.result.modules)} modules | "
            f"{total_funcs} functions | {total_classes} classes\n",
        ]

        # Group modules by top-level package
        groups = self._group_modules()

        # Table of contents
        lines.append("## Contents\n")
        for group_name, modules in groups.items():
            anchor = group_name.replace(".", "").replace(" ", "-").lower()
            non_trivial = [m for m in modules if self._has_content(m)]
            if non_trivial:
                lines.append(f"- [{group_name}](#{anchor}) ({len(non_trivial)} modules)")
        lines.append("")

        # Render each group
        for group_name, modules in groups.items():
            non_trivial = [(m, self.result.modules[m]) for m in modules
                           if self._has_content(m)]
            if not non_trivial:
                continue
            lines.append(f"## {group_name}\n")
            for mod_name, mod_info in non_trivial:
                lines.append(self._render_module_section(mod_name, mod_info))

        return "\n".join(lines)

    def _group_modules(self) -> Dict[str, List[str]]:
        """Group module names by top-level package."""
        groups: Dict[str, List[str]] = defaultdict(list)
        for mod_name in sorted(self.result.modules.keys()):
            parts = mod_name.split(".")
            if parts[0].startswith("_"):
                continue  # skip __main__, _internal, etc.
            group = parts[0] if len(parts) > 1 else "Core"
            groups[group].append(mod_name)
        return dict(groups)

    def _has_content(self, mod_name: str) -> bool:
        """Check if a module has any public functions or classes."""
        mod = self.result.modules.get(mod_name)
        if not mod:
            return False
        has_funcs = any(
            not f.is_method and not f.name.startswith("_")
            for f in self.result.functions.values()
            if f.module == mod_name or f.name.startswith(mod_name + ".")
        )
        has_classes = any(
            not c.name.startswith("_")
            for c in self.result.classes.values()
            if c.module == mod_name or c.qualified_name.startswith(mod_name + ".")
        )
        return has_funcs or has_classes

    def _render_module_section(self, mod_name: str, mod_info: ModuleInfo) -> str:
        """Render a module as a subsection within the consolidated doc."""
        src = self._linker.file_link(mod_info.file)
        heading = f"### `{mod_name}` {src}" if src else f"### `{mod_name}`"
        lines = [f"{heading}\n"]

        module_classes = self._get_module_classes(mod_name)
        if module_classes:
            lines.extend(self._render_classes_table(module_classes))
            lines.extend(self._render_class_methods(module_classes))

        module_functions = self._get_module_functions(mod_name)
        if module_functions:
            lines.extend(self._render_functions_table(module_functions))

        return "\n".join(lines)

    def _get_module_classes(self, mod_name: str) -> Dict[str, ClassInfo]:
        """Get all public classes for a module."""
        return {
            k: v for k, v in self.result.classes.items()
            if (v.module == mod_name or k.startswith(mod_name + "."))
            and not v.name.startswith("_")
        }

    def _get_module_functions(self, mod_name: str) -> Dict[str, FunctionInfo]:
        """Get all public functions for a module."""
        return {
            k: v for k, v in self.result.functions.items()
            if (v.module == mod_name or k.startswith(mod_name + "."))
            and not v.is_method and not v.name.startswith("_")
        }

    def _render_classes_table(self, module_classes: Dict[str, ClassInfo]) -> List[str]:
        """Render the classes summary table."""
        lines = ["| Class | Methods | Description | Source |", "|-------|---------|-------------|--------|"]
        for cls_name, cls_info in sorted(module_classes.items()):
            doc = cls_info.docstring.splitlines()[0] if cls_info.docstring else "—"
            public_methods = [m for m in cls_info.methods
                              if not m.split(".")[-1].startswith("_")]
            src = self._linker.source_link(cls_info.file, cls_info.line)
            lines.append(f"| `{cls_info.name}` | {len(public_methods)} | {doc} | {src} |")
        lines.append("")
        return lines

    def _render_class_methods(self, module_classes: Dict[str, ClassInfo]) -> List[str]:
        """Render expanded methods for classes with >=2 public methods."""
        lines = []
        for cls_name, cls_info in sorted(module_classes.items()):
            methods = self._get_public_methods(cls_info)
            if len(methods) >= 2:
                lines.append(f"**`{cls_info.name}` methods:**\n")
                for m in methods:
                    sig = self._format_signature(m)
                    doc = f" — {m.docstring.splitlines()[0]}" if m.docstring else ""
                    lines.append(f"- `{sig}`{doc}")
                lines.append("")
        return lines

    def _render_functions_table(self, module_functions: Dict[str, FunctionInfo]) -> List[str]:
        """Render the functions summary table."""
        lines = ["| Function | Signature | CC | Description | Source |", "|----------|-----------|----|-----------  |--------|"]
        for func_name, func_info in sorted(module_functions.items()):
            sig = self._format_signature(func_info)
            cc = func_info.complexity.get(
                "cyclomatic_complexity",
                func_info.complexity.get("cyclomatic", "—"),
            )
            doc = func_info.docstring.splitlines()[0] if func_info.docstring else "—"
            warn = " ⚠️" if isinstance(cc, (int, float)) and cc > 10 else ""
            src = self._linker.source_link(func_info.file, func_info.line)
            lines.append(f"| `{func_info.name}` | `{sig}` | {cc}{warn} | {doc} | {src} |")
        lines.append("")
        return lines

    def _get_public_methods(self, cls_info: ClassInfo) -> List[FunctionInfo]:
        """Get public (non-dunder) methods of a class."""
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

    @staticmethod
    def _format_signature(func: FunctionInfo) -> str:
        """Format a function signature string."""
        args = [a for a in func.args if a != "self"]
        args_str = ", ".join(args[:4])
        if len(args) > 4:
            args_str += ", ..."
        ret = f" → {func.returns}" if func.returns else ""
        return f"{func.name}({args_str}){ret}"
