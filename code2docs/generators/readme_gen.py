"""README.md generator from AnalysisResult."""

import re
from pathlib import Path
from typing import Dict, List, Optional

from jinja2 import Environment, PackageLoader, select_autoescape

from code2llm.api import AnalysisResult, FunctionInfo, ClassInfo

from ..config import Code2DocsConfig
from ..analyzers.dependency_scanner import DependencyScanner
from ..analyzers.endpoint_detector import EndpointDetector
from ..formatters.badges import generate_badges
from ..formatters.toc import generate_toc
from ..llm_helper import LLMHelper


MARKER_START = "<!-- code2docs:start -->"
MARKER_END = "<!-- code2docs:end -->"


class ReadmeGenerator:
    """Generate README.md from AnalysisResult."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self.llm = LLMHelper(config.llm)
        self.env = Environment(
            loader=PackageLoader("code2docs", "templates"),
            autoescape=select_autoescape([]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate(self) -> str:
        """Generate full README content."""
        sections = self.config.readme.sections
        project_name = self.config.project_name or Path(self.result.project_path).name

        context = self._build_context(project_name)

        try:
            template = self.env.get_template("readme.md.j2")
            return template.render(**context, sections=sections)
        except Exception:
            # Fallback: build manually if template fails
            return self._build_manual(project_name, sections, context)

    def _build_context(self, project_name: str) -> Dict:
        """Build template context from analysis result."""
        # Dependencies
        dep_scanner = DependencyScanner()
        deps = dep_scanner.scan(self.result.project_path)

        # Endpoints
        endpoint_detector = EndpointDetector()
        endpoints = endpoint_detector.detect(self.result, self.result.project_path)

        # Public API
        public_functions = {
            k: v for k, v in self.result.functions.items()
            if not v.is_private and not v.is_method
        }
        public_classes = {
            k: v for k, v in self.result.classes.items()
        }

        # Entry points — keep only module-level public functions,
        # exclude class methods (Capitalized segments) and dunder/private names
        entry_points = [
            ep for ep in (self.result.entry_points or [])
            if not any(
                seg.startswith("_") or (seg[0].isupper() if seg else False)
                for seg in ep.split(".")
            )
        ]

        # Metrics
        stats = self.result.stats or {}
        avg_complexity = self._calc_avg_complexity()

        # Module tree
        module_tree = self._build_module_tree()

        # Project description: LLM if available, else package docstring
        project_description = self._generate_description(project_name, entry_points)

        # Metadata: author, license, contributors
        metadata = self._extract_project_metadata()

        # Extras from pyproject.toml
        extras = self._extract_extras()

        return {
            "project_name": project_name,
            "project_path": self.result.project_path,
            "project_description": project_description,
            "badges": generate_badges(project_name, self.config.readme.badges, stats, deps),
            "stats": stats,
            "avg_complexity": avg_complexity,
            "dependencies": deps,
            "endpoints": endpoints,
            "public_functions": public_functions,
            "public_classes": public_classes,
            "entry_points": entry_points,
            "module_tree": module_tree,
            "modules": self.result.modules,
            "sync_markers": self.config.readme.sync_markers,
            # New metadata fields
            "author": metadata.get("author", ""),
            "license": metadata.get("license", ""),
            "license_file": metadata.get("license_file", ""),
            "contributors": metadata.get("contributors", []),
            "repo_url": self.config.repo_url,
            "version": metadata.get("version", "0.1.0"),
            "extras": extras,
        }

    def _calc_avg_complexity(self) -> float:
        """Calculate average cyclomatic complexity."""
        complexities = []
        for func in self.result.functions.values():
            cc = func.complexity.get("cyclomatic_complexity",
                                     func.complexity.get("cyclomatic", 0))
            if cc > 0:
                complexities.append(cc)
        return round(sum(complexities) / len(complexities), 1) if complexities else 0.0

    def _build_module_tree(self) -> str:
        """Build text-based module tree."""
        if not self.result.modules:
            return ""

        lines = []
        sorted_modules = sorted(self.result.modules.keys())
        for mod_name in sorted_modules:
            mod = self.result.modules[mod_name]
            prefix = "📦" if mod.is_package else "📄"
            func_count = len(mod.functions)
            class_count = len(mod.classes)
            detail = []
            if func_count:
                detail.append(f"{func_count} functions")
            if class_count:
                detail.append(f"{class_count} classes")
            detail_str = f" ({', '.join(detail)})" if detail else ""
            lines.append(f"{prefix} `{mod_name}`{detail_str}")

        return "\n".join(lines)

    def _generate_description(self, project_name: str, entry_points: List[str]) -> str:
        """Generate project description: LLM if available, else package docstring."""
        # Try LLM first
        if self.llm.available:
            modules_summary = ", ".join(sorted(self.result.modules.keys())[:15])
            eps_str = ", ".join(entry_points[:10])
            llm_desc = self.llm.generate_project_description(
                project_name, modules_summary, eps_str
            )
            if llm_desc:
                return llm_desc
        # Fallback: extract from package docstring
        return self._extract_project_description(project_name)

    def _extract_project_description(self, project_name: str) -> str:
        """Extract project description from top-level package docstring."""
        # Try top-level package module (e.g. "mylib" or "mylib.__init__")
        for mod_name, mod_info in self.result.modules.items():
            if mod_info.is_package and mod_name == project_name:
                doc = getattr(mod_info, "docstring", None)
                if doc:
                    return doc.strip()
        # Fallback: first package with a docstring
        for mod_info in self.result.modules.values():
            doc = getattr(mod_info, "docstring", None)
            if mod_info.is_package and doc:
                return doc.strip()
        return ""

    def _extract_project_metadata(self) -> Dict:
        """Extract project metadata (author, license, version) from pyproject.toml or git."""
        metadata = {
            "author": "",
            "license": "",
            "license_file": "",
            "contributors": [],
            "version": "0.1.0",
        }

        # Try pyproject.toml
        try:
            import tomllib
            pyproject_path = Path(self.result.project_path) / "pyproject.toml"
            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    data = tomllib.load(f)

                project = data.get("project", {})
                metadata["version"] = project.get("version", metadata["version"])

                # Authors
                authors = project.get("authors", [])
                if authors:
                    if isinstance(authors[0], dict):
                        metadata["author"] = authors[0].get("name", "")
                        metadata["contributors"] = [a.get("name", "") for a in authors[1:] if a.get("name")]
                    else:
                        metadata["author"] = str(authors[0])

                # License
                metadata["license"] = project.get("license", {}).get("text", "")
                if not metadata["license"]:
                    metadata["license"] = project.get("license", "")
        except Exception:
            pass

        # Try git for contributors if not found
        if not metadata["contributors"]:
            try:
                import subprocess
                result = subprocess.run(
                    ["git", "shortlog", "-sne", "HEAD"],
                    capture_output=True, text=True, cwd=self.result.project_path
                )
                if result.returncode == 0:
                    contributors = []
                    for line in result.stdout.strip().split("\n")[:5]:
                        parts = line.split("\t")
                        if len(parts) >= 2:
                            contributors.append(parts[1])
                    metadata["contributors"] = contributors
            except Exception:
                pass

        # Try git config for author if not found
        if not metadata["author"]:
            try:
                import subprocess
                name = subprocess.run(
                    ["git", "config", "user.name"],
                    capture_output=True, text=True, cwd=self.result.project_path
                )
                email = subprocess.run(
                    ["git", "config", "user.email"],
                    capture_output=True, text=True, cwd=self.result.project_path
                )
                if name.returncode == 0 and name.stdout.strip():
                    author = name.stdout.strip()
                    if email.returncode == 0 and email.stdout.strip():
                        author += f" <{email.stdout.strip()}>"
                    metadata["author"] = author
            except Exception:
                pass

        # Find LICENSE file
        license_paths = [
            Path(self.result.project_path) / lf
            for lf in ["LICENSE", "LICENSE.txt", "LICENSE.md", "COPYING"]
        ]
        # Also check parent directory if project_path is a nested package (e.g., code2docs/code2docs)
        parent_path = Path(self.result.project_path).parent
        if parent_path != Path(self.result.project_path):
            license_paths += [
                parent_path / lf
                for lf in ["LICENSE", "LICENSE.txt", "LICENSE.md", "COPYING"]
            ]

        for license_path in license_paths:
            if license_path.exists():
                metadata["license_file"] = license_path.name
                # Try to extract license name from file content
                if not metadata["license"]:
                    try:
                        content = license_path.read_text(encoding="utf-8").lower()
                        for license_type in ["mit", "apache", "gpl", "bsd", "mpl", "lgpl"]:
                            if license_type in content:
                                metadata["license"] = license_type.upper()
                                break
                    except Exception:
                        pass
                break

        return metadata

    def _extract_extras(self) -> List[Dict]:
        """Extract optional dependencies (extras) from pyproject.toml."""
        extras = []
        try:
            import tomllib
            pyproject_path = Path(self.result.project_path) / "pyproject.toml"
            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    data = tomllib.load(f)

                project = data.get("project", {})
                optional_deps = project.get("optional-dependencies", {})

                for name, deps in optional_deps.items():
                    description = {
                        "dev": "development tools",
                        "test": "testing tools",
                        "docs": "documentation tools",
                        "watch": "file watcher (watchdog)",
                        "mkdocs": "MkDocs integration",
                        "llm": "LLM integration (litellm)",
                        "git": "Git integration (GitPython)",
                        "all": "all optional features",
                    }.get(name, f"{name} features")

                    extras.append({
                        "name": name,
                        "description": description,
                        "dependencies": deps,
                    })
        except Exception:
            pass
        return extras

    def _build_manual(self, project_name: str, sections: List[str], context: Dict) -> str:
        """Fallback manual README builder (orchestrator)."""
        section_builders = {
            "overview": self._build_overview_section,
            "install": self._build_install_section,
            "quickstart": self._build_quickstart_section,
            "api": self._build_api_section,
            "structure": self._build_structure_section,
            "endpoints": self._build_endpoints_section,
        }
        parts: List[str] = []
        if context.get("sync_markers"):
            parts.append(MARKER_START)
        for section in sections:
            builder = section_builders.get(section)
            if builder:
                content = builder(project_name, context)
                if content:
                    parts.append(content)
        if context.get("sync_markers"):
            parts.append(MARKER_END)
        return "\n".join(parts)

    @staticmethod
    def _build_overview_section(project_name: str, context: Dict) -> str:
        """Build overview section with badges and stats."""
        parts = [f"# {project_name}\n"]
        if context.get("badges"):
            parts.append(context["badges"] + "\n")
        stats = context.get("stats", {})
        if stats:
            parts.append(
                f"> **{stats.get('functions_found', 0)}** functions | "
                f"**{stats.get('classes_found', 0)}** classes | "
                f"**{stats.get('files_processed', 0)}** files | "
                f"CC̄ = {context.get('avg_complexity', 0)}\n"
            )
        return "\n".join(parts)

    @staticmethod
    def _build_install_section(_project_name: str, context: Dict) -> str:
        """Build installation section from dependencies."""
        deps = context.get("dependencies")
        if not deps or not deps.install_command:
            return ""
        parts = ["## Installation\n", f"```bash\n{deps.install_command}\n```\n"]
        if deps.python_version:
            parts.append(f"Requires Python {deps.python_version}\n")
        return "\n".join(parts)

    @staticmethod
    def _build_quickstart_section(_project_name: str, context: Dict) -> str:
        """Build quick start section from entry points."""
        parts = ["## Quick Start\n"]
        entry_points = context.get("entry_points", [])
        if entry_points:
            parts.append("```python")
            parts.append(f"# Entry points: {', '.join(entry_points[:3])}")
            parts.append("```\n")
        return "\n".join(parts)

    @staticmethod
    def _build_api_section(_project_name: str, context: Dict) -> str:
        """Build API overview section with classes and functions."""
        parts = ["## API Overview\n"]
        for name, cls in list(context.get("public_classes", {}).items())[:20]:
            doc = f" — {cls.docstring.splitlines()[0]}" if cls.docstring else ""
            parts.append(f"- **`{cls.name}`**{doc}")
        parts.append("")
        for name, func in list(context.get("public_functions", {}).items())[:30]:
            args_str = ", ".join(func.args[:5])
            ret = f" → {func.returns}" if func.returns else ""
            parts.append(f"- `{func.name}({args_str}){ret}`")
        parts.append("")
        return "\n".join(parts)

    @staticmethod
    def _build_structure_section(_project_name: str, context: Dict) -> str:
        """Build project structure section from module tree."""
        tree = context.get("module_tree", "")
        if not tree:
            return ""
        return f"## Project Structure\n\n{tree}\n"

    @staticmethod
    def _build_endpoints_section(_project_name: str, context: Dict) -> str:
        """Build endpoints section from detected routes."""
        endpoints = context.get("endpoints", [])
        if not endpoints:
            return ""
        parts = [
            "## Endpoints\n",
            "| Method | Path | Function | Framework |",
            "|--------|------|----------|-----------|",
        ]
        for ep in endpoints:
            parts.append(f"| {ep.method} | `{ep.path}` | `{ep.function_name}` | {ep.framework} |")
        parts.append("")
        return "\n".join(parts)

    def write(self, path: str, content: str) -> None:
        """Write README, respecting sync markers if existing file has them."""
        readme_path = Path(path)

        if readme_path.exists():
            existing = readme_path.read_text(encoding="utf-8")
            if MARKER_START in existing and MARKER_END in existing:
                # Replace only between markers
                pattern = re.compile(
                    re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
                    re.DOTALL,
                )
                content = pattern.sub(content, existing)

        readme_path.parent.mkdir(parents=True, exist_ok=True)
        readme_path.write_text(content, encoding="utf-8")


def generate_readme(project_path: str = "./", output: str = "README.md",
                    sections: Optional[List[str]] = None, sync_markers: bool = True,
                    config: Optional[Code2DocsConfig] = None) -> str:
    """Convenience function to generate a README."""
    from ..analyzers.project_scanner import ProjectScanner

    config = config or Code2DocsConfig()
    if sections:
        config.readme.sections = sections
    config.readme.sync_markers = sync_markers

    scanner = ProjectScanner(config)
    result = scanner.analyze(project_path)

    gen = ReadmeGenerator(config, result)
    content = gen.generate()
    gen.write(output, content)
    return content
