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
        readme_path = ctx.project / self.config.readme_output
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
        examples_dir = ctx.project / "examples"
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
        gen.write(str(ctx.project / "mkdocs.yml"), content)
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
        (ctx.project / "CONTRIBUTING.md").write_text(content, encoding="utf-8")
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
]
