"""Configuration documentation generator."""

from dataclasses import fields, MISSING

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


class ConfigDocsGenerator:
    """Generate docs/configuration.md from Code2DocsConfig dataclass."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self) -> str:
        """Generate configuration.md content."""
        project = self.config.project_name or "Project"
        lines = [
            f"# {project} — Configuration Reference\n",
            "> All options for `code2docs.yaml`\n",
            self._render_section("Top-level", Code2DocsConfig),
        ]
        # Nested config sections
        for f in fields(Code2DocsConfig):
            val = getattr(self.config, f.name)
            if hasattr(val, "__dataclass_fields__"):
                lines.append("")
                lines.append(self._render_section(f"`{f.name}`", type(val)))
        lines.append("")
        lines.append(self._render_example())
        return "\n".join(lines)

    # Human-readable descriptions for known config fields
    _FIELD_DOCS = {
        "project_name": "Name of the project (used in headings and badges)",
        "source": "Root directory to analyze",
        "output": "Output directory for generated docs",
        "readme_output": "Path for the generated README file",
        "verbose": "Print detailed analysis info during generation",
        "exclude_tests": "Exclude test files from analysis",
        "skip_private": "Skip private functions/classes in output",
        "sections": "README sections to include",
        "badges": "Badge types to show in README header",
        "sync_markers": "Wrap generated content in `<!-- code2docs:start/end -->` markers",
        "api_reference": "Generate per-module API reference docs",
        "module_docs": "Generate detailed module documentation",
        "architecture": "Generate architecture overview with Mermaid diagrams",
        "changelog": "Generate changelog from git history",
        "auto_generate": "Auto-generate usage example files",
        "from_entry_points": "Generate examples from detected entry points",
        "strategy": "Sync strategy: `markers`, `full`, or `git-diff`",
        "watch": "Enable file watcher for auto-resync",
        "ignore": "Glob patterns to ignore during sync",
        "enabled": "Enable LLM-assisted documentation generation",
        "model": "LLM model identifier (litellm format, e.g. `openai/gpt-5.4-mini`, `ollama/llama3`)",
        "api_key": "API key for the LLM provider (use `.env` or env var `CODE2DOCS_LLM_API_KEY`)",
        "api_base": "Custom API base URL (for self-hosted or proxy endpoints)",
        "max_tokens": "Maximum tokens per LLM call",
        "temperature": "Sampling temperature (low = factual, high = creative)",
    }

    def _render_section(self, title: str, cls: type) -> str:
        """Render a dataclass as a Markdown table."""
        lines = [
            f"## {title}\n",
            "| Option | Type | Default | Description |",
            "|--------|------|---------|-------------|",
        ]
        # Get actual defaults from current config instance
        for f in fields(cls):
            type_str = getattr(f.type, "__name__", str(f.type))
            # Clean up type display
            type_str = type_str.replace("typing.", "")
            # Resolve actual default value
            if f.default is not MISSING:
                default = f.default
            elif f.default_factory is not MISSING:
                default = f.default_factory()
            else:
                default = "—"
            # Format default for display
            if isinstance(default, list):
                default = ", ".join(str(x) for x in default) if default else "[]"
            elif isinstance(default, bool):
                default = str(default).lower()
            elif hasattr(default, "__dataclass_fields__"):
                default = f"*see `{f.name}` section*"
            default_str = str(default) if default != "" else '""'
            doc = self._FIELD_DOCS.get(f.name, "")
            lines.append(f"| `{f.name}` | `{type_str}` | {default_str} | {doc} |")
        return "\n".join(lines)

    def _render_example(self) -> str:
        """Render an example code2docs.yaml."""
        lines = [
            "## Example `code2docs.yaml`\n",
            "```yaml",
            f"project_name: {self.config.project_name or 'my-project'}",
            f"source: {self.config.source}",
            f"output: {self.config.output}",
            f"readme_output: {self.config.readme_output}",
            "verbose: false",
            "",
            "readme:",
            "  sections:",
            "    - overview",
            "    - install",
            "    - quickstart",
            "    - api",
            "    - structure",
            "  sync_markers: true",
            "",
            "docs:",
            f"  api_reference: {self.config.docs.api_reference}",
            f"  module_docs: {self.config.docs.module_docs}",
            f"  architecture: {self.config.docs.architecture}",
            "",
            "examples:",
            f"  auto_generate: {self.config.examples.auto_generate}",
            "```",
        ]
        return "\n".join(lines)
