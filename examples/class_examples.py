"""Class usage examples for code2docs."""

from code2docs.generators.module_docs_gen import ModuleDocsGenerator
from code2docs.formatters.markdown import MarkdownFormatter
from code2docs.generators.readme_gen import ReadmeGenerator
from code2docs.generators.examples_gen import ExamplesGenerator
from code2docs.generators.api_reference_gen import ApiReferenceGenerator


# --- ModuleDocsGenerator ---
# Generate docs/modules/ — detailed per-module documentation.
instance = ModuleDocsGenerator(config=..., result=...)
instance.generate_all()
instance.write_all(output_dir=..., files=...)

# --- MarkdownFormatter ---
# Helper for constructing Markdown documents.
instance = MarkdownFormatter()
instance.heading(text=..., level=...)
instance.paragraph(text=...)
instance.blockquote(text=...)

# --- ReadmeGenerator ---
# Generate README.md from AnalysisResult.
instance = ReadmeGenerator(config=..., result=...)
instance.generate()
instance.write(path=..., content=...)

# --- ExamplesGenerator ---
# Generate examples/ — usage examples from public API signatures.
instance = ExamplesGenerator(config=..., result=...)
instance.generate_all()
instance.write_all(output_dir=..., files=...)

# --- ApiReferenceGenerator ---
# Generate docs/api/ — per-module API reference from signatures.
instance = ApiReferenceGenerator(config=..., result=...)
instance.generate_all()
instance.write_all(output_dir=..., files=...)
