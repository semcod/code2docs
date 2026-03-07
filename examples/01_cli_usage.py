"""Example 1: CLI Usage - Generate documentation from command line.

This example demonstrates how to use code2docs from the command line
to generate documentation for your project.
"""

# =============================================================================
# BASIC CLI USAGE
# =============================================================================

# Generate README.md for current directory
# $ code2docs .

# Generate with specific output
# $ code2docs ./my_project --output docs/

# Generate only README (skip other docs)
# $ code2docs . --readme-only

# Dry run - preview what would be generated
# $ code2docs . --dry-run

# =============================================================================
# ADVANCED CLI OPTIONS
# =============================================================================

# Watch mode - auto-regenerate on file changes
# $ code2docs . --watch

# Sync mode - update only changed sections
# $ code2docs . --sync

# Custom config file
# $ code2docs . --config my-code2docs.yaml

# Verbose output
# $ code2docs . -v


# =============================================================================
# PYTHON API: CLI Programmatically
# =============================================================================

import subprocess


def run_cli_basic(project_path: str) -> None:
    """Run code2docs CLI programmatically."""
    result = subprocess.run(
        ["code2docs", project_path, "--output", "docs/"],
        capture_output=True,
        text=True
    )
    print(f"Exit code: {result.returncode}")
    print(f"Output: {result.stdout}")


def run_cli_with_config(project_path: str, config_path: str) -> None:
    """Run with custom configuration."""
    subprocess.run([
        "code2docs", project_path,
        "--config", config_path,
        "--readme-only"
    ], check=True)


if __name__ == "__main__":
    # Example usage
    # run_cli_basic("./my_project")
    pass
