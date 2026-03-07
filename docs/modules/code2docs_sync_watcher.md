# code2docs.sync.watcher

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/watcher.py` | 75 lines

## Overview

File watcher for auto-resync on source changes (requires watchdog).

## Functions

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

**Calls:** `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`

**Called by:** `code2docs.cli._run_watch`, `code2docs.cli._run_watch`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 75 |
| Functions | 1 |
| Classes | 0 |
| Fan-in | 2 |
| Fan-out | 29 |
