"""CLI interface for code2docs."""

import sys
from pathlib import Path
from typing import Optional

import click

from .config import Code2DocsConfig


class DefaultGroup(click.Group):
    """Click Group that routes unknown subcommands to 'generate'."""

    def parse_args(self, ctx, args):
        if not args:
            args = ["generate"]
        elif args[0] not in self.commands and args[0] not in ("--help", "-h"):
            args = ["generate"] + args
        return super().parse_args(ctx, args)


@click.group(cls=DefaultGroup)
def main():
    """code2docs — Auto-generate project documentation from source code."""


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--readme-only", is_flag=True, help="Generate only README.md")
@click.option("--sections", "-s", default=None, help="Comma-separated sections to generate")
@click.option("--output", "-o", default=None, help="Output directory for docs")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.option("--dry-run", is_flag=True, help="Show what would be generated without writing")
def generate(project_path, config_path, readme_only, sections, output, verbose, dry_run):
    """Generate documentation (default command)."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True
    if output:
        config.output = output
    if sections:
        config.readme.sections = [s.strip() for s in sections.split(",")]

    _run_generate(project_path, config, readme_only=readme_only, dry_run=dry_run)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.option("--dry-run", is_flag=True, help="Show what would change without writing")
def sync(project_path, config_path, verbose, dry_run):
    """Synchronize documentation with source code changes."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True

    _run_sync(project_path, config, dry_run=dry_run)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def watch(project_path, config_path, verbose):
    """Watch for file changes and auto-regenerate docs."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True

    _run_watch(project_path, config)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--output", "-o", default="code2docs.yaml", help="Output config file path")
def init(project_path, output):
    """Initialize code2docs.yaml configuration file."""
    project_path = Path(project_path).resolve()
    config = Code2DocsConfig(
        project_name=project_path.name,
        source="./",
    )
    out_path = project_path / output
    config.to_yaml(str(out_path))
    click.echo(f"Created {out_path}")


def _load_config(project_path: str, config_path: Optional[str] = None) -> Code2DocsConfig:
    """Load configuration, auto-detecting code2docs.yaml if present."""
    project = Path(project_path).resolve()

    if config_path:
        return Code2DocsConfig.from_yaml(config_path)

    # Auto-detect
    for name in ("code2docs.yaml", "code2docs.yml"):
        candidate = project / name
        if candidate.exists():
            return Code2DocsConfig.from_yaml(str(candidate))

    # Defaults
    config = Code2DocsConfig(project_name=project.name, source="./")
    return config


def _run_generate(project_path: str, config: Code2DocsConfig,
                  readme_only: bool = False, dry_run: bool = False):
    """Run full documentation generation."""
    from .analyzers.project_scanner import ProjectScanner
    from .generators.readme_gen import ReadmeGenerator
    from .generators.api_reference_gen import ApiReferenceGenerator
    from .generators.module_docs_gen import ModuleDocsGenerator
    from .generators.examples_gen import ExamplesGenerator
    from .generators.architecture_gen import ArchitectureGenerator
    from .generators.depgraph_gen import DepGraphGenerator
    from .generators.coverage_gen import CoverageGenerator
    from .generators.mkdocs_gen import MkDocsGenerator
    from .generators.api_changelog_gen import ApiChangelogGenerator

    project = Path(project_path).resolve()
    click.echo(f"📖 code2docs: analyzing {project.name}...")

    # Step 1: Analyze
    scanner = ProjectScanner(config)
    result = scanner.analyze(str(project))

    if config.verbose:
        click.echo(f"  Functions: {len(result.functions)}")
        click.echo(f"  Classes: {len(result.classes)}")
        click.echo(f"  Modules: {len(result.modules)}")

    # Step 2: Generate README
    readme_gen = ReadmeGenerator(config, result)
    readme_content = readme_gen.generate()

    if dry_run:
        click.echo(f"\n--- README.md ({len(readme_content)} chars) ---")
        click.echo(readme_content[:500] + "..." if len(readme_content) > 500 else readme_content)
    else:
        readme_path = project / config.readme_output
        readme_gen.write(str(readme_path), readme_content)
        click.echo(f"  ✅ {readme_path.relative_to(project)}")

    if readme_only:
        return

    # Step 3: Generate docs/
    docs_dir = project / config.output
    docs_dir.mkdir(parents=True, exist_ok=True)

    if config.docs.api_reference:
        api_gen = ApiReferenceGenerator(config, result)
        files = api_gen.generate_all()
        if not dry_run:
            api_gen.write_all(str(docs_dir / "api"), files)
            click.echo(f"  ✅ docs/api/ ({len(files)} files)")
        else:
            click.echo(f"  [dry-run] docs/api/ ({len(files)} files)")

    if config.docs.module_docs:
        mod_gen = ModuleDocsGenerator(config, result)
        files = mod_gen.generate_all()
        if not dry_run:
            mod_gen.write_all(str(docs_dir / "modules"), files)
            click.echo(f"  ✅ docs/modules/ ({len(files)} files)")
        else:
            click.echo(f"  [dry-run] docs/modules/ ({len(files)} files)")

    if config.docs.architecture:
        arch_gen = ArchitectureGenerator(config, result)
        content = arch_gen.generate()
        if not dry_run:
            (docs_dir / "architecture.md").write_text(content, encoding="utf-8")
            click.echo(f"  ✅ docs/architecture.md")
        else:
            click.echo(f"  [dry-run] docs/architecture.md")

    # Step 4: Dependency graph
    depgraph_gen = DepGraphGenerator(config, result)
    content = depgraph_gen.generate()
    if not dry_run:
        (docs_dir / "dependency-graph.md").write_text(content, encoding="utf-8")
        click.echo(f"  ✅ docs/dependency-graph.md")
    else:
        click.echo(f"  [dry-run] docs/dependency-graph.md")

    # Step 5: Docstring coverage
    cov_gen = CoverageGenerator(config, result)
    content = cov_gen.generate()
    if not dry_run:
        (docs_dir / "coverage.md").write_text(content, encoding="utf-8")
        click.echo(f"  ✅ docs/coverage.md")
    else:
        click.echo(f"  [dry-run] docs/coverage.md")

    # Step 6: API changelog (diff with previous snapshot)
    api_cl_gen = ApiChangelogGenerator(config, result)
    content = api_cl_gen.generate(str(project))
    if not dry_run:
        (docs_dir / "api-changelog.md").write_text(content, encoding="utf-8")
        api_cl_gen.save_snapshot(str(project))
        click.echo(f"  ✅ docs/api-changelog.md")
    else:
        click.echo(f"  [dry-run] docs/api-changelog.md")

    # Step 7: Generate examples/
    if config.examples.auto_generate:
        ex_gen = ExamplesGenerator(config, result)
        files = ex_gen.generate_all()
        if not dry_run:
            examples_dir = project / "examples"
            ex_gen.write_all(str(examples_dir), files)
            click.echo(f"  ✅ examples/ ({len(files)} files)")
        else:
            click.echo(f"  [dry-run] examples/ ({len(files)} files)")

    # Step 8: mkdocs.yml
    mkdocs_gen = MkDocsGenerator(config, result)
    content = mkdocs_gen.generate(str(docs_dir))
    if not dry_run:
        mkdocs_gen.write(str(project / "mkdocs.yml"), content)
        click.echo(f"  ✅ mkdocs.yml")
    else:
        click.echo(f"  [dry-run] mkdocs.yml")

    click.echo("📖 Done!")


def _run_sync(project_path: str, config: Code2DocsConfig, dry_run: bool = False):
    """Run sync — regenerate only changed documentation."""
    from .sync.differ import Differ
    from .sync.updater import Updater

    project = Path(project_path).resolve()
    click.echo(f"🔄 code2docs sync: {project.name}...")

    differ = Differ(config)
    changes = differ.detect_changes(str(project))

    if not changes:
        click.echo("  No changes detected.")
        return

    click.echo(f"  Changes detected in {len(changes)} modules")

    if dry_run:
        for change in changes:
            click.echo(f"    - {change}")
        return

    updater = Updater(config)
    updater.apply(str(project), changes)
    click.echo("🔄 Sync complete!")


def _run_watch(project_path: str, config: Code2DocsConfig):
    """Run file watcher for auto-resync."""
    try:
        from .sync.watcher import start_watcher
    except ImportError:
        click.echo("Error: watchdog not installed. Install with: pip install code2docs[watch]")
        sys.exit(1)

    project = Path(project_path).resolve()
    click.echo(f"👁 Watching {project.name} for changes... (Ctrl+C to stop)")
    start_watcher(str(project), config)
