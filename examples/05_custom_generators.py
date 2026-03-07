"""Example 5: Custom Generators - Build your own documentation generator.

This example shows how to create custom documentation generators
using the code2docs generator framework.
"""

from typing import Dict, List
from dataclasses import dataclass
from code2llm.api import AnalysisResult
from code2docs.config import Code2DocsConfig
from code2docs.formatters.markdown import MarkdownFormatter


# =============================================================================
# CUSTOM GENERATOR EXAMPLE: Metrics Report
# =============================================================================

class MetricsReportGenerator:
    """Generate a metrics report from code analysis."""
    
    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self.formatter = MarkdownFormatter()
    
    def generate(self) -> str:
        """Generate the metrics report."""
        lines = []
        
        # Title
        lines.append(self.formatter.heading("Code Metrics Report", level=1))
        lines.append("")
        
        # Summary
        lines.append(self.formatter.heading("Summary", level=2))
        lines.append(self.formatter.paragraph(
            f"Project: **{self.config.project_name}**"
        ))
        lines.append("")
        
        # Statistics table
        stats = self._calculate_stats()
        lines.append(self.formatter.heading("Statistics", level=2))
        lines.append(self._format_stats_table(stats))
        lines.append("")
        
        # Top files by size
        lines.append(self.formatter.heading("Largest Files", level=2))
        lines.extend(self._list_largest_files())
        lines.append("")
        
        # Function analysis
        lines.append(self.formatter.heading("Function Analysis", level=2))
        lines.extend(self._analyze_functions())
        
        return "\n".join(lines)
    
    def _calculate_stats(self) -> Dict[str, int]:
        """Calculate code statistics."""
        return {
            "Total Files": len(self.result.files),
            "Total Functions": len(self.result.functions),
            "Total Classes": len(self.result.classes),
            "Avg Functions/File": len(self.result.functions) // max(1, len(self.result.files)),
        }
    
    def _format_stats_table(self, stats: Dict[str, int]) -> str:
        """Format statistics as markdown table."""
        lines = ["| Metric | Value |", "|--------|-------|"]
        for key, value in stats.items():
            lines.append(f"| {key} | {value} |")
        return "\n".join(lines)
    
    def _list_largest_files(self) -> List[str]:
        """List files with most functions."""
        # Count functions per file
        file_counts: Dict[str, int] = {}
        for func in self.result.functions.values():
            file_counts[func.file] = file_counts.get(func.file, 0) + 1
        
        # Sort and format
        sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)
        
        lines = ["| File | Functions |", "|------|-----------|"]
        for file, count in sorted_files[:10]:  # Top 10
            filename = file.split("/")[-1] if "/" in file else file
            lines.append(f"| `{filename}` | {count} |")
        
        return lines
    
    def _analyze_functions(self) -> List[str]:
        """Analyze function characteristics."""
        total_args = sum(len(f.args) for f in self.result.functions.values())
        avg_args = total_args / max(1, len(self.result.functions))
        
        with_docstrings = sum(
            1 for f in self.result.functions.values() if f.docstring
        )
        doc_rate = with_docstrings / max(1, len(self.result.functions)) * 100
        
        return [
            f"- **Average arguments per function:** {avg_args:.1f}",
            f"- **Documentation coverage:** {doc_rate:.1f}%",
            f"- **Functions with docstrings:** {with_docstrings}/{len(self.result.functions)}",
        ]


# =============================================================================
# CUSTOM GENERATOR EXAMPLE: API Changelog Generator
# =============================================================================

class APIChangelogGenerator:
    """Generate changelog based on API changes."""
    
    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
    
    def generate(self, previous_result: AnalysisResult = None) -> str:
        """Generate changelog comparing to previous analysis."""
        lines = []
        
        lines.append(f"# API Changelog - {self.config.project_name}\n")
        
        if previous_result is None:
            lines.append("## Initial Release\n")
            lines.append(self._list_new_apis())
        else:
            changes = self._compare_apis(previous_result)
            if changes["added"]:
                lines.append("## New APIs\n")
                for api in changes["added"]:
                    lines.append(f"- `{api}`")
                lines.append("")
            
            if changes["removed"]:
                lines.append("## Removed APIs\n")
                for api in changes["removed"]:
                    lines.append(f"- ~~`{api}`~~")
                lines.append("")
            
            if changes["modified"]:
                lines.append("## Modified APIs\n")
                for api in changes["modified"]:
                    lines.append(f"- `{api}` (signature changed)")
        
        return "\n".join(lines)
    
    def _list_new_apis(self) -> str:
        """List all APIs as new."""
        lines = ["### Functions\n"]
        for name in sorted(self.result.functions.keys()):
            lines.append(f"- `{name}()`")
        
        lines.append("\n### Classes\n")
        for name in sorted(self.result.classes.keys()):
            lines.append(f"- `{name}`")
        
        return "\n".join(lines)
    
    def _compare_apis(self, previous: AnalysisResult) -> Dict[str, List[str]]:
        """Compare current APIs to previous version."""
        current_funcs = set(self.result.functions.keys())
        previous_funcs = set(previous.functions.keys())
        
        current_classes = set(self.result.classes.keys())
        previous_classes = set(previous.classes.keys())
        
        return {
            "added": list(current_funcs - previous_funcs) + list(current_classes - previous_classes),
            "removed": list(previous_funcs - current_funcs) + list(previous_classes - current_classes),
            "modified": [],  # Would require deeper comparison
        }


# =============================================================================
# USING CUSTOM GENERATORS
# =============================================================================


def generate_custom_report(project_path: str) -> None:
    """Generate a custom metrics report."""
    from code2llm.api import analyze
    
    result = analyze(project_path)
    config = Code2DocsConfig(project_name="My Project")
    
    # Use custom generator
    generator = MetricsReportGenerator(config=config, result=result)
    report = generator.generate()
    
    # Save report
    output_path = f"{config.output_dir}/metrics.md"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(report)
    print(f"Generated metrics report: {output_path}")


# =============================================================================
# EXAMPLE: EXTENDING BASE GENERATOR
# =============================================================================

from code2docs.generators.base import BaseGenerator


class CustomGenerator(BaseGenerator):
    """Example of extending the base generator class."""
    
    def generate(self) -> str:
        """Override to provide custom generation logic."""
        return f"# Custom doc for {self.config.project_name}"
    
    def write(self, path: str, content: str) -> None:
        """Override to customize file writing."""
        print(f"Writing to {path}...")
        super().write(path, content)


if __name__ == "__main__":
    # Run custom generator
    # generate_custom_report("./my_project")
    pass
