"""
code2docs - Auto-generate and sync project documentation from source code.

Uses code2llm's AnalysisResult to produce human-readable documentation:
README.md, API references, module docs, examples, and architecture diagrams.
"""

__version__ = "3.0.10"
__author__ = "Tom Sapletta"

from .config import Code2DocsConfig

__all__ = [
    "Code2DocsConfig",
    "generate_readme",
    "generate_docs",
    "analyze_and_document",
]


def __getattr__(name):
    """Lazy import heavy modules on first access."""
    if name == "generate_readme":
        from .generators.readme_gen import generate_readme
        return generate_readme
    if name == "generate_docs":
        from .generators import generate_docs
        return generate_docs
    if name == "analyze_and_document":
        from .analyzers.project_scanner import analyze_and_document
        return analyze_and_document
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
