
CONSTANT_3 = 3
CONSTANT_500 = 500

"""Registry adapters — wrap existing generators into BaseGenerator interface."""
from pathlib import Path
from typing import Optional
import click
from ..base import BaseGenerator, GenerateContext

class ReadmeGeneratorAdapter(BaseGenerator):
    name = 'readme'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return True

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .readme_gen import ReadmeGenerator
        gen = ReadmeGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            click.echo(f'\n--- README.md ({len(content)} chars) ---')
            preview = content[:500] + '...' if len(content) > 500 else content
            click.echo(preview)
            return None
        readme_output = Path(self.config.readme_output)
        if readme_output.parent == Path('.'):
            readme_path = ctx.docs_dir / readme_output.name
        else:
            readme_path = ctx.project / readme_output
        gen.write(str(readme_path), content)
        return f'✅ {readme_path.relative_to(ctx.project)}'

class ApiReferenceAdapter(BaseGenerator):
    name = 'api_reference'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only and self.config.docs.api_reference

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .api_reference_gen import ApiReferenceGenerator
        gen = ApiReferenceGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/api.md'
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / 'api.md').write_text(content, encoding='utf-8')
        return '✅ docs/api.md'

class ModuleDocsAdapter(BaseGenerator):
    name = 'module_docs'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only and self.config.docs.module_docs

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .module_docs_gen import ModuleDocsGenerator
        gen = ModuleDocsGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/modules.md'
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / 'modules.md').write_text(content, encoding='utf-8')
        return '✅ docs/modules.md'

class ArchitectureAdapter(BaseGenerator):
    name = 'architecture'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only and self.config.docs.architecture

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .architecture_gen import ArchitectureGenerator
        gen = ArchitectureGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/architecture.md'
        (ctx.docs_dir / 'architecture.md').write_text(content, encoding='utf-8')
        return '✅ docs/architecture.md'

class DepGraphAdapter(BaseGenerator):
    name = 'depgraph'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .depgraph_gen import DepGraphGenerator
        gen = DepGraphGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/dependency-graph.md'
        (ctx.docs_dir / 'dependency-graph.md').write_text(content, encoding='utf-8')
        return '✅ docs/dependency-graph.md'

class CoverageAdapter(BaseGenerator):
    name = 'coverage'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .coverage_gen import CoverageGenerator
        gen = CoverageGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/coverage.md'
        (ctx.docs_dir / 'coverage.md').write_text(content, encoding='utf-8')
        return '✅ docs/coverage.md'

class ApiChangelogAdapter(BaseGenerator):
    name = 'api_changelog'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .api_changelog_gen import ApiChangelogGenerator
        gen = ApiChangelogGenerator(self.config, self.result)
        content = gen.generate(str(ctx.project))
        if ctx.dry_run:
            return '[dry-run] docs/api-changelog.md'
        (ctx.docs_dir / 'api-changelog.md').write_text(content, encoding='utf-8')
        gen.save_snapshot(str(ctx.project))
        return '✅ docs/api-changelog.md'

class ExamplesAdapter(BaseGenerator):
    name = 'examples'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only and self.config.examples.auto_generate

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .examples_gen import ExamplesGenerator
        gen = ExamplesGenerator(self.config, self.result)
        files = gen.generate_all()
        if ctx.dry_run:
            return f'[dry-run] examples/ ({len(files)} files)'
        examples_dir = ctx.docs_dir / 'examples'
        gen.write_all(str(examples_dir), files)
        return f'✅ examples/ ({len(files)} files)'

class MkDocsAdapter(BaseGenerator):
    name = 'mkdocs'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .mkdocs_gen import MkDocsGenerator
        gen = MkDocsGenerator(self.config, self.result)
        content = gen.generate(str(ctx.docs_dir))
        if ctx.dry_run:
            return '[dry-run] mkdocs.yml'
        gen.write(str(ctx.docs_dir / 'mkdocs.yml'), content)
        return '✅ mkdocs.yml'

class GettingStartedAdapter(BaseGenerator):
    name = 'getting_started'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .getting_started_gen import GettingStartedGenerator
        gen = GettingStartedGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/getting-started.md'
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / 'getting-started.md').write_text(content, encoding='utf-8')
        return '✅ docs/getting-started.md'

class ConfigDocsAdapter(BaseGenerator):
    name = 'config_docs'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .config_docs_gen import ConfigDocsGenerator
        gen = ConfigDocsGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] docs/configuration.md'
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / 'configuration.md').write_text(content, encoding='utf-8')
        return '✅ docs/configuration.md'

class ContributingAdapter(BaseGenerator):
    name = 'contributing'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .contributing_gen import ContributingGenerator
        gen = ContributingGenerator(self.config, self.result)
        content = gen.generate()
        if ctx.dry_run:
            return '[dry-run] CONTRIBUTING.md'
        ctx.docs_dir.mkdir(parents=True, exist_ok=True)
        (ctx.docs_dir / 'CONTRIBUTING.md').write_text(content, encoding='utf-8')
        return '✅ CONTRIBUTING.md'

class Code2LlmAdapter(BaseGenerator):
    """Adapter for code2llm analysis generation."""
    name = 'code2llm'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .code2llm_gen import Code2LlmGenerator
        gen = Code2LlmGenerator(self.config, self.result)
        results = gen.generate_all()
        if ctx.dry_run:
            return '[dry-run] project/ (code2llm analysis)'
        files = [k for k in results.keys() if k != 'status' and (not k.startswith('['))]
        if files:
            return f"✅ project/ ({len(files)} files: {', '.join(files[:3])}{('...' if len(files) > 3 else '')})"
        return '⚠️ project/ (no files generated)'

class OrgReadmeAdapter(BaseGenerator):
    """Adapter for organization README generation."""
    name = 'org_readme'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return hasattr(self.config, 'org_name') and bool(self.config.org_name)

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .org_readme_gen import OrgReadmeGenerator
        org_name = getattr(self.config, 'org_name', '')
        if not org_name:
            return None
        gen = OrgReadmeGenerator(self.config, str(ctx.project), org_name)
        content = gen.generate()
        if ctx.dry_run:
            click.echo(f'\n--- {org_name} README ({len(content)} chars) ---')
            preview = content[:500] + '...' if len(content) > 500 else content
            click.echo(preview)
            return None
        readme_path = ctx.docs_dir / 'README.md'
        gen.write(str(readme_path), content)
        return f'✅ {readme_path.relative_to(ctx.project)}'

class IndexHtmlAdapter(BaseGenerator):
    """Adapter for generating index.html for GitHub Pages browsing."""
    name = 'index_html'

    def should_run(self, *, readme_only: bool=False) -> bool:
        return not readme_only

    def run(self, ctx: GenerateContext) -> Optional[str]:
        if ctx.dry_run:
            return '[dry-run] docs/index.html'
        content = self._generate_html(ctx)
        (ctx.docs_dir / 'index.html').write_text(content, encoding='utf-8')
        return '✅ docs/index.html'

    def _generate_html(self, ctx: GenerateContext) -> str:
        project_name = self.config.project_name or ctx.project.name
        files = self._collect_doc_files(ctx.docs_dir)
        github_link = self._build_github_link(self.config.repo_url)
        files_html = self._build_files_html(files)
        return self._build_html_template(project_name, github_link, files_html)

    def _collect_doc_files(self, docs_dir: Path) -> list:
        """Collect existing documentation files with their display info."""
        doc_files = [
            ('README.md', 'Project Overview', '📖'),
            ('getting-started.md', 'Getting Started', '🚀'),
            ('api.md', 'API Reference', '📚'),
            ('modules.md', 'Module Documentation', '📦'),
            ('architecture.md', 'Architecture', '🏗️'),
            ('dependency-graph.md', 'Dependency Graph', '🔗'),
            ('coverage.md', 'Code Coverage', '📊'),
            ('api-changelog.md', 'API Changelog', '📝'),
            ('configuration.md', 'Configuration', '⚙️'),
            ('CONTRIBUTING.md', 'Contributing Guide', '🤝'),
        ]
        files = [(href, title, icon) for href, title, icon in doc_files if (docs_dir / href).exists()]
        if (docs_dir / 'examples').is_dir():
            files.append(('examples/', 'Examples', '💡'))
        return files

    def _build_github_link(self, repo_url: str) -> str:
        """Build GitHub link HTML if repo_url is available."""
        if not repo_url:
            return ''
        return f'<a href="{repo_url}" class="github-link" target="_blank" rel="noopener">View on GitHub</a>'

    def _build_files_html(self, files: list) -> str:
        """Build HTML for file cards."""
        return '\n'.join(
            f'<a href="{href}" class="doc-card"><span class="icon">{icon}</span><span class="title">{title}</span></a>'
            for href, title, icon in files
        )

    def _build_html_template(self, project_name: str, github_link: str, files_html: str) -> str:
        return f'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>{project_name} - Documentation</title>\n    <style>\n        * {{ margin: 0; padding: 0; box-sizing: border-box; }}\n        body {{\n            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, sans-serif;\n            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);\n            min-height: 100vh;\n            padding: 40px 20px;\n        }}\n        .container {{\n            max-width: 900px;\n            margin: 0 auto;\n        }}\n        .header {{\n            text-align: center;\n            margin-bottom: 40px;\n            color: white;\n        }}\n        .header h1 {{\n            font-size: 2.5rem;\n            margin-bottom: 10px;\n            text-shadow: 0 2px 4px rgba(0,0,0,0.2);\n        }}\n        .header p {{\n            font-size: 1.1rem;\n            opacity: 0.9;\n        }}\n        .github-link {{\n            display: inline-block;\n            margin-top: 15px;\n            padding: 10px 20px;\n            background: rgba(255,255,255,0.2);\n            color: white;\n            text-decoration: none;\n            border-radius: 25px;\n            transition: background 0.3s;\n        }}\n        .github-link:hover {{ background: rgba(255,255,255,0.3); }}\n        .docs-grid {{\n            display: grid;\n            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));\n            gap: 20px;\n        }}\n        .doc-card {{\n            background: white;\n            border-radius: 12px;\n            padding: 25px;\n            text-decoration: none;\n            color: #333;\n            box-shadow: 0 4px 15px rgba(0,0,0,0.1);\n            transition: transform 0.2s, box-shadow 0.2s;\n            display: flex;\n            align-items: center;\n            gap: 15px;\n        }}\n        .doc-card:hover {{\n            transform: translateY(-3px);\n            box-shadow: 0 8px 25px rgba(0,0,0,0.15);\n        }}\n        .doc-card .icon {{\n            font-size: 2rem;\n            flex-shrink: 0;\n        }}\n        .doc-card .title {{\n            font-size: 1.1rem;\n            font-weight: 600;\n        }}\n        .footer {{\n            text-align: center;\n            margin-top: 40px;\n            color: rgba(255,255,255,0.7);\n            font-size: 0.9rem;\n        }}\n        @media (max-width: 600px) {{\n            .header h1 {{ font-size: 1.8rem; }}\n            .docs-grid {{ grid-template-columns: 1fr; }}\n        }}\n    </style>\n</head>\n<body>\n    <div class="container">\n        <div class="header">\n            <h1>{project_name}</h1>\n            <p>Generated Documentation</p>\n            {github_link}\n        </div>\n        <div class="docs-grid">\n            {files_html}\n        </div>\n        <div class="footer">\n            Generated with <a href="https://github.com/wronai/code2docs" style="color: rgba(255,255,255,0.9);">code2docs</a>\n        </div>\n    </div>\n</body>\n</html>'
ALL_ADAPTERS = [ReadmeGeneratorAdapter, ApiReferenceAdapter, ModuleDocsAdapter, ArchitectureAdapter, DepGraphAdapter, CoverageAdapter, ApiChangelogAdapter, ExamplesAdapter, GettingStartedAdapter, ConfigDocsAdapter, ContributingAdapter, MkDocsAdapter, Code2LlmAdapter, OrgReadmeAdapter, IndexHtmlAdapter]