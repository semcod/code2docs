"""Entry point examples for code2docs."""

from code2docs import __getattr__

# Call entry point: __getattr__
# Lazy import heavy modules on first access.
result = __getattr__(name=...)

from code2docs.sync.updater import __init__

# Call entry point: __init__
result = __init__(self=..., config=...)

from code2docs.sync.updater import apply

# Call entry point: apply
# Regenerate documentation for changed modules.
result = apply(self=..., project_path=..., changes=...)

from code2docs.formatters.markdown import __init__

# Call entry point: __init__
result = __init__(self=...)

from code2docs.formatters.markdown import heading

# Call entry point: heading
# Add a heading.
result = heading(self=..., text=..., level=...)
