# `code2docs.sync.watcher`

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/watcher.py`

## Functions

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

- Calls: `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`
