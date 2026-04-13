
PORT_4 = 4
CONSTANT_5 = 5
CONSTANT_50 = 50


PORT_4 = PORT_4
CONSTANT_5 = CONSTANT_5
CONSTANT_50 = CONSTANT_50


PORT_4 = PORT_4
CONSTANT_5 = CONSTANT_5
CONSTANT_50 = CONSTANT_50


PORT_4 = PORT_4
CONSTANT_5 = CONSTANT_5
CONSTANT_50 = CONSTANT_50



PORT_4 = PORT_4
CONSTANT_5 = CONSTANT_5
CONSTANT_50 = CONSTANT_50

PORT_4 = PORT_4
CONSTANT_5 = CONSTANT_5
CONSTANT_50 = CONSTANT_50

"""Auto-generate usage examples from public signatures and entry points."""

from pathlib import Path
from typing import Dict, List, Optional, Set

from code2llm.api import AnalysisResult, FunctionInfo, ClassInfo

from ..config import Code2DocsConfig

# Default type hints → example values

if __name__ == "__main__":
    _TYPE_EXAMPLES = {
    "str": '"./my-project"',
    "Path": 'Path("./my-project")',
    "int": "10",
    "float": "0.5",
    "bool": "True",
    "list": "[]",
    "dict": "{}",
    "List": "[]",
    "Dict": "{}",
    "Optional": "None",
    "None": "None",
}

# Arg name → realistic example value
    _ARG_EXAMPLES = {
    "project_path": '"./my-project"',
    "path": '"./my-project"',
    "source": '"./src"',
    "output": '"./docs"',
    "output_dir": '"./docs"',
    "output_path": '"./docs/README.md"',
    "config": "config",
    "config_path": '"code2docs.yaml"',
    "result": "result",
    "name": '"my-project"',
    "project_name": '"my-project"',
    "verbose": "True",
    "dry_run": "False",
    "readme_only": "False",
    "sections": '["overview", "install", "quickstart"]',
    "content": '"# My Doc\\n## Section"',
    "markdown_content": '"# My Doc\\n## Section"',
    "max_depth": "3",
    "target": "80",
    "badge_types": '["version", "python"]',
    "stats": "{}",
    "deps": "[]",
    "sync_markers": "True",
    "docstring": '"""My function docstring."""',
}


class ExamplesGenerator:
    """Generate examples/ — usage examples from public API signatures."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self._pkg = self._detect_package_name()

    def _get_example_value(self, arg_name: str) -> str:
        """Get realistic example value based on actual project config."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        
        # Map argument names to actual config values
        arg_mappings = {
            "project_path": f'"./{project_name}"',
            "path": f'"./{project_name}"',
            "source": f'"{self.config.source}"' if self.config.source else '"./src"',
            "output": f'"{self.config.output}"' if self.config.output else '"./docs"',
            "output_dir": f'"{self.config.output}"' if self.config.output else '"./docs"',
            "output_path": f'"{self.config.readme_output}"' if self.config.readme_output else '"./docs/README.md"',
            "config": "config",
            "config_path": '"code2docs.yaml"',
            "result": "result",
            "name": f'"{project_name}"',
            "project_name": f'"{project_name}"',
            "verbose": "True",
            "dry_run": "False",
            "readme_only": "False",
            "sections": '["overview", "install", "quickstart"]',
            "content": '"# My Doc\\n## Section"',
            "markdown_content": '"# My Doc\\n## Section"',
            "max_depth": "3",
            "target": "80",
            "badge_types": '["version", "python"]',
            "stats": "{}",
            "deps": "[]",
            "sync_markers": "True",
            "docstring": '"""My function docstring."""',
        }
        
        if arg_name in arg_mappings:
            return arg_mappings[arg_name]
        
        # Fallback to original static examples
        return _ARG_EXAMPLES.get(arg_name, '"..."')

    def generate_all(self) -> Dict[str, str]:
        """Generate all example files. Returns {filename: content}."""
        files: Dict[str, str] = {}
        files["quickstart.py"] = self._generate_quickstart()
        files["advanced_usage.py"] = self._generate_advanced()
        return files

    # ── quickstart.py ─────────────────────────────────────────────────

    def _generate_quickstart(self) -> str:
        """Generate quickstart.py — minimal working example."""
        pkg = self._pkg
        lines = [
            f'"""',
            f"Quickstart — {pkg}",
            f"",
            f"Minimal working examples for the most common use cases.",
            f"Run: python examples/quickstart.py",
            f'"""',
            "",
            "from pathlib import Path",
            "",
        ]

        # Find the top-level convenience functions (generate_readme, generate_docs, etc.)
        convenience = self._find_convenience_functions()
        api_classes = self._find_api_classes()

        # --- Imports ---
        imports: Set[str] = set()
        for func in convenience:
            imports.add(f"from {pkg} import {func.name}")
        for cls in api_classes:
            imports.add(f"from {pkg} import {cls.name}")
        if not imports:
            imports.add(f"import {pkg}")
        lines.extend(sorted(imports))
        lines.append("")

        # --- Example 1: Config (define first so later examples can use it) ---
        config_cls = self._find_class_by_name("Code2DocsConfig")
        project_name = self.config.project_name or Path(self.result.project_path).name
        source = self.config.source or "./"
        output = self.config.output or "./docs"
        if config_cls:
            lines.append('# ' + '=' * CONSTANT_50)
            lines.append("# Example 1: Configuration")
            lines.append('# ' + '=' * CONSTANT_50)
            lines.append("")
            lines.append(f"config = {config_cls.name}(")
            lines.append(f'    project_name="{project_name}",')
            lines.append(f'    source="{source}",')
            lines.append(f'    output="{output}",')
            lines.append("    verbose=True,")
            lines.append(")")
            lines.append("")

        # --- Example 2: Quick generate ---
        lines.append("")
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("# Example 2: Generate documentation")
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("")
        
        project_path = f'"./{project_name}"' if project_name != "." else '"./"'

        gen_func = self._find_function_by_name("generate_readme")
        if gen_func:
            lines.append("# Generate a README for your project")
            lines.append(f'generate_readme({project_path}, output="README.md")')
            lines.append("")

        docs_func = self._find_function_by_name("generate_docs")
        if docs_func:
            lines.append("# Generate all documentation")
            if config_cls:
                lines.append(f'docs = generate_docs({project_path}, config=config)')
            else:
                lines.append(f'docs = generate_docs({project_path})')
            lines.append('print(f"Generated {len(docs)} documentation sections")')
            lines.append("")

        # --- Example 3: Scanner ---
        scanner_cls = self._find_class_by_name("ProjectScanner")
        if scanner_cls:
            lines.append("")
            lines.append('# ' + '=' * CONSTANT_50)
            lines.append("# Example 3: Analyze a project programmatically")
            lines.append('# ' + '=' * CONSTANT_50)
            lines.append("")
            lines.append(f"from {pkg}.analyzers.project_scanner import ProjectScanner")
            lines.append("")
            lines.append("scanner = ProjectScanner(config)")
            lines.append(f'result = scanner.analyze({project_path})')
            lines.append("")
            lines.append('print(f"Found {len(result.functions)} functions")')
            lines.append('print(f"Found {len(result.classes)} classes")')
            lines.append('print(f"Found {len(result.modules)} modules")')

        lines.append("")
        return "\n".join(lines)

    # ── advanced_usage.py ─────────────────────────────────────────────

    def _generate_advanced(self) -> str:
        """Generate advanced_usage.py — individual generator usage, sync, etc."""
        pkg = self._pkg
        lines = [
            f'"""',
            f"Advanced usage — {pkg}",
            f"",
            f"Shows how to use individual generators, sync, and formatters.",
            f"Run: python examples/advanced_usage.py",
            f'"""',
            "",
            "from pathlib import Path",
            "",
        ]

        gen_classes = self._find_generator_classes()
        if gen_classes:
            lines.extend(self._render_generator_examples(pkg, gen_classes))

        fmt_funcs = self._find_formatter_functions()
        if fmt_funcs:
            lines.extend(self._render_formatter_examples(pkg, fmt_funcs))

        differ_cls = self._find_class_by_name("Differ")
        if differ_cls:
            lines.extend(self._render_sync_examples(pkg))

        lines.append("")
        return "\n".join(lines)

    def _render_generator_examples(self, pkg: str, gen_classes: List[ClassInfo]) -> List[str]:
        """Render individual generator usage examples."""
        lines = []
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("# Using individual generators")
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("")
        lines.append(f"from {pkg} import Code2DocsConfig")
        lines.append(f"from {pkg}.analyzers.project_scanner import ProjectScanner")
        for cls in gen_classes[:PORT_4]:
            mod = cls.module or pkg
            if not mod.startswith(pkg):
                mod = f"{pkg}.{mod}"
            lines.append(f"from {mod} import {cls.name}")
        lines.append("")
        lines.append("# Step 1: Analyze the project")
        lines.append("config = Code2DocsConfig(project_name=\"my-project\")")
        lines.append("project_name_adv = config.project_name")
        lines.append("scanner = ProjectScanner(config)")
        lines.append('result = scanner.analyze(f"./{project_name_adv}") if project_name_adv != "." else scanner.analyze("./")')
        lines.append("")

        for i, cls in enumerate(gen_classes[:PORT_4], start=2):
            gen_name = cls.name[0].lower() + cls.name[1:]
            gen_name = gen_name.replace("Generator", "_gen")
            lines.append(f"# Step {i}: Generate with {cls.name}")
            lines.append(f"{gen_name} = {cls.name}(config, result)")

            methods = self._get_public_methods(cls)
            gen_method = next(
                (m for m in methods if m.name in ("generate", "generate_all")),
                methods[0] if methods else None,
            )
            if gen_method:
                ret = gen_method.returns or "str"
                if "Dict" in ret or "dict" in ret:
                    lines.append(f"files = {gen_name}.{gen_method.name}()")
                    lines.append('print(f"Generated {len(files)} files")')
                else:
                    lines.append(f"content = {gen_name}.{gen_method.name}()")
                    lines.append('print(f"Generated {len(content)} characters")')
            lines.append("")
        return lines

    def _find_formatter_functions(self) -> List[FunctionInfo]:
        """Find formatter functions for examples."""
        funcs = [
            self._find_function_by_name("generate_badges"),
            self._find_function_by_name("generate_toc"),
        ]
        return [f for f in funcs if f]

    def _render_formatter_examples(self, pkg: str, fmt_funcs: List[FunctionInfo]) -> List[str]:
        """Render formatter usage examples."""
        lines = [""]
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("# Formatters")
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("")
        for func in fmt_funcs:
            mod = func.module or pkg
            if not mod.startswith(pkg):
                mod = f"{pkg}.{mod}"
            lines.append(f"from {mod} import {func.name}")
        lines.append("")

        badges_func = self._find_function_by_name("generate_badges")
        if badges_func:
            lines.append("# Generate shields.io badges")
            lines.append('badges = generate_badges(')
            lines.append('    project_name="my-project",')
            lines.append('    badge_types=["version", "python", "coverage"],')
            lines.append('    stats={"version": "1.0.0", "python": ">=3.9"},')
            lines.append(')')
            lines.append('for badge in badges:')
            lines.append('    print(badge)')
            lines.append("")

        toc_func = self._find_function_by_name("generate_toc")
        if toc_func:
            lines.append("# Generate table of contents")
            lines.append('markdown = "# Title\\n## Section 1\\n## Section 2\\n### Subsection"')
            lines.append("toc = generate_toc(markdown, max_depth=2)")
            lines.append("print(toc)")
            lines.append("")
        return lines

    def _render_sync_examples(self, pkg: str) -> List[str]:
        """Render sync/diff usage examples."""
        lines = [""]
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("# Sync — detect and apply changes")
        lines.append('# ' + '=' * CONSTANT_50)
        lines.append("")
        lines.append(f"from {pkg}.sync.differ import Differ")
        lines.append(f"from {pkg}.sync.updater import Updater")
        lines.append("")
        lines.append("# Detect changes since last generation")
        lines.append("differ = Differ(config)")
        lines.append('changes = differ.detect_changes("./my-project")')
        lines.append("")
        lines.append("if changes:")
        lines.append('    print(f"Detected {len(changes)} changed modules:")')
        lines.append("    for change in changes:")
        lines.append('        print(f"  {change}")')
        lines.append("")
        lines.append("    # Apply selective update")
        lines.append("    updater = Updater(config)")
        lines.append('    updater.apply("./my-project", changes)')
        lines.append('    print("Documentation updated!")')
        lines.append("else:")
        lines.append('    print("No changes detected.")')
        return lines

    # ── helpers ────────────────────────────────────────────────────────

    def _detect_package_name(self) -> str:
        """Detect the top-level package name from analysis."""
        name = self.config.project_name or Path(self.result.project_path).name

        # Count which top-level root appears most often in modules
        from collections import Counter
        roots = Counter()
        for mod_name in self.result.modules:
            root = mod_name.split(".")[0]
            if not root.startswith("_"):
                roots[root] += 1

        if roots:
            # If project_name matches a root, use it; else use most common
            if name in roots:
                return name
            return roots.most_common(1)[0][0]
        return name

    def _find_convenience_functions(self) -> List[FunctionInfo]:
        """Find top-level convenience functions (generate_*, analyze_*)."""
        targets = ("generate_readme", "generate_docs", "analyze_and_document")
        found = []
        for name in targets:
            func = self._find_function_by_name(name)
            if func:
                found.append(func)
        return found

    def _find_api_classes(self) -> List[ClassInfo]:
        """Find user-facing config/API classes."""
        targets = ("Code2DocsConfig",)
        return [c for c in self.result.classes.values() if c.name in targets]

    def _find_generator_classes(self) -> List[ClassInfo]:
        """Find Generator classes, prioritized by user-facing importance."""
        priority = ["ReadmeGenerator", "ArchitectureGenerator",
                    "CoverageGenerator", "DepGraphGenerator"]
        found = []
        for name in priority:
            cls = self._find_class_by_name(name)
            if cls:
                found.append(cls)
        return found

    def _find_function_by_name(self, name: str) -> Optional[FunctionInfo]:
        """Find a function by short name."""
        for key, func in self.result.functions.items():
            if func.name == name and not func.is_method:
                return func
        return None

    def _find_class_by_name(self, name: str) -> Optional[ClassInfo]:
        """Find a class by short name."""
        for key, cls in self.result.classes.items():
            if cls.name == name:
                return cls
        return None

    def _build_realistic_args(self, func: FunctionInfo) -> str:
        """Build a realistic argument string for a function call."""
        args = [a for a in func.args if a not in ("self", "cls")]
        parts = []
        for arg in args[:CONSTANT_5]:
            val = self._get_example_value(arg)
            if not val or val == '"..."':
                # Try type hint
                val = self._example_from_type(func, arg)
            if not val:
                val = '"..."'
            parts.append(f"{arg}={val}" if len(args) > 1 else val)
        return ", ".join(parts)

    def _example_from_type(self, func: FunctionInfo, arg: str) -> Optional[str]:
        """Try to infer example value from type annotation."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        
        # FunctionInfo.returns gives return type, but arg types
        # are not always available; use naming heuristics
        if "path" in arg.lower():
            return f'"./{project_name}"'
        if "name" in arg.lower():
            return f'"{project_name}"'
        if "dir" in arg.lower():
            return f'"{self.config.output}"' if self.config.output else '"./docs"'
        if arg.startswith("is_") or arg.startswith("enable"):
            return "True"
        if "count" in arg.lower() or "max" in arg.lower() or "min" in arg.lower():
            return "10"
        return None

    def _get_public_methods(self, cls: ClassInfo) -> List[FunctionInfo]:
        """Get public methods of a class."""
        methods = []
        for method_name in cls.methods:
            short = method_name.split(".")[-1]
            if short.startswith("_"):
                continue
            for key in [method_name, f"{cls.qualified_name}.{short}"]:
                func = self.result.functions.get(key)
                if func:
                    methods.append(func)
                    break
        return methods

    def write_all(self, output_dir: str, files: Dict[str, str]) -> None:
        """Write all generated example files."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            (out / filename).write_text(content, encoding="utf-8")
