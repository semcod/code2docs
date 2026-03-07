"""Documentation generators — produce Markdown, examples, and diagrams."""

from .readme_gen import ReadmeGenerator
from .api_reference_gen import ApiReferenceGenerator
from .module_docs_gen import ModuleDocsGenerator
from .examples_gen import ExamplesGenerator
from .architecture_gen import ArchitectureGenerator
from .changelog_gen import ChangelogGenerator
from .depgraph_gen import DepGraphGenerator
from .coverage_gen import CoverageGenerator
from .mkdocs_gen import MkDocsGenerator
from .api_changelog_gen import ApiChangelogGenerator

__all__ = [
    "ReadmeGenerator",
    "ApiReferenceGenerator",
    "ModuleDocsGenerator",
    "ExamplesGenerator",
    "ArchitectureGenerator",
    "ChangelogGenerator",
    "DepGraphGenerator",
    "CoverageGenerator",
    "MkDocsGenerator",
    "ApiChangelogGenerator",
    "generate_docs",
]


def generate_docs(project_path: str, config=None):
    """High-level function to generate all documentation."""
    from ..analyzers.project_scanner import ProjectScanner
    from ..config import Code2DocsConfig

    config = config or Code2DocsConfig()
    scanner = ProjectScanner(config)
    result = scanner.analyze(project_path)

    docs = {}
    docs["readme"] = ReadmeGenerator(config, result).generate()

    if config.docs.api_reference:
        docs["api"] = ApiReferenceGenerator(config, result).generate_all()

    if config.docs.module_docs:
        docs["modules"] = ModuleDocsGenerator(config, result).generate_all()

    if config.docs.architecture:
        docs["architecture"] = ArchitectureGenerator(config, result).generate()

    docs["dependency_graph"] = DepGraphGenerator(config, result).generate()
    docs["coverage"] = CoverageGenerator(config, result).generate()

    return docs
