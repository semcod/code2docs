"""Example 6: Formatters and Utilities - Working with markdown formatting.

This example shows how to use the formatting utilities
to create well-structured markdown documents.
"""

from code2docs.formatters.markdown import MarkdownFormatter
from code2docs.formatters.badges import generate_badges
from code2docs.formatters.toc import generate_toc, extract_headings


# =============================================================================
# MARKDOWN FORMATTER
# =============================================================================


def markdown_formatting_examples() -> None:
    """Demonstrate markdown formatting utilities."""
    formatter = MarkdownFormatter()
    
    # Headings
    print(formatter.heading("Main Title", level=1))
    print(formatter.heading("Section", level=2))
    print(formatter.heading("Subsection", level=3))
    
    # Text formatting
    print(formatter.paragraph("This is a paragraph of text."))
    print(formatter.bold("Bold text"))
    print(formatter.italic("Italic text"))
    print(formatter.code("inline_code"))
    
    # Code blocks
    code = """def hello():
    print("Hello, World!")"""
    print(formatter.code_block(code, language="python"))
    
    # Lists
    items = ["First item", "Second item", "Third item"]
    print(formatter.list_item("First item"))
    print(formatter.list_item("Second item"))
    print(formatter.list_item("Nested item", indent=1))
    
    # Blockquotes
    print(formatter.blockquote("This is a quoted text"))
    
    # Links and images
    print(formatter.link("Visit GitHub", "https://github.com"))
    print(formatter.image("Logo", "./logo.png"))


def generate_complex_document() -> str:
    """Generate a complex markdown document using the formatter."""
    f = MarkdownFormatter()
    
    sections = []
    
    # Title
    sections.append(f.heading("API Documentation", level=1))
    sections.append("")
    
    # Overview
    sections.append(f.heading("Overview", level=2))
    sections.append(f.paragraph(
        "This document describes the API endpoints and usage."
    ))
    sections.append("")
    
    # Authentication section
    sections.append(f.heading("Authentication", level=2))
    sections.append(f.paragraph(
        f"All API requests require an {f.bold('API key')} in the header."
    ))
    sections.append(f.code_block(
        'Authorization: Bearer YOUR_API_KEY',
        language="http"
    ))
    sections.append("")
    
    # Endpoints
    sections.append(f.heading("Endpoints", level=2))
    
    # Example endpoint
    sections.append(f.heading("GET /api/users", level=3))
    sections.append(f.paragraph("List all users."))
    sections.append("**Response:**")
    sections.append(f.code_block(
        '{"users": [{"id": 1, "name": "John"}]}',
        language="json"
    ))
    sections.append("")
    
    # Table example
    sections.append(f.heading("Error Codes", level=2))
    sections.append(f.table(
        headers=["Code", "Description"],
        rows=[
            ["400", "Bad Request"],
            ["401", "Unauthorized"],
            ["404", "Not Found"],
            ["500", "Internal Server Error"],
        ]
    ))
    
    return "\n".join(sections)


# =============================================================================
# BADGES
# =============================================================================


def badge_examples() -> None:
    """Generate various badge examples."""
    from code2docs.analyzers.dependency_scanner import DependencyScanner
    
    # Generate version badge
    badges = generate_badges(
        project_name="My Project",
        badge_types=["version", "python", "license"],
        stats={
            "coverage": 85,
            "complexity": "A",
            "lines": 5000,
        },
        deps=["numpy", "pandas", "requests"]
    )
    
    print("Generated badges:")
    for badge in badges.split("\n"):
        print(f"  {badge}")


# =============================================================================
# TABLE OF CONTENTS
# =============================================================================


def toc_examples() -> None:
    """Demonstrate table of contents generation."""
    markdown_content = """
# Main Title

## Introduction

Some intro text.

## Getting Started

### Installation

Instructions here.

### Configuration

Config details.

## API Reference

### Functions

Function docs.

### Classes

Class docs.
"""
    
    # Generate TOC
    toc = generate_toc(markdown_content, max_depth=3)
    print("Table of Contents:")
    print(toc)
    
    # Extract headings
    print("\nExtracted headings:")
    headings = extract_headings(markdown_content, max_depth=2)
    for level, text, anchor in headings:
        print(f"  Level {level}: {text} (#{anchor})")


# =============================================================================
# COMBINED EXAMPLE: README GENERATOR
# =============================================================================


def build_custom_readme() -> str:
    """Build a custom README using formatters."""
    f = MarkdownFormatter()
    
    parts = []
    
    # Header with badges
    parts.append(f.heading("My Awesome Project", level=1))
    parts.append("")
    parts.append(generate_badges(
        project_name="My Project",
        badge_types=["version", "python", "license"],
        stats={"coverage": 90}
    ))
    parts.append("")
    
    # Description
    parts.append(f.paragraph(
        "A powerful Python library for automating documentation generation."
    ))
    parts.append("")
    
    # TOC
    readme_content = "\n".join(parts)
    toc = generate_toc(readme_content + "\n## Features\n\n## Installation\n\n## Usage\n\n## API\n")
    parts.append(f.heading("Table of Contents", level=2))
    parts.append(toc)
    parts.append("")
    
    # Features
    parts.append(f.heading("Features", level=2))
    features = [
        "Automatic README generation",
        "API documentation extraction",
        "Module-level documentation",
        "Dependency graph visualization",
    ]
    for feature in features:
        parts.append(f.list_item(feature))
    parts.append("")
    
    # Installation
    parts.append(f.heading("Installation", level=2))
    parts.append(f.code_block("pip install my-project", language="bash"))
    parts.append("")
    
    return "\n".join(parts)


if __name__ == "__main__":
    # Run examples
    # markdown_formatting_examples()
    # print(generate_complex_document())
    # badge_examples()
    # toc_examples()
    # print(build_custom_readme())
    pass
