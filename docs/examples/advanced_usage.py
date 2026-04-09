"""
Advanced usage — code2docs

Shows how to use individual generators, sync, and formatters.
Run: python examples/advanced_usage.py
"""


# ==================================================
# Using individual generators
# ==================================================

from code2docs import Code2DocsConfig
from code2docs.analyzers.project_scanner import ProjectScanner
from code2docs.generators.readme_gen import ReadmeGenerator
from code2docs.generators.architecture_gen import ArchitectureGenerator
from code2docs.generators.coverage_gen import CoverageGenerator
from code2docs.generators.depgraph_gen import DepGraphGenerator

# Step 1: Analyze the project
config = Code2DocsConfig(project_name="my-project")
project_name_adv = config.project_name
scanner = ProjectScanner(config)
result = scanner.analyze(f"./{project_name_adv}") if project_name_adv != "." else scanner.analyze("./")

# Step 2: Generate with ReadmeGenerator
readme_gen = ReadmeGenerator(config, result)
content = readme_gen.generate()
print(f"Generated {len(content)} characters")

# Step 3: Generate with ArchitectureGenerator
architecture_gen = ArchitectureGenerator(config, result)
content = architecture_gen.generate()
print(f"Generated {len(content)} characters")

# Step 4: Generate with CoverageGenerator
coverage_gen = CoverageGenerator(config, result)
content = coverage_gen.generate()
print(f"Generated {len(content)} characters")

# Step 5: Generate with DepGraphGenerator
depGraph_gen = DepGraphGenerator(config, result)
content = depGraph_gen.generate()
print(f"Generated {len(content)} characters")


# ==================================================
# Formatters
# ==================================================

from code2docs.formatters.badges import generate_badges
from code2docs.formatters.toc import generate_toc

# Generate shields.io badges
badges = generate_badges(
    project_name="my-project",
    badge_types=["version", "python", "coverage"],
    stats={"version": "1.0.0", "python": ">=3.9"},
)
for badge in badges:
    print(badge)

# Generate table of contents
markdown = "# Title\n## Section 1\n## Section 2\n### Subsection"
toc = generate_toc(markdown, max_depth=2)
print(toc)


# ==================================================
# Sync — detect and apply changes
# ==================================================

from code2docs.sync.differ import Differ
from code2docs.sync.updater import Updater

# Detect changes since last generation
differ = Differ(config)
changes = differ.detect_changes("./my-project")

if changes:
    print(f"Detected {len(changes)} changed modules:")
    for change in changes:
        print(f"  {change}")

    # Apply selective update
    updater = Updater(config)
    updater.apply("./my-project", changes)
    print("Documentation updated!")
else:
    print("No changes detected.")
