"""MkDocs configuration generator — auto-generate mkdocs.yml from docs tree."""

from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


class MkDocsGenerator:
    """Generate mkdocs.yml from the docs/ directory structure."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self, docs_dir: Optional[str] = None) -> str:
        """Generate mkdocs.yml content."""
        project_name = self.config.project_name or "Project"
        nav = self._build_nav(docs_dir)

        # Read MkDocs config from pyproject.toml if available
        mkdocs_config = self._read_pyproject_mkdocs()

        data = {
            "site_name": f"{project_name} Documentation",
            "theme": mkdocs_config.get("theme", {"name": "material"}),
            "nav": nav,
            "markdown_extensions": mkdocs_config.get(
                "markdown_extensions",
                [
                    "admonition",
                    "pymdownx.highlight",
                    "pymdownx.superfences",
                    {
                        "pymdownx.superfences": {
                            "custom_fences": [
                                {
                                    "name": "mermaid",
                                    "class": "mermaid",
                                    "format": "!!python/name:pymdownx.superfences.fence_code_format",
                                }
                            ]
                        }
                    },
                ],
            ),
        }

        # Add extra fields from pyproject.toml if present
        for key in ["extra_css", "extra_javascript", "plugins", "copyright"]:
            if key in mkdocs_config:
                data[key] = mkdocs_config[key]

        return yaml.dump(data, default_flow_style=False, sort_keys=False)

    def _read_pyproject_mkdocs(self) -> Dict[str, Any]:
        """Read MkDocs configuration from [tool.mkdocs] in pyproject.toml."""
        project_path = Path(self.result.project_path)
        pyproject_path = project_path / "pyproject.toml"

        if not pyproject_path.exists():
            # Also check parent directory (for nested packages)
            pyproject_path = project_path.parent / "pyproject.toml"

        if not pyproject_path.exists():
            return {}

        try:
            import tomllib

            with open(pyproject_path, "rb") as f:
                data = tomllib.load(f)

            # Support both [tool.mkdocs] and [tool.poetry.plugins.mkdocs] formats
            tool_data = data.get("tool", {})
            mkdocs_data = tool_data.get("mkdocs", {})

            # Also check for poetry-style config
            if not mkdocs_data:
                poetry = tool_data.get("poetry", {})
                plugins = poetry.get("plugins", {})
                mkdocs_data = plugins.get("mkdocs", {})

            return mkdocs_data
        except Exception:
            return {}

    def _build_nav(self, docs_dir: Optional[str] = None) -> List:
        """Build navigation structure from docs tree and analysis."""
        nav: List = [{"Home": "index.md"}]

        if self.config.docs.architecture:
            nav.append({"Architecture": "architecture.md"})

        # API reference (single file)
        if self.config.docs.api_reference:
            nav.append({"API Reference": "api.md"})

        # Module docs (single file)
        if self.config.docs.module_docs:
            nav.append({"Modules": "modules.md"})

        # Extra pages
        nav.append({"Dependency Graph": "dependency-graph.md"})
        nav.append({"Coverage": "coverage.md"})

        if self.config.docs.changelog:
            nav.append({"Changelog": "changelog.md"})

        return nav

    def write(self, output_path: str, content: str) -> None:
        """Write mkdocs.yml file."""
        Path(output_path).write_text(content, encoding="utf-8")
