"""Example 3: Programmatic API - Use code2docs in your Python code.

This example demonstrates how to use code2docs programmatically
to analyze code and generate documentation.
"""

from pathlib import Path
from code2llm.api import analyze
from code2docs import generate_readme, Code2DocsConfig
from code2docs.generators.readme_gen import ReadmeGenerator
from code2docs.generators.api_reference_gen import ApiReferenceGenerator
from code2docs.generators.module_docs_gen import ModuleDocsGenerator


# =============================================================================
# BASIC PROGRAMMATIC USAGE
# =============================================================================


def generate_readme_simple(project_path: str) -> str:
    """Generate README.md content from a project."""
    # Analyze the project
    result = analyze(project_path)
    
    # Generate README
    config = Code2DocsConfig(project_name="My Project")
    content = generate_readme(
        project_path=project_path,
        config=config,
        output="README.md"
    )
    return content


def generate_full_documentation(project_path: str) -> None:
    """Generate complete documentation for a project."""
    # Analyze the project
    result = analyze(project_path)
    
    # Create configuration
    config = Code2DocsConfig(
        project_name=result.project_name or "My Project",
        output_dir="docs",
    )
    
    # Generate README
    readme_gen = ReadmeGenerator(config=config, result=result)
    readme_content = readme_gen.generate()
    readme_gen.write(path="docs/README.md", content=readme_content)
    
    # Generate API reference
    api_gen = ApiReferenceGenerator(config=config, result=result)
    api_files = api_gen.generate_all()
    api_gen.write_all(output_dir="docs/api", files=api_files)
    
    # Generate module documentation
    module_gen = ModuleDocsGenerator(config=config, result=result)
    module_files = module_gen.generate_all()
    module_gen.write_all(output_dir="docs/modules", files=module_files)
    
    print(f"Generated documentation in docs/")


# =============================================================================
# ADVANCED: CUSTOM GENERATION PIPELINE
# =============================================================================


def custom_documentation_pipeline(project_path: str) -> dict:
    """Create a custom documentation pipeline."""
    from code2docs.generators.architecture_gen import ArchitectureGenerator
    from code2docs.generators.depgraph_gen import DependencyGraphGenerator
    from code2docs.generators.changelog_gen import ChangelogGenerator
    
    result = analyze(project_path)
    config = Code2DocsConfig(project_name="Custom Project")
    
    generated = {}
    
    # Generate architecture diagram
    arch_gen = ArchitectureGenerator(config=config, result=result)
    generated["architecture"] = arch_gen.generate()
    
    # Generate dependency graph
    dep_gen = DependencyGraphGenerator(config=config, result=result)
    generated["dependencies"] = dep_gen.generate()
    
    # Generate changelog
    change_gen = ChangelogGenerator(config=config, result=result)
    generated["changelog"] = change_gen.generate()
    
    return generated


# =============================================================================
# WORKING WITH ANALYSIS RESULTS
# =============================================================================


def inspect_project_structure(project_path: str) -> None:
    """Inspect project structure from analysis."""
    result = analyze(project_path)
    
    print("=== Project Structure ===")
    print(f"Project: {result.project_name}")
    print(f"Files: {len(result.files)}")
    print(f"Functions: {len(result.functions)}")
    print(f"Classes: {len(result.classes)}")
    
    # List all functions
    print("\n=== Functions ===")
    for name, func in result.functions.items():
        print(f"  - {name} (line {func.line})")
    
    # List all classes
    print("\n=== Classes ===")
    for name, cls in result.classes.items():
        print(f"  - {name}")
        if cls.methods:
            for method in cls.methods:
                print(f"    - {method}")


# =============================================================================
# EXAMPLE: CONDITIONAL DOCUMENTATION GENERATION
# =============================================================================


def generate_docs_if_needed(project_path: str, force: bool = False) -> bool:
    """Only generate docs if code has changed."""
    from code2docs.sync.differ import Differ
    
    differ = Differ(project_path)
    changes = differ.detect_changes()
    
    if changes.has_changes or force:
        print(f"Changes detected: {len(changes.new_files)} new, "
              f"{len(changes.modified)} modified")
        
        result = analyze(project_path)
        config = Code2DocsConfig()
        
        # Update only changed sections
        from code2docs.sync.updater import Updater
        updater = Updater(config=config)
        updater.apply(project_path=project_path, changes=changes)
        
        return True
    else:
        print("No changes detected, skipping documentation generation")
        return False


if __name__ == "__main__":
    # Run examples
    # generate_readme_simple("./my_project")
    # generate_full_documentation("./my_project")
    # inspect_project_structure("./my_project")
    pass
