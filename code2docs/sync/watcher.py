"""File watcher for auto-resync on source changes (requires watchdog)."""

import time
from pathlib import Path
from typing import Optional

from ..config import Code2DocsConfig


def start_watcher(project_path: str, config: Optional[Code2DocsConfig] = None) -> None:
    """Start watching project for file changes and auto-resync docs.

    Requires watchdog package: pip install code2docs[watch]
    """
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler, FileModifiedEvent
    except ImportError:
        raise ImportError(
            "watchdog is required for watch mode. Install with: pip install code2docs[watch]"
        )

    config = config or Code2DocsConfig()
    project = Path(project_path).resolve()

    class DocsHandler(FileSystemEventHandler):
        """Handler that triggers resync on Python file changes."""

        def __init__(self):
            self._last_trigger = 0.0
            self._debounce_seconds = 2.0

        def on_modified(self, event):
            if not event.src_path.endswith(".py"):
                return

            # Check ignore patterns
            rel = str(Path(event.src_path).relative_to(project))
            for pattern in config.sync.ignore:
                if pattern.rstrip("/") in rel:
                    return

            # Debounce
            now = time.time()
            if now - self._last_trigger < self._debounce_seconds:
                return
            self._last_trigger = now

            print(f"  Change detected: {rel}")
            try:
                from .differ import Differ
                from .updater import Updater

                differ = Differ(config)
                changes = differ.detect_changes(str(project))
                if changes:
                    print(f"  Regenerating {len(changes)} changed modules...")
                    updater = Updater(config)
                    updater.apply(str(project), changes)
                    print("  Done.")
            except Exception as e:
                print(f"  Error during resync: {e}")

    handler = DocsHandler()
    observer = Observer()
    observer.schedule(handler, str(project), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
