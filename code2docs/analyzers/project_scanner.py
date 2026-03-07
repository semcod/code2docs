"""Wrapper around code2llm's ProjectAnalyzer for documentation purposes."""

from pathlib import Path
from typing import Optional

from code2llm import Config, FAST_CONFIG
from code2llm.core.analyzer import ProjectAnalyzer
from code2llm.core.models import AnalysisResult

from ..config import Code2DocsConfig


class ProjectScanner:
    """Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults."""

    def __init__(self, config: Optional[Code2DocsConfig] = None):
        self.config = config or Code2DocsConfig()
        self._llm_config = self._build_llm_config()

    def _build_llm_config(self) -> Config:
        """Create code2llm Config tuned for documentation generation."""
        config = Config(
            mode="static",
            verbose=self.config.verbose,
        )
        config.filters.exclude_tests = self.config.exclude_tests
        config.filters.skip_private = self.config.skip_private
        # Keep properties and accessors visible for docs
        config.filters.skip_properties = False
        config.filters.skip_accessors = False
        # Enable pattern detection for architecture docs
        config.performance.skip_pattern_detection = False
        config.performance.parallel_enabled = True
        return config

    def analyze(self, project_path: str) -> AnalysisResult:
        """Analyze a project and return AnalysisResult for doc generation."""
        analyzer = ProjectAnalyzer(self._llm_config)
        return analyzer.analyze_project(project_path)


def analyze_and_document(project_path: str, config: Optional[Code2DocsConfig] = None) -> AnalysisResult:
    """Convenience function: analyze a project in one call."""
    scanner = ProjectScanner(config)
    return scanner.analyze(project_path)
