"""code2llm integration generator — produces analysis files in project/ folder."""

import subprocess
from pathlib import Path
from typing import List, Optional, Dict

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


def parse_gitignore(project_path: Path) -> List[str]:
    """Parse .gitignore file and return list of patterns to exclude.

    Filters out:
    - Empty lines
    - Comments (lines starting with #)
    - Negation patterns (starting with !)
    - Complex patterns with ** or regex

    Returns simple directory/file patterns that can be passed to --skip-subprojects.
    """
    gitignore_path = project_path / ".gitignore"
    if not gitignore_path.exists():
        return []

    try:
        content = gitignore_path.read_text(encoding="utf-8")
        return _extract_patterns(content)
    except Exception:
        return []


def _extract_patterns(content: str) -> List[str]:
    """Extract valid patterns from gitignore content."""
    patterns = []
    for line in content.split("\n"):
        pattern = _process_line(line)
        if pattern:
            patterns.append(pattern)
    return patterns


def _process_line(line: str) -> str:
    """Process a single gitignore line, returning valid pattern or empty string."""
    line = line.strip()

    if _should_skip_line(line):
        return ""

    pattern = _clean_pattern(line)
    if _is_valid_pattern(pattern):
        return pattern
    return ""


def _should_skip_line(line: str) -> bool:
    """Check if line should be skipped (empty, comment, negation, globstar)."""
    if not line or line.startswith("#"):
        return True
    if line.startswith("!"):
        return True
    if "**" in line:
        return True
    if "*" in line and "/" not in line:
        return True
    return False


def _clean_pattern(line: str) -> str:
    """Clean up the pattern by removing trailing slashes and leading slashes."""
    pattern = line.rstrip("/")
    if pattern.startswith("/"):
        pattern = pattern[1:]
    return pattern


def _is_valid_pattern(pattern: str) -> bool:
    """Check if pattern is valid (no special chars, length > 1)."""
    if not pattern or len(pattern) <= 1:
        return False
    if any(c in pattern for c in "[]?*"):
        return False
    return True


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

        cmd = self._build_base_cmd(project_path, output_dir, cfg)
        self._add_config_options(cmd, cfg)
        self._add_exclude_patterns(cmd, cfg, project_path)
        self._execute_command(cmd, project_path)

    def _build_base_cmd(self, project_path: Path, output_dir: Path, cfg) -> List[str]:
        """Build base command with required options."""
        return [
            "python", "-m", "code2llm",
            str(project_path),
            "-f", ",".join(cfg.formats),
            "-o", str(output_dir),
            "--strategy", cfg.strategy,
            "--max-depth", str(cfg.max_depth),
        ]

    def _add_config_options(self, cmd: List[str], cfg) -> None:
        """Add optional flags based on config settings."""
        if not cfg.chunk:
            cmd.append("--no-chunk")
        if cfg.no_png:
            cmd.append("--no-png")
        if self.config.verbose:
            cmd.append("-v")

    def _add_exclude_patterns(self, cmd: List[str], cfg, project_path: Path) -> None:
        """Add exclude patterns from config and .gitignore."""
        skip_dirs = self._get_config_skip_dirs(cfg)
        gitignore_patterns = parse_gitignore(project_path)

        all_patterns = self._merge_patterns(skip_dirs, gitignore_patterns)
        if all_patterns:
            cmd.append("--skip-subprojects")
            cmd.extend(all_patterns[:10])

    def _get_config_skip_dirs(self, cfg) -> List[str]:
        """Get skip directories from config exclude patterns."""
        if not cfg.exclude_patterns:
            return []
        return [p for p in cfg.exclude_patterns if not p.startswith(".") and not p.startswith("*")]

    def _merge_patterns(self, config_patterns: List[str], gitignore_patterns: List[str]) -> List[str]:
        """Merge config and gitignore patterns, removing duplicates."""
        existing = set(config_patterns)
        merged = list(config_patterns)
        for p in gitignore_patterns:
            if p not in existing:
                merged.append(p)
                existing.add(p)
        return merged

    def _execute_command(self, cmd: List[str], project_path: Path) -> None:
        """Run the subprocess command and handle errors."""
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
