"""Generator registry — pluggable generator system."""

from typing import Dict, List, Optional, Type

import click

from .base import BaseGenerator, GenerateContext


class GeneratorRegistry:
    """Registry of documentation generators.

    Generators register themselves via :meth:`register`. The CLI calls
    :meth:`run_all` which iterates registered generators in priority order.
    """

    def __init__(self) -> None:
        self._generators: List[BaseGenerator] = []

    def add(self, generator: BaseGenerator) -> None:
        """Add a generator instance to the registry."""
        self._generators.append(generator)

    def run_all(self, ctx: GenerateContext, *, readme_only: bool = False) -> None:
        """Run every registered generator that should execute."""
        for gen in self._generators:
            if gen.should_run(readme_only=readme_only):
                msg = gen.run(ctx)
                if msg:
                    click.echo(f"  {msg}")

    def run_only(self, name: str, ctx: GenerateContext) -> None:
        """Run a single generator by name."""
        for gen in self._generators:
            if gen.name == name:
                msg = gen.run(ctx)
                if msg:
                    click.echo(f"  {msg}")
                return
