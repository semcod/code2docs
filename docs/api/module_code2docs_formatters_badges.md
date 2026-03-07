# `code2docs.formatters.badges`

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/badges.py`

## Functions

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

- Calls: `quote`, `quote`, `hasattr`, `stats.get`

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

- Calls: `None.join`, `code2docs.formatters.badges._make_badge`, `badges.append`
