"""code2llm integration generator — produces analysis files in project/ folder."""

import subprocess
from pathlib import Path
from typing import List, Optional, Dict

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


class Code2LlmGenerator:
    """Generate code2llm analysis files in project/ directory.
    
    This generator wraps the code2llm CLI to produce comprehensive
    code analysis files including:
    - analysis.toon (health diagnostics)
    - context.md (LLM narrative)
    - evolution.toon (refactoring queue)
    - project.toon (project logic)
    - flow.toon, map.toon (structural analysis)
    - Mermaid diagrams (*.mmd)
    """

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate_all(self) -> Dict[str, str]:
        """Generate all code2llm analysis files.
        
        Returns:
            Dict mapping file names to their content or status.
        """
        project_path = Path(self.result.project_path)
        output_dir = project_path / "project"
        
        # Ensure output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)
        
        results = {}
        
        # Run code2llm analysis
        try:
            self._run_code2llm(project_path, output_dir)
            results["status"] = "success"
        except Exception as e:
            results["status"] = f"error: {e}"
            return results
        
        # Read generated files for reporting
        generated_files = [
            "analysis.toon",
            "context.md", 
            "evolution.toon",
            "project.toon",
            "flow.toon",
            "map.toon",
            "README.md",
        ]
        
        for filename in generated_files:
            file_path = output_dir / filename
            if file_path.exists():
                results[filename] = f"generated ({file_path.stat().st_size} bytes)"
        
        # Count Mermaid files
        mmd_files = list(output_dir.glob("*.mmd"))
        if mmd_files:
            results["diagrams"] = f"{len(mmd_files)} Mermaid files"
        
        return results

    def _run_code2llm(self, project_path: Path, output_dir: Path) -> None:
        """Execute code2llm CLI with appropriate options."""
        cfg = self.config.code2llm
        
        cmd = [
            "python", "-m", "code2llm",
            str(project_path),
            "-f", ",".join(cfg.formats),
            "-o", str(output_dir),
            "--strategy", cfg.strategy,
        ]
        
        # Add options based on config
        if not cfg.chunk:
            cmd.append("--no-chunk")
        if cfg.no_png:
            cmd.append("--no-png")
        if self.config.verbose:
            cmd.append("-v")
        
        # Run the command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(project_path),
        )
        
        # Don't raise on mmdc/png errors (optional dependencies)
        if result.returncode != 0 and "mmdc" not in result.stderr:
            raise RuntimeError(f"code2llm failed: {result.stderr}")

    def get_analysis_summary(self) -> str:
        """Get a summary of the analysis for integration with other docs."""
        project_path = Path(self.result.project_path)
        analysis_file = project_path / "project" / "analysis.toon"
        
        if not analysis_file.exists():
            return "Analysis not yet generated."
        
        content = analysis_file.read_text(encoding="utf-8")
        lines = content.split("\n")[:10]
        return "\n".join(lines)


def generate_code2llm_analysis(project_path: str, 
                                config: Optional[Code2DocsConfig] = None) -> Dict[str, str]:
    """Convenience function to generate code2llm analysis.
    
    Args:
        project_path: Path to the project to analyze
        config: Optional configuration
        
    Returns:
        Dictionary with generation status and file list
    """
    from ..analyzers.project_scanner import ProjectScanner
    
    config = config or Code2DocsConfig()
    scanner = ProjectScanner(config)
    result = scanner.analyze(project_path)
    
    gen = Code2LlmGenerator(config, result)
    return gen.generate_all()
