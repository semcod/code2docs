"""Example 2: Configuration - Set up code2docs with custom settings.

This example shows how to configure code2docs programmatically
and via YAML configuration files.
"""

from pathlib import Path
from code2docs.config import Code2DocsConfig


# =============================================================================
# PROGRAMMATIC CONFIGURATION
# =============================================================================


def create_basic_config() -> Code2DocsConfig:
    """Create a basic configuration."""
    config = Code2DocsConfig(
        project_name="My Project",
        output_dir="docs",
        readme_sections=[
            "header",
            "badges",
            "overview",
            "installation",
            "usage",
            "api",
            "contributing",
        ]
    )
    return config


def create_advanced_config() -> Code2DocsConfig:
    """Create advanced configuration with all options."""
    return Code2DocsConfig(
        project_name="My Awesome Project",
        project_description="A powerful tool for automation",
        output_dir="documentation",
        readme_file="README.md",
        
        # README sections to include
        readme_sections=[
            "header",
            "badges", 
            "toc",
            "overview",
            "features",
            "installation",
            "quickstart",
            "usage",
            "api",
            "examples",
            "contributing",
            "license",
        ],
        
        # Badge configuration
        badges={
            "version": True,
            "python": True,
            "license": True,
            "ci": False,
        },
        
        # API documentation settings
        api_config={
            "include_private": False,
            "include_docstrings": True,
            "group_by_module": True,
        },
        
        # Files to exclude
        exclude_patterns=[
            "tests/*",
            "*_test.py",
            "__pycache__/*",
            ".venv/*",
        ],
        
        # Sync markers for partial updates
        sync_markers=True,
    )


# =============================================================================
# YAML CONFIGURATION FILE
# =============================================================================

EXAMPLE_YAML_CONFIG = """
# code2docs.yaml - Example configuration file

project_name: "My Project"
project_description: "Automatically generated docs from code"
output_dir: "docs"
readme_file: "README.md"

# README sections in order
readme_sections:
  - header
  - badges
  - toc
  - overview
  - installation
  - usage
  - api
  - examples

# Badge types to generate
badges:
  version: true
  python: true
  license: true
  ci: false
  coverage: true

# API documentation settings
api_config:
  include_private: false
  include_docstrings: true
  group_by_module: true

# Patterns to exclude from analysis
exclude_patterns:
  - "tests/*"
  - "*_test.py"
  - "__pycache__/*"
  - ".venv/*"
  - "node_modules/*"

# Enable sync markers for partial updates
sync_markers: true
"""


def save_yaml_config_example(path: str = "code2docs.yaml") -> None:
    """Save example YAML config to file."""
    Path(path).write_text(EXAMPLE_YAML_CONFIG)
    print(f"Saved example config to {path}")


def load_config_from_yaml(path: str) -> Code2DocsConfig:
    """Load configuration from YAML file."""
    return Code2DocsConfig.from_yaml(path)


# =============================================================================
# USAGE EXAMPLES
# =============================================================================

if __name__ == "__main__":
    # Create and use config programmatically
    config = create_basic_config()
    print(f"Project: {config.project_name}")
    print(f"Output dir: {config.output_dir}")
    
    # Save example YAML config
    save_yaml_config_example("example-code2docs.yaml")
    
    # Load from YAML
    # loaded_config = load_config_from_yaml("code2docs.yaml")
