"""Basic usage of code2docs."""

from code2docs.sync.updater import Updater
from code2docs.formatters.markdown import MarkdownFormatter
from code2docs.generators.readme_gen import ReadmeGenerator
from code2docs.sync.differ import ChangeInfo
from code2docs.sync.differ import Differ
from code2docs.sync.watcher import start_watcher
from code2docs.formatters.badges import generate_badges
from code2docs.formatters.toc import generate_toc
from code2docs.formatters.toc import extract_headings
from code2docs.generators.readme_gen import generate_readme

# Create Updater instance
obj = Updater(config=...)

result = obj.apply(project_path=..., changes=...)

# Standalone functions
result = start_watcher(project_path=..., config=...)
result = generate_badges(project_name=..., badge_types=..., stats=..., deps=...)
result = generate_toc(markdown_content=..., max_depth=...)
result = extract_headings(content=..., max_depth=...)
result = generate_readme(project_path=..., output=..., sections=..., sync_markers=...)
