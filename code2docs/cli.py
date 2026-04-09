"""CLI interface for code2docs."""
import sys
from pathlib import Path
from typing import Optional
import click
from rich.console import Console
from rich.table import Table
from .config import Code2DocsConfig

console = Console()


class DefaultGroup(click.Group):
    """Click Group that routes unknown subcommands to 'generate'."""

    def parse_args(self, ctx, args):
        if not args:
            args = ['generate']
        elif args[0] not in self.commands and args[0] not in ('--help', '-h'):
            args = ['generate'] + args
        return super().parse_args(ctx, args)

@click.group(cls=DefaultGroup)
def main() -> None:
    """code2docs — Auto-generate project documentation from source code."""

@main.command()
@click.argument('project_path', default='.', type=click.Path(exists=True))
@click.option('--config', '-c', 'config_path', default=None, help='Path to code2docs.yaml')
@click.option('--readme-only', is_flag=True, help='Generate only README.md')
@click.option('--sections', '-s', default=None, help='Comma-separated sections to generate')
@click.option('--output', '-o', default=None, help='Output directory for docs')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--dry-run', is_flag=True, help='Show what would be generated without writing')
@click.option('--llm', 'llm_model', default=None, help='Enable LLM-assisted generation (e.g. openai/gpt-5.4-mini, ollama/llama3)')
@click.option('--org-name', default=None, help='Organization name for org-mode README generation')
def generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model, org_name) -> None:
    """Generate documentation (default command)."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True
    if output:
        config.output = output
    if sections:
        config.readme.sections = [s.strip() for s in sections.split(',')]
    if llm_model:
        config.llm.enabled = True
        config.llm.model = llm_model
    if org_name:
        config.org_name = org_name
    _run_generate(project_path, config, readme_only=readme_only, dry_run=dry_run)

@main.command()
@click.argument('project_path', default='.', type=click.Path(exists=True))
@click.option('--config', '-c', 'config_path', default=None, help='Path to code2docs.yaml')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
@click.option('--dry-run', is_flag=True, help='Show what would change without writing')
def sync(project_path, config_path, verbose, dry_run) -> None:
    """Synchronize documentation with source code changes."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True
    _run_sync(project_path, config, dry_run=dry_run)

@main.command()
@click.argument('project_path', default='.', type=click.Path(exists=True))
@click.option('--config', '-c', 'config_path', default=None, help='Path to code2docs.yaml')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def watch(project_path, config_path, verbose) -> None:
    """Watch for file changes and auto-regenerate docs."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True
    _run_watch(project_path, config)

@main.command()
@click.argument('project_path', default='.', type=click.Path(exists=True))
@click.option('--output', '-o', default='code2docs.yaml', help='Output config file path')
def init(project_path, output) -> None:
    """Initialize code2docs.yaml configuration file."""
    project_path = Path(project_path).resolve()
    config = Code2DocsConfig(project_name=project_path.name, source='./')
    out_path = project_path / output
    config.to_yaml(str(out_path))
    click.echo(f'Created {out_path}')

@main.command()
@click.argument('project_path', default='.', type=click.Path(exists=True))
@click.option('--config', '-c', 'config_path', default=None, help='Path to code2docs.yaml')
@click.option('--target', '-t', default=80, type=int, help='Docstring coverage target (%)')
def check(project_path, config_path, target) -> None:
    """Health check — verify documentation completeness."""
    config = _load_config(project_path, config_path)
    _run_check(project_path, config, target)

@main.command()
@click.argument('project_path', default='.', type=click.Path(exists=True))
@click.option('--config', '-c', 'config_path', default=None, help='Path to code2docs.yaml')
def diff(project_path, config_path) -> None:
    """Preview what would change without writing anything."""
    config = _load_config(project_path, config_path)
    _run_diff(project_path, config)

def _load_config(project_path: str, config_path: Optional[str]=None) -> Code2DocsConfig:
    """Load configuration, auto-detecting code2docs.yaml if present."""
    project = Path(project_path).resolve()
    if config_path:
        return Code2DocsConfig.from_yaml(config_path)
    for name in ('code2docs.yaml', 'code2docs.yml'):
        candidate = project / name
        if candidate.exists():
            return Code2DocsConfig.from_yaml(str(candidate))
    config = Code2DocsConfig(project_name=project.name, source='./')
    return config

def _run_generate(project_path: str, config: Code2DocsConfig, readme_only: bool=False, dry_run: bool=False) -> None:
    """Run full documentation generation via the generator registry."""
    from .analyzers.project_scanner import ProjectScanner
    from .base import GenerateContext
    from .registry import GeneratorRegistry
    from .generators._registry_adapters import ALL_ADAPTERS
    project = Path(project_path).resolve()
    console.print(f'[bold blue]📖 code2docs[/] analyzing [bold]{project.name}[/]...')
    if config.llm.enabled:
        console.print(f'  [cyan]🤖 LLM enabled:[/] {config.llm.model}')
    elif config.verbose:
        console.print('  [dim]ℹ️  LLM disabled — using algorithm-based generation[/]')
    with console.status('[bold green]Analyzing source code...') as status:
        scanner = ProjectScanner(config)
        result = scanner.analyze(str(project))
    if config.verbose:
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_row('Functions', f'[green]{len(result.functions)}[/]')
        table.add_row('Classes', f'[green]{len(result.classes)}[/]')
        table.add_row('Modules', f'[green]{len(result.modules)}[/]')
        console.print(table)
    docs_dir = project / config.output
    if not dry_run and (not readme_only):
        docs_dir.mkdir(parents=True, exist_ok=True)
    ctx = GenerateContext(project=project, docs_dir=docs_dir, dry_run=dry_run, verbose=config.verbose)
    registry = GeneratorRegistry()
    for adapter_cls in ALL_ADAPTERS:
        registry.add(adapter_cls(config, result))
    registry.run_all(ctx, readme_only=readme_only)
    console.print('[bold green]✨ Done![/]')

def _run_sync(project_path: str, config: Code2DocsConfig, dry_run: bool=False) -> None:
    """Run sync — regenerate only changed documentation."""
    from .sync.differ import Differ
    from .sync.updater import Updater
    project = Path(project_path).resolve()
    console.print(f'[bold blue]🔄 code2docs sync:[/] {project.name}...')
    differ = Differ(config)
    changes = differ.detect_changes(str(project))
    if not changes:
        console.print('  [green]No changes detected.[/]')
        return
    console.print(f'  [yellow]Changes detected in {len(changes)} modules[/]')
    if dry_run:
        for change in changes:
            console.print(f'    [dim]-[/] {change}')
        return
    updater = Updater(config)
    updater.apply(str(project), changes)
    console.print('[bold green]🔄 Sync complete![/]')

def _run_watch(project_path: str, config: Code2DocsConfig) -> None:
    """Run file watcher for auto-resync."""
    try:
        from .sync.watcher import start_watcher
    except ImportError:
        console.print('[red]Error:[/] watchdog not installed. Install with: [bold]pip install code2docs\\[watch][/]')
        sys.exit(1)
    project = Path(project_path).resolve()
    console.print(f'[bold blue]👁 Watching[/] {project.name} for changes... [dim](Ctrl+C to stop)[/]')
    start_watcher(str(project), config)

def _run_check(project_path: str, config: Code2DocsConfig, target: int=80) -> None:
    """Run documentation health check."""
    from .analyzers.project_scanner import ProjectScanner
    from .analyzers.docstring_extractor import DocstringExtractor
    project = Path(project_path).resolve()
    console.print(f'[bold blue]🩺 code2docs check:[/] {project.name}\n')
    with console.status('[bold green]Analyzing...'):
        scanner = ProjectScanner(config)
        result = scanner.analyze(str(project))
    table = Table(title='Documentation Health', show_lines=True)
    table.add_column('Check', style='bold')
    table.add_column('Status')
    table.add_column('Details', style='dim')
    score = 0
    total = 0
    total += 1
    readme = project / config.readme_output
    if readme.exists():
        table.add_row('README.md', '[green]✅ exists[/]', f'{readme.stat().st_size} bytes')
        score += 1
    else:
        table.add_row('README.md', '[red]❌ missing[/]', '')
    docs_dir = project / config.output
    for name, label in [('api.md', 'API reference'), ('modules.md', 'Module docs')]:
        total += 1
        f = docs_dir / name
        if f.exists():
            lines = len(f.read_text(encoding='utf-8').splitlines())
            table.add_row(label, '[green]✅ exists[/]', f'{lines} lines')
            score += 1
        else:
            table.add_row(label, '[red]❌ missing[/]', '')
    total += 1
    ex_dir = project / 'examples'
    if ex_dir.exists() and any(ex_dir.iterdir()):
        count = sum((1 for f in ex_dir.glob('*.py')))
        table.add_row('examples/', '[green]✅ exists[/]', f'{count} files')
        score += 1
    else:
        table.add_row('examples/', '[red]❌ missing[/]', '')
    total += 1
    extractor = DocstringExtractor()
    report = extractor.coverage_report(result)
    coverage = report.get('overall_coverage', 0)
    style = 'green' if coverage >= target else 'yellow'
    icon = '✅' if coverage >= target else '⚠️'
    table.add_row('Docstring coverage', f'[{style}]{icon} {coverage:.0f}%[/]', f'target: {target}%')
    if coverage >= target:
        score += 1
    console.print(table)
    console.print(f'\n  [bold]Score: {score}/{total}[/]')

def _run_diff(project_path: str, config: Code2DocsConfig) -> None:
    """Preview documentation changes without writing."""
    from .analyzers.project_scanner import ProjectScanner
    from .base import GenerateContext
    from .registry import GeneratorRegistry
    from .generators._registry_adapters import ALL_ADAPTERS
    project = Path(project_path).resolve()
    console.print(f'[bold blue]🔍 code2docs diff:[/] {project.name}\n')
    scanner = ProjectScanner(config)
    result = scanner.analyze(str(project))
    docs_dir = project / config.output
    ctx = GenerateContext(project=project, docs_dir=docs_dir, dry_run=True)
    registry = GeneratorRegistry()
    for adapter_cls in ALL_ADAPTERS:
        registry.add(adapter_cls(config, result))
    registry.run_all(ctx)