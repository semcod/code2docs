"""Base generator interface and generation context."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from code2llm.api import AnalysisResult

from .config import Code2DocsConfig


@dataclass
class GenerateContext:
    """Shared context passed to all generators during a run."""
    project: Path
    docs_dir: Path
    dry_run: bool = False
    verbose: bool = False


class BaseGenerator(ABC):
    """Abstract base for all documentation generators.

    Subclasses must define ``name`` and implement ``should_run`` / ``run``.
    Adding a new generator requires only creating a subclass and registering it
    with the :class:`GeneratorRegistry`; no changes to ``cli.py`` needed.
    """

    name: str = ""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    @abstractmethod
    def should_run(self, *, readme_only: bool = False) -> bool:
        """Return True if this generator should execute."""

    @abstractmethod
    def run(self, ctx: GenerateContext) -> Optional[str]:
        """Execute generation and write output.

        Returns a short status message (e.g. '✅ docs/api/ (12 files)')
        or None if nothing was produced.
        """
