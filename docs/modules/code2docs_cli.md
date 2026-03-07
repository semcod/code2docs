# code2docs.cli

> Source: `/home/tom/github/wronai/code2docs/code2docs/cli.py` | 269 lines

## Overview

CLI interface for code2docs.

## Classes

### DefaultGroup

*Bases:* `click.Group`

Click Group that routes unknown subcommands to 'generate'.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `parse_args` | `self, ctx, args` | `—` | — |

## Functions

### `main()`

code2docs — Auto-generate project documentation from source code.

**Calls:** `click.group`

### `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run)`

Generate documentation (default command).

**Calls:** `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_generate`

### `sync(project_path, config_path, verbose, dry_run)`

Synchronize documentation with source code changes.

**Calls:** `main.command`, `click.argument`, `click.option`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_sync`, `click.Path`

### `watch(project_path, config_path, verbose)`

Watch for file changes and auto-regenerate docs.

**Calls:** `main.command`, `click.argument`, `click.option`, `click.option`, `code2docs.cli._load_config`, `code2docs.cli._run_watch`, `click.Path`

### `init(project_path, output)`

Initialize code2docs.yaml configuration file.

**Calls:** `main.command`, `click.argument`, `click.option`, `None.resolve`, `Code2DocsConfig`, `config.to_yaml`, `click.echo`, `str`, `click.Path`, `Path`

### `_load_config(project_path, config_path)`

Load configuration, auto-detecting code2docs.yaml if present.

**Calls:** `None.resolve`, `Code2DocsConfig`, `Code2DocsConfig.from_yaml`, `candidate.exists`, `Path`, `Code2DocsConfig.from_yaml`, `str`

**Called by:** `code2docs.cli.generate`, `code2docs.cli.sync`, `code2docs.cli.watch`, `code2docs.cli.generate`, `code2docs.cli.sync`, `code2docs.cli.watch`

### `_run_generate(project_path, config, readme_only, dry_run)`

Run full documentation generation.

**Calls:** `None.resolve`, `click.echo`, `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `readme_gen.generate`, `docs_dir.mkdir`, `DepGraphGenerator`, `depgraph_gen.generate`, `CoverageGenerator`

**Called by:** `code2docs.cli.generate`, `code2docs.cli.generate`

### `_run_sync(project_path, config, dry_run)`

Run sync — regenerate only changed documentation.

**Calls:** `None.resolve`, `click.echo`, `Differ`, `differ.detect_changes`, `click.echo`, `Updater`, `updater.apply`, `click.echo`, `str`, `click.echo`

**Called by:** `code2docs.cli.sync`, `code2docs.cli.sync`

### `_run_watch(project_path, config)`

Run file watcher for auto-resync.

**Calls:** `None.resolve`, `click.echo`, `code2docs.sync.watcher.start_watcher`, `str`, `click.echo`, `sys.exit`, `Path`

**Called by:** `code2docs.cli.watch`, `code2docs.cli.watch`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 269 |
| Functions | 10 |
| Classes | 1 |
| Fan-in | 12 |
| Fan-out | 147 |
