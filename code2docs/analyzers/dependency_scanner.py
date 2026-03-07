"""Scan project dependencies from requirements.txt, pyproject.toml, setup.py."""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None  # type: ignore


@dataclass
class DependencyInfo:
    """Information about a project dependency."""
    name: str
    version_spec: str = ""
    optional: bool = False
    group: str = "main"


@dataclass
class ProjectDependencies:
    """All detected project dependencies."""
    python_version: str = ""
    dependencies: List[DependencyInfo] = field(default_factory=list)
    dev_dependencies: List[DependencyInfo] = field(default_factory=list)
    optional_groups: Dict[str, List[DependencyInfo]] = field(default_factory=dict)
    install_command: str = "pip install ."
    source_file: str = ""


class DependencyScanner:
    """Scan and parse project dependency files."""

    def scan(self, project_path: str) -> ProjectDependencies:
        """Scan project for dependency information."""
        project = Path(project_path)
        deps = ProjectDependencies()

        # Priority: pyproject.toml > setup.py > requirements.txt
        pyproject = project / "pyproject.toml"
        if pyproject.exists():
            deps = self._parse_pyproject(pyproject)
            deps.source_file = "pyproject.toml"
            return deps

        setup_py = project / "setup.py"
        if setup_py.exists():
            deps = self._parse_setup_py(setup_py)
            deps.source_file = "setup.py"
            return deps

        req_txt = project / "requirements.txt"
        if req_txt.exists():
            deps = self._parse_requirements_txt(req_txt)
            deps.source_file = "requirements.txt"
            return deps

        return deps

    def _parse_pyproject(self, path: Path) -> ProjectDependencies:
        """Parse pyproject.toml for dependencies."""
        deps = ProjectDependencies()

        if tomllib is None:
            # Fallback: regex-based parsing
            return self._parse_pyproject_regex(path)

        with open(path, "rb") as f:
            data = tomllib.load(f)

        project = data.get("project", {})
        deps.python_version = project.get("requires-python", "")

        # Main dependencies
        for dep_str in project.get("dependencies", []):
            deps.dependencies.append(self._parse_dep_string(dep_str))

        # Optional dependencies
        for group, dep_list in project.get("optional-dependencies", {}).items():
            group_deps = [self._parse_dep_string(d) for d in dep_list]
            for d in group_deps:
                d.optional = True
                d.group = group
            deps.optional_groups[group] = group_deps
            if group == "dev":
                deps.dev_dependencies = group_deps

        # Install command
        name = project.get("name", "")
        if name:
            deps.install_command = f"pip install {name}"

        return deps

    def _parse_pyproject_regex(self, path: Path) -> ProjectDependencies:
        """Fallback regex-based pyproject.toml parser."""
        deps = ProjectDependencies()
        content = path.read_text(encoding="utf-8")

        # Extract dependencies array
        dep_match = re.search(r'dependencies\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if dep_match:
            for dep_str in re.findall(r'"([^"]+)"', dep_match.group(1)):
                deps.dependencies.append(self._parse_dep_string(dep_str))

        # Extract python version
        py_match = re.search(r'requires-python\s*=\s*"([^"]+)"', content)
        if py_match:
            deps.python_version = py_match.group(1)

        return deps

    def _parse_setup_py(self, path: Path) -> ProjectDependencies:
        """Parse setup.py for dependencies (regex-based, no exec)."""
        deps = ProjectDependencies()
        content = path.read_text(encoding="utf-8")

        # install_requires
        match = re.search(r'install_requires\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if match:
            for dep_str in re.findall(r'"([^"]+)"', match.group(1)):
                deps.dependencies.append(self._parse_dep_string(dep_str))

        # python_requires
        py_match = re.search(r'python_requires\s*=\s*"([^"]+)"', content)
        if py_match:
            deps.python_version = py_match.group(1)

        return deps

    def _parse_requirements_txt(self, path: Path) -> ProjectDependencies:
        """Parse requirements.txt."""
        deps = ProjectDependencies()

        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            deps.dependencies.append(self._parse_dep_string(line))

        deps.install_command = "pip install -r requirements.txt"
        return deps

    @staticmethod
    def _parse_dep_string(dep_str: str) -> DependencyInfo:
        """Parse a dependency string like 'package>=1.0'."""
        match = re.match(r'^([a-zA-Z0-9_-]+)\s*(.*)', dep_str.strip())
        if match:
            return DependencyInfo(
                name=match.group(1),
                version_spec=match.group(2).strip(),
            )
        return DependencyInfo(name=dep_str.strip())
