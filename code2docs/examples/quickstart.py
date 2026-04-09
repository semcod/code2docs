"""
Quickstart — code2docs

Minimal working examples for the most common use cases.
Run: python examples/quickstart.py
"""


from code2docs import Code2DocsConfig
from code2docs import generate_docs
from code2docs import generate_readme

# ==================================================
# Example 1: Configuration
# ==================================================

config = Code2DocsConfig(
    project_name="my-project",
    source="./src",
    output="./docs",
    verbose=True,
)


# ==================================================
# Example 2: Generate documentation
# ==================================================

# Generate a README for your project
generate_readme("./my-project", output="README.md")

# Generate all documentation
docs = generate_docs("./my-project", config=config)
print(f"Generated {len(docs)} documentation sections")


# ==================================================
# Example 3: Analyze a project programmatically
# ==================================================

from code2docs.analyzers.project_scanner import ProjectScanner

scanner = ProjectScanner(config)
result = scanner.analyze("./my-project")

print(f"Found {len(result.functions)} functions")
print(f"Found {len(result.classes)} classes")
print(f"Found {len(result.modules)} modules")
