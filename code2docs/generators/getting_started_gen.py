"""Getting Started guide generator."""

from typing import List

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..analyzers.dependency_scanner import DependencyScanner
from ..llm_helper import LLMHelper


class GettingStartedGenerator:
    """Generate docs/getting-started.md from entry points and dependencies."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self.llm = LLMHelper(config.llm)

    def generate(self) -> str:
        """Generate getting-started.md content."""
        project = self.config.project_name or "Project"
        lines = [
            f"# Getting Started with {project}\n",
        ]
        # LLM-generated intro if available
        intro = self._generate_intro(project)
        if intro:
            lines.append(intro)
            lines.append("")
        lines += [
            self._render_prerequisites(),
            "",
            self._render_installation(),
            "",
            self._render_first_usage(),
            "",
            self._render_next_steps(),
            "",
        ]
        return "\n".join(lines)

    def _render_prerequisites(self) -> str:
        """Render prerequisites section."""
        dep_scanner = DependencyScanner()
        deps = dep_scanner.scan(self.result.project_path)
        lines = ["## Prerequisites\n"]

        lang = deps.language
        if lang in ("javascript", "typescript"):
            node_ver = deps.runtime_version or ">=18"
            lines.append(f"- Node.js {node_ver}")
            if "pnpm" in deps.install_command:
                lines.append("- pnpm")
            elif "yarn" in deps.install_command:
                lines.append("- yarn")
            else:
                lines.append("- npm")
        elif lang == "rust":
            lines.append("- Rust toolchain (rustup)")
            lines.append("- cargo")
        elif lang == "go":
            go_ver = deps.runtime_version or ">=1.21"
            lines.append(f"- Go {go_ver}")
        else:
            py_ver = deps.python_version or ">=3.9"
            lines.append(f"- Python {py_ver}")
            lines.append("- pip (or your preferred package manager)")

        if deps.dependencies:
            lines.append(f"- {len(deps.dependencies)} dependencies (installed automatically)")
        return "\n".join(lines)

    def _render_installation(self) -> str:
        """Render installation section."""
        dep_scanner = DependencyScanner()
        deps = dep_scanner.scan(self.result.project_path)
        cmd = deps.install_command or f"pip install {self.config.project_name or '.'}"
        repo_url = self.config.repo_url or "<repository-url>"
        project = self.config.project_name or "project"
        lang = deps.language

        lines = [
            "## Installation\n",
            "```bash",
            cmd,
            "```\n",
            "To install from source:\n",
            "```bash",
            f"git clone {repo_url}",
            f"cd {project}",
        ]

        if lang in ("javascript", "typescript"):
            lines.append(cmd)
        elif lang == "rust":
            lines.append("cargo build --release")
        elif lang == "go":
            lines.append("go build ./...")
        else:
            lines.append("pip install -e .")

        lines.append("```")
        return "\n".join(lines)

    def _render_first_usage(self) -> str:
        """Render first usage example — CLI + Python API."""
        project = self.config.project_name or "project"
        lines = [
            "## Quick Start\n",
            "### Command Line\n",
            "```bash",
            f"# Generate full documentation for your project",
            f"{project} ./path/to/your/project",
            "",
            f"# Preview what would be generated (no file writes)",
            f"{project} ./path/to/your/project --dry-run",
            "",
            f"# Only regenerate README",
            f"{project} ./path/to/your/project --readme-only",
            "```\n",
            "### Python API\n",
            "```python",
        ]

        # Find user-facing public functions, prioritize by name
        public_funcs = [
            f for f in self.result.functions.values()
            if not f.is_private and not f.is_method
            and not f.name.startswith("_")
        ]
        # Prefer functions whose name suggests a user-facing API
        priority_prefixes = ("generate", "analyze", "create", "build", "run", "process")
        public_funcs.sort(
            key=lambda f: (
                0 if any(f.name.startswith(p) for p in priority_prefixes) else 1,
                f.name,
            )
        )
        if public_funcs:
            func = public_funcs[0]
            mod = func.module or project
            args = [a for a in func.args if a != "self"]
            args_str = ", ".join(f'"{a}"' if i == 0 else f"{a}=..."
                                 for i, a in enumerate(args[:3]))
            lines.append(f"from {mod} import {func.name}")
            lines.append("")
            if func.docstring:
                lines.append(f"# {func.docstring.splitlines()[0]}")
            lines.append(f"result = {func.name}({args_str})")
        else:
            lines.append(f"import {project}")

        lines.append("```")
        return "\n".join(lines)

    def _generate_intro(self, project: str) -> str:
        """Generate LLM-enhanced intro paragraph. Returns '' if unavailable."""
        if not self.llm.available:
            return ""
        # Gather CLI commands
        cli_funcs = [
            f for f in self.result.functions.values()
            if not f.is_private and not f.is_method
            and f.module and "cli" in f.module
        ]
        cli_str = ", ".join(f.name for f in cli_funcs[:8]) or "N/A"
        # Gather public API
        public_funcs = [
            f for f in self.result.functions.values()
            if not f.is_private and not f.is_method
            and not f.name.startswith("_")
        ]
        api_str = ", ".join(f"{f.name}()" for f in public_funcs[:8]) or "N/A"
        result = self.llm.generate_getting_started_summary(project, cli_str, api_str)
        return result or ""

    def _render_next_steps(self) -> str:
        """Render next steps with links to other docs."""
        lines = [
            "## What's Next\n",
            "- 📖 [API Reference](api.md) — Full function and class documentation",
            "- 🏗️ [Architecture](architecture.md) — System design and module relationships",
            "- 📊 [Coverage Report](coverage.md) — Docstring coverage analysis",
            "- 🔗 [Dependency Graph](dependency-graph.md) — Module dependency visualization",
        ]
        return "\n".join(lines)

    def _get_top_level_modules(self) -> List[str]:
        """Get top-level package names."""
        top = set()
        for mod_name in self.result.modules:
            parts = mod_name.split(".")
            if len(parts) >= 1:
                top.add(parts[0])
        return sorted(top)
