"""Organization README generator - generates overview of multiple projects."""

from pathlib import Path
from typing import Dict, Optional

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..analyzers.project_scanner import ProjectScanner


class OrgReadmeGenerator:
    """Generate organization README with list of projects and brief descriptions."""

    def __init__(self, config: Code2DocsConfig, org_path: str, org_name: str = ""):
        self.config = config
        self.org_path = Path(org_path).resolve()
        self.org_name = org_name or self.org_path.name
        self.scanner = ProjectScanner(config)

    def generate(self) -> str:
        """Generate organization README content."""
        projects = self._discover_projects()
        
        lines = [
            f"# {self.org_name}\n",
            f"Projects in the {self.org_name} organization.\n",
            f"**{len(projects)}** projects discovered.\n",
            "## Projects\n",
        ]
        
        for project_name, project_info in sorted(projects.items()):
            lines.append(self._render_project_section(project_name, project_info))
            lines.append("")
        
        return "\n".join(lines)

    def _discover_projects(self) -> Dict[str, Dict]:
        """Discover all projects in organization directory."""
        projects = {}
        
        for item in self.org_path.iterdir():
            if not item.is_dir():
                continue
            if item.name.startswith(".") or item.name.startswith("__"):
                continue
            
            project_info = self._analyze_project(item)
            if project_info:
                projects[item.name] = project_info
        
        return projects

    def _analyze_project(self, project_path: Path) -> Optional[Dict]:
        """Analyze a single project and return summary info."""
        try:
            result = self.scanner.analyze(str(project_path))
            
            # Extract description from first module docstring or pyproject.toml
            description = self._extract_description(project_path, result)
            
            # Count functions, classes, modules
            func_count = len(result.functions)
            class_count = len(result.classes)
            module_count = len(result.modules)
            
            # Get version from pyproject.toml if available
            version = self._get_version(project_path)
            
            # Get repo URL from git or config
            repo_url = self._get_repo_url(project_path)
            
            return {
                "name": project_path.name,
                "description": description,
                "version": version,
                "stats": {
                    "functions": func_count,
                    "classes": class_count,
                    "modules": module_count,
                },
                "repo_url": repo_url,
                "path": str(project_path),
            }
        except Exception:
            return None

    def _extract_description(self, project_path: Path, result: AnalysisResult) -> str:
        """Extract short description from project (max 5 lines)."""
        # Try pyproject.toml first
        try:
            import tomllib
            pyproject = project_path / "pyproject.toml"
            if pyproject.exists():
                with open(pyproject, "rb") as f:
                    data = tomllib.load(f)
                    desc = data.get("project", {}).get("description", "")
                    if desc:
                        # Limit to ~5 lines worth of content
                        return self._truncate_description(desc)
        except Exception:
            pass
        
        # Try first package docstring
        for mod in result.modules.values():
            if mod.is_package and hasattr(mod, "docstring") and mod.docstring:
                return self._truncate_description(mod.docstring)
        
        # Try README.md first paragraph
        readme = project_path / "README.md"
        if readme.exists():
            try:
                content = readme.read_text(encoding="utf-8")
                # Find first paragraph after title
                lines = content.split("\n")
                for i, line in enumerate(lines):
                    if line.startswith("# "):
                        # Get next non-empty lines
                        desc_lines = []
                        for j in range(i + 1, min(i + 10, len(lines))):
                            if lines[j].strip() and not lines[j].startswith("#"):
                                desc_lines.append(lines[j].strip())
                            if len(desc_lines) >= 5:
                                break
                        if desc_lines:
                            return " ".join(desc_lines)
            except Exception:
                pass
        
        return "No description available."

    def _truncate_description(self, desc: str, max_chars: int = 300) -> str:
        """Truncate description to ~5 lines of content."""
        lines = desc.strip().split("\n")
        # Filter out empty lines and headers
        content_lines = [l.strip() for l in lines if l.strip() and not l.startswith("#")]
        
        result = []
        char_count = 0
        for line in content_lines[:5]:
            if char_count + len(line) > max_chars:
                remaining = max_chars - char_count
                if remaining > 20:
                    result.append(line[:remaining] + "...")
                break
            result.append(line)
            char_count += len(line)
        
        return " ".join(result) if result else "No description available."

    def _get_version(self, project_path: Path) -> str:
        """Get version from pyproject.toml or VERSION file."""
        try:
            import tomllib
            pyproject = project_path / "pyproject.toml"
            if pyproject.exists():
                with open(pyproject, "rb") as f:
                    data = tomllib.load(f)
                    return data.get("project", {}).get("version", "")
        except Exception:
            pass
        
        version_file = project_path / "VERSION"
        if version_file.exists():
            return version_file.read_text(encoding="utf-8").strip()
        
        return ""

    def _get_repo_url(self, project_path: Path) -> str:
        """Get repository URL from git or pyproject.toml."""
        # Try pyproject.toml
        try:
            import tomllib
            pyproject = project_path / "pyproject.toml"
            if pyproject.exists():
                with open(pyproject, "rb") as f:
                    data = tomllib.load(f)
                    urls = data.get("project", {}).get("urls", {})
                    if urls:
                        return urls.get("Repository", urls.get("Homepage", ""))
        except Exception:
            pass
        
        # Try git remote
        try:
            import subprocess
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                cwd=str(project_path),
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0:
                url = result.stdout.strip()
                # Convert SSH to HTTPS
                if url.startswith("git@"):
                    url = url.replace(":", "/", 1).replace("git@", "https://", 1)
                return url.removesuffix(".git")
        except Exception:
            pass
        
        return ""

    def _render_project_section(self, name: str, info: Dict) -> str:
        """Render a single project section (5 lines max)."""
        lines = [f"### {name}"]
        
        # Line 1: Description
        lines.append(info["description"])
        
        # Line 2: Stats
        stats = info["stats"]
        stats_line = f"📊 {stats['functions']} functions | {stats['classes']} classes | {stats['modules']} modules"
        if info["version"]:
            stats_line += f" | v{info['version']}"
        lines.append(stats_line)
        
        # Line 3: Repo link if available
        if info["repo_url"]:
            lines.append(f"🔗 [{info['repo_url']}]({info['repo_url']})")
        
        return "\n".join(lines)

    def write(self, output_path: str, content: str) -> None:
        """Write README to output path."""
        out_path = Path(output_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
