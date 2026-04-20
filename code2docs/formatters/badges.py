"""Badge generation using shields.io URLs."""

from typing import Dict, List, Optional
from urllib.parse import quote


def generate_badges(project_name: str, badge_types: List[str],
                    stats: Dict = None, deps=None) -> str:
    """Generate shields.io badge Markdown strings."""
    stats = stats or {}
    badges: List[str] = []

    for badge_type in badge_types:
        badge = _make_badge(badge_type, project_name, stats, deps)
        if badge:
            badges.append(badge)

    return " ".join(badges)


def _make_badge(badge_type: str, project_name: str,
                stats: Dict, deps) -> Optional[str]:
    """Create a single badge Markdown string."""
    name = quote(project_name)

    if badge_type == "version":
        return f"![version](https://img.shields.io/badge/version-0.1.0-blue)"

    elif badge_type == "python":
        lang = getattr(deps, "language", "python") if deps else "python"
        if lang and lang != "python":
            return _runtime_badge(lang, deps)
        py_version = ""
        if deps and hasattr(deps, "python_version"):
            py_version = deps.python_version
        py_version = py_version or ">=3.9"
        py_safe = quote(py_version)
        return f"![python](https://img.shields.io/badge/python-{py_safe}-blue)"

    elif badge_type == "coverage":
        return f"![coverage](https://img.shields.io/badge/coverage-unknown-lightgrey)"

    elif badge_type == "complexity":
        funcs = stats.get("functions_found", 0)
        if funcs:
            return f"![functions](https://img.shields.io/badge/functions-{funcs}-green)"
        return None

    elif badge_type == "license":
        return f"![license](https://img.shields.io/badge/license-Apache%202.0-green)"

    elif badge_type == "docs":
        return f"![docs](https://img.shields.io/badge/docs-auto--generated-blueviolet)"

    return None


_RUNTIME_LABELS = {
    "php": ("php", "777BB4"),
    "javascript": ("node", "339933"),
    "typescript": ("typescript", "3178C6"),
    "rust": ("rust", "B7410E"),
    "go": ("go", "00ADD8"),
}


def _runtime_badge(lang: str, deps) -> Optional[str]:
    """Generate a runtime badge for non-Python languages."""
    label, color = _RUNTIME_LABELS.get(lang, (lang, "blue"))
    version = getattr(deps, "runtime_version", "") if deps else ""
    version = version or "any"
    return f"![{label}](https://img.shields.io/badge/{quote(label)}-{quote(version)}-{color})"
