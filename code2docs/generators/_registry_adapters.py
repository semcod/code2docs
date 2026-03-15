"""Registry adapters — wrap existing generators into BaseGenerator interface."""

from pathlib import Path
from typing import Optional

import click

from ..base import BaseGenerator, GenerateContext
from ..config import Code2DocsConfig
from code2llm.api import AnalysisResult


class ReadmeGeneratorAdapter(BaseGenerator):
    name = "readme"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return True

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .readme_gen import ReadmeGenerator
        gen = ReadmeGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            click.echo(f"\n--- README.md ({len(content)} chars) ---")
            preview = content[:500] + "..." if len(content) > 500 else content
            click.echo(preview)
            return None
        # Use docs_dir if readme_output is a simple filename, otherwise respect the path
        readme_output = Path(self.config.readme_output)
        if readme_output.parent == Path("."):
            readme_path = ctx.docs_dir / readme_output.name
        else:
            readme_path = ctx.project / readme_output
        gen.write(str(readme_path), content)
        return f"✅ {readme_path.relative_to(ctx.project)}"


class ApiReferenceAdapter(BaseGenerator):
    name = "api_reference"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only and self.config.docs.api_reference

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .api_reference_gen import ApiReferenceGenerator
        gen = ApiReferenceGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/api.md"
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / "api.md").write_text(content, encoding="utf-8")
        return "✅ docs/api.md"


class ModuleDocsAdapter(BaseGenerator):
    name = "module_docs"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only and self.config.docs.module_docs

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .module_docs_gen import ModuleDocsGenerator
        gen = ModuleDocsGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/modules.md"
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / "modules.md").write_text(content, encoding="utf-8")
        return "✅ docs/modules.md"


class ArchitectureAdapter(BaseGenerator):
    name = "architecture"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only and self.config.docs.architecture

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .architecture_gen import ArchitectureGenerator
        gen = ArchitectureGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/architecture.md"
        (ctx.docs_dir / "architecture.md").write_text(content, encoding="utf-8")
        return "✅ docs/architecture.md"


class DepGraphAdapter(BaseGenerator):
    name = "depgraph"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .depgraph_gen import DepGraphGenerator
        gen = DepGraphGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/dependency-graph.md"
        (ctx.docs_dir / "dependency-graph.md").write_text(content, encoding="utf-8")
        return "✅ docs/dependency-graph.md"


class CoverageAdapter(BaseGenerator):
    name = "coverage"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .coverage_gen import CoverageGenerator
        gen = CoverageGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/coverage.md"
        (ctx.docs_dir / "coverage.md").write_text(content, encoding="utf-8")
        return "✅ docs/coverage.md"


class ApiChangelogAdapter(BaseGenerator):
    name = "api_changelog"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .api_changelog_gen import ApiChangelogGenerator
        gen = ApiChangelogGenerator(self.config, self.result)
        content = gen.generate(str(ctx.project))
        if ctx.dry_run:
            return "[dry-run] docs/api-changelog.md"
        (ctx.docs_dir / "api-changelog.md").write_text(content, encoding="utf-8")
        gen.save_snapshot(str(ctx.project))
        return "✅ docs/api-changelog.md"


class ExamplesAdapter(BaseGenerator):
    name = "examples"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only and self.config.examples.auto_generate

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .examples_gen import ExamplesGenerator
        gen = ExamplesGenerator(self.config, self.result)
        files = gen.generate_all()
        if ctx.dry_run:
            return f"[dry-run] examples/ ({len(files)} files)"
        examples_dir = ctx.docs_dir / "examples"
        gen.write_all(str(examples_dir), files)
        return f"✅ examples/ ({len(files)} files)"


class MkDocsAdapter(BaseGenerator):
    name = "mkdocs"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .mkdocs_gen import MkDocsGenerator
        gen = MkDocsGenerator(self.config, self.result)
        content = gen.generate(str(ctx.docs_dir))
        if ctx.dry_run:
            return "[dry-run] mkdocs.yml"
        gen.write(str(ctx.docs_dir / "mkdocs.yml"), content)
        return "✅ mkdocs.yml"


class GettingStartedAdapter(BaseGenerator):
    name = "getting_started"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .getting_started_gen import GettingStartedGenerator
        gen = GettingStartedGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/getting-started.md"
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / "getting-started.md").write_text(content, encoding="utf-8")
        return "✅ docs/getting-started.md"


class ConfigDocsAdapter(BaseGenerator):
    name = "config_docs"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .config_docs_gen import ConfigDocsGenerator
        gen = ConfigDocsGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] docs/configuration.md"
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / "configuration.md").write_text(content, encoding="utf-8")
        return "✅ docs/configuration.md"


class ContributingAdapter(BaseGenerator):
    name = "contributing"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .contributing_gen import ContributingGenerator
        gen = ContributingGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return "[dry-run] CONTRIBUTING.md"
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / "CONTRIBUTING.md").write_text(content, encoding="utf-8")
        return "✅ CONTRIBUTING.md"


class Code2LlmAdapter(BaseGenerator):
    """Adapter for code2llm analysis generation."""
    name = "code2llm"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .code2llm_gen import Code2LlmGenerator
        gen = Code2LlmGenerator(self.config, self.result)
        results = gen.generate_all()
        
        if ctx.dry_run:
            return "[dry-run] project/ (code2llm analysis)"
        
        # Report what was generated
        files = [k for k in results.keys() if k != "status" and not k.startswith("[")]
        if files:
            return f"✅ project/ ({len(files)} files: {', '.join(files[:3])}{'...' if len(files) > 3 else ''})"
        return "⚠️ project/ (no files generated)"


class OrgReadmeAdapter(BaseGenerator):
    """Adapter for organization README generation."""
    name = "org_readme"

    def should_run(self, *, readme_only: bool = False) -> bool:
        # Only run if org_name is set in config
        return hasattr(self.config, 'org_name') and bool(self.config.org_name)

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .org_readme_gen import OrgReadmeGenerator

        org_name = getattr(self.config, 'org_name', '')
        if not org_name:
            return None

        gen = OrgReadmeGenerator(self.config, str(ctx.project), org_name)
        content = gen.generate()

        if ctx.dry_run:
            click.echo(f"\n--- {org_name} README ({len(content)} chars) ---")
            preview = content[:500] + "..." if len(content) > 500 else content
            click.echo(preview)
            return None

        readme_path = ctx.docs_dir / "README.md"
        gen.write(str(readme_path), content)
        return f"✅ {readme_path.relative_to(ctx.project)}"


class IndexHtmlAdapter(BaseGenerator):
    """Adapter for generating index.html for GitHub Pages browsing."""
    name = "index_html"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        if ctx.dry_run:
            return "[dry-run] docs/index.html"

        content = self._generate_html(ctx)
        (ctx.docs_dir / "index.html").write_text(content, encoding="utf-8")
        return "✅ docs/index.html"

    def _generate_html(self, ctx: GenerateContext) -> str:
        project_name = self.config.project_name or ctx.project.name
        repo_url = self.config.repo_url

        files = []
        if (ctx.docs_dir / "README.md").exists():
            files.append(("README.md", "Project Overview", "📖"))
        if (ctx.docs_dir / "getting-started.md").exists():
            files.append(("getting-started.md", "Getting Started", "🚀"))
        if (ctx.docs_dir / "api.md").exists():
            files.append(("api.md", "API Reference", "📚"))
        if (ctx.docs_dir / "modules.md").exists():
            files.append(("modules.md", "Module Documentation", "📦"))
        if (ctx.docs_dir / "architecture.md").exists():
            files.append(("architecture.md", "Architecture", "🏗️"))
        if (ctx.docs_dir / "dependency-graph.md").exists():
            files.append(("dependency-graph.md", "Dependency Graph", "🔗"))
        if (ctx.docs_dir / "coverage.md").exists():
            files.append(("coverage.md", "Code Coverage", "📊"))
        if (ctx.docs_dir / "api-changelog.md").exists():
            files.append(("api-changelog.md", "API Changelog", "📝"))
        if (ctx.docs_dir / "configuration.md").exists():
            files.append(("configuration.md", "Configuration", "⚙️"))
        if (ctx.docs_dir / "CONTRIBUTING.md").exists():
            files.append(("CONTRIBUTING.md", "Contributing Guide", "🤝"))
        if (ctx.docs_dir / "examples").is_dir():
            files.append(("examples/", "Examples", "💡"))

        github_link = f'<a href="{repo_url}" class="github-link" target="_blank" rel="noopener">View on GitHub</a>' if repo_url else ""

        files_html = "\n".join(
            f'<a href="{href}" class="doc-card"><span class="icon">{icon}</span><span class="title">{title}</span></a>'
            for href, title, icon in files
        )

        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name} - Documentation</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            color: white;
        }}
        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
        .header p {{
            font-size: 1.1rem;
            opacity: 0.9;
        }}
        .github-link {{
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: rgba(255,255,255,0.2);
            color: white;
            text-decoration: none;
            border-radius: 25px;
            transition: background 0.3s;
        }}
        .github-link:hover {{ background: rgba(255,255,255,0.3); }}
        .docs-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }}
        .doc-card {{
            background: white;
            border-radius: 12px;
            padding: 25px;
            text-decoration: none;
            color: #333;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        .doc-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }}
        .doc-card .icon {{
            font-size: 2rem;
            flex-shrink: 0;
        }}
        .doc-card .title {{
            font-size: 1.1rem;
            font-weight: 600;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            color: rgba(255,255,255,0.7);
            font-size: 0.9rem;
        }}
        @media (max-width: 600px) {{
            .header h1 {{ font-size: 1.8rem; }}
            .docs-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{project_name}</h1>
            <p>Generated Documentation</p>
            {github_link}
        </div>
        <div class="docs-grid">
            {files_html}
        </div>
        <div class="footer">
            Generated with <a href="https://github.com/wronai/code2docs" style="color: rgba(255,255,255,0.9);">code2docs</a>
        </div>
    </div>
</body>
</html>'''



ALL_ADAPTERS = [
    ReadmeGeneratorAdapter,
    ApiReferenceAdapter,
    ModuleDocsAdapter,
    ArchitectureAdapter,
    DepGraphAdapter,
    CoverageAdapter,
    ApiChangelogAdapter,
    ExamplesAdapter,
    GettingStartedAdapter,
    ConfigDocsAdapter,
    ContributingAdapter,
    MkDocsAdapter,
    Code2LlmAdapter,
    OrgReadmeAdapter,
    IndexHtmlAdapter,
]
