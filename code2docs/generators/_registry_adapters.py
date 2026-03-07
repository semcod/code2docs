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
        files = gen.generate_all()
        if ctx.dry_run:
            return f"[dry-run] docs/api/ ({len(files)} files)"
        gen.write_all(str(ctx.docs_dir / "api"), files)
        return f"✅ docs/api/ ({len(files)} files)"


class ModuleDocsAdapter(BaseGenerator):
    name = "module_docs"

    def should_run(self, *, readme_only: bool = False) -> bool:
        return not readme_only and self.config.docs.module_docs

    def run(self, ctx: GenerateContext) -> Optional[str]:
        from .module_docs_gen import ModuleDocsGenerator
        gen = ModuleDocsGenerator(self.config, self.result)
        files = gen.generate_all()
        if ctx.dry_run:
            return f"[dry-run] docs/modules/ ({len(files)} files)"
        gen.write_all(str(ctx.docs_dir / "modules"), files)
        return f"✅ docs/modules/ ({len(files)} files)"


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


ALL_ADAPTERS = [
    ReadmeGeneratorAdapter,
    ApiReferenceAdapter,
    ModuleDocsAdapter,
    ArchitectureAdapter,
    DepGraphAdapter,
    CoverageAdapter,
    ApiChangelogAdapter,
    ExamplesAdapter,
    MkDocsAdapter,
]
