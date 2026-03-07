# `code2docs.cli`

> Source: `/home/tom/github/wronai/code2docs/code2docs/cli.py`

## Classes

### `DefaultGroup`

Inherits from: `click.Group`

Click Group that routes unknown subcommands to 'generate'.

#### Methods

- `parse_args(self, ctx, args)`

## Functions

### `_load_config(project_path, config_path)`

Load configuration, auto-detecting code2docs.yaml if present.

- Calls: `None.resolve`, `Code2DocsConfig`, `Code2DocsConfig.from_yaml`, `candidate.exists`, `Path`, `Code2DocsConfig.from_yaml`, `str`

### `_run_generate(project_path, config, readme_only, dry_run)`

Run full documentation generation.

- Calls: `None.resolve`, `click.echo`, `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `readme_gen.generate`, `docs_dir.mkdir`, `DepGraphGenerator`, `depgraph_gen.generate`, `CoverageGenerator`

### `_run_sync(project_path, config, dry_run)`

Run sync — regenerate only changed documentation.

- Calls: `None.resolve`, `click.echo`, `Differ`, `differ.detect_changes`, `click.echo`, `Updater`, `updater.apply`, `click.echo`, `str`, `click.echo`

### `_run_watch(project_path, config)`

Run file watcher for auto-resync.

- Calls: `None.resolve`, `click.echo`, `code2docs.sync.watcher.start_watcher`, `str`, `click.echo`, `sys.exit`, `Path`

### `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run)`

Generate documentation (default command).

- Calls: `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_generate`

### `init(project_path, output)`

Initialize code2docs.yaml configuration file.

- Calls: `main.command`, `click.argument`, `click.option`, `None.resolve`, `Code2DocsConfig`, `config.to_yaml`, `click.echo`, `str`, `click.Path`, `Path`

### `main()`

code2docs — Auto-generate project documentation from source code.

- Calls: `click.group`

### `sync(project_path, config_path, verbose, dry_run)`

Synchronize documentation with source code changes.

- Calls: `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_sync`, `click.Path`

### `watch(project_path, config_path, verbose)`

Watch for file changes and auto-regenerate docs.

- Calls: `main.command`, `click.argument`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_watch`, `click.Path`
