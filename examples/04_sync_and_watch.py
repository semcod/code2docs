"""Example 4: Sync and Watch - Keep docs in sync with code changes.

This example shows how to use the sync and watch features
to automatically update documentation when code changes.
"""

import time
from code2docs.sync.watcher import start_watcher
from code2docs.sync.differ import Differ, ChangeInfo
from code2docs.sync.updater import Updater
from code2docs.config import Code2DocsConfig


# =============================================================================
# DETECTING CHANGES
# =============================================================================


def detect_changes_example(project_path: str) -> ChangeInfo:
    """Detect what files have changed since last documentation generation."""
    differ = Differ(project_path)
    changes = differ.detect_changes()
    
    print(f"Changes detected:")
    print(f"  New files: {len(changes.new_files)}")
    for f in changes.new_files[:5]:  # Show first 5
        print(f"    - {f}")
    
    print(f"  Modified: {len(changes.modified)}")
    for f in changes.modified[:5]:
        print(f"    - {f}")
    
    print(f"  Deleted: {len(changes.deleted)}")
    for f in changes.deleted[:5]:
        print(f"    - {f}")
    
    return changes


# =============================================================================
# UPDATING DOCUMENTATION
# =============================================================================


def update_docs_incrementally(project_path: str) -> None:
    """Update only the parts of docs that need changing."""
    config = Code2DocsConfig(
        project_name="My Project",
        output_dir="docs",
        sync_markers=True,  # Enable sync markers for partial updates
    )
    
    differ = Differ(project_path)
    changes = differ.detect_changes()
    
    if not changes.has_changes:
        print("No changes to document")
        return
    
    updater = Updater(config=config)
    updater.apply(project_path=project_path, changes=changes)
    
    print("Documentation updated incrementally")


def force_full_regeneration(project_path: str) -> None:
    """Force full regeneration of all documentation."""
    config = Code2DocsConfig(
        project_name="My Project",
        output_dir="docs",
    )
    
    # Create empty changes to force full regeneration
    from code2docs.sync.differ import ChangeInfo
    changes = ChangeInfo(
        new_files=[], modified=[], deleted=[],
        has_changes=True  # Force update
    )
    
    updater = Updater(config=config)
    updater.apply(project_path=project_path, changes=changes)
    
    print("Full documentation regeneration complete")


# =============================================================================
# FILE WATCHER
# =============================================================================


def watch_and_auto_regenerate(project_path: str, interval: int = 5) -> None:
    """Watch for file changes and auto-regenerate documentation.
    
    Args:
        project_path: Path to watch
        interval: Check interval in seconds
    """
    config = Code2DocsConfig(
        project_name="My Project",
        output_dir="docs",
    )
    
    print(f"Starting watcher on {project_path}")
    print(f"Press Ctrl+C to stop")
    
    try:
        start_watcher(
            project_path=project_path,
            config=config,
            interval=interval
        )
    except KeyboardInterrupt:
        print("\nWatcher stopped")


# =============================================================================
# CUSTOM WATCHER WITH CALLBACKS
# =============================================================================


def custom_watcher_with_hooks(project_path: str) -> None:
    """Set up a custom watcher with pre/post generation hooks."""
    import os
    import signal
    
    config = Code2DocsConfig(project_name="My Project")
    running = True
    
    def on_change_detected(changes: ChangeInfo) -> None:
        """Called when changes are detected."""
        print(f"[{time.strftime('%H:%M:%S')}] Changes detected:")
        print(f"  New: {len(changes.new_files)}, "
              f"Modified: {len(changes.modified)}, "
              f"Deleted: {len(changes.deleted)}")
    
    def on_generation_start() -> None:
        """Called before documentation generation."""
        print("  -> Starting doc generation...")
    
    def on_generation_complete() -> None:
        """Called after documentation generation."""
        print("  -> Documentation updated!")
    
    def signal_handler(signum, frame):
        nonlocal running
        running = False
        print("\nShutting down...")
    
    signal.signal(signal.SIGINT, signal_handler)
    
    differ = Differ(project_path)
    updater = Updater(config=config)
    
    print(f"Custom watcher started on {project_path}")
    
    while running:
        changes = differ.detect_changes()
        
        if changes.has_changes:
            on_change_detected(changes)
            on_generation_start()
            updater.apply(project_path=project_path, changes=changes)
            on_generation_complete()
        
        time.sleep(5)  # Check every 5 seconds


# =============================================================================
# GIT INTEGRATION
# =============================================================================


def sync_with_git_changes(project_path: str) -> None:
    """Only regenerate docs for files changed in git."""
    import subprocess
    
    # Get list of changed files from git
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD"],
        capture_output=True,
        text=True,
        cwd=project_path
    )
    
    changed_files = result.stdout.strip().split("\n")
    python_files = [f for f in changed_files if f.endswith(".py")]
    
    if not python_files:
        print("No Python files changed")
        return
    
    print(f"Python files changed: {len(python_files)}")
    
    # Create partial change info
    changes = ChangeInfo(
        new_files=[],
        modified=python_files,
        deleted=[],
        has_changes=True
    )
    
    config = Code2DocsConfig()
    updater = Updater(config=config)
    updater.apply(project_path=project_path, changes=changes)


if __name__ == "__main__":
    # Example usage
    # detect_changes_example("./my_project")
    # update_docs_incrementally("./my_project")
    # watch_and_auto_regenerate("./my_project")
    pass
