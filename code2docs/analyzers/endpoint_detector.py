"""Detect web framework endpoints (Flask, FastAPI, Django) from AST analysis."""

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from code2llm.core.models import AnalysisResult, FunctionInfo


@dataclass
class Endpoint:
    """Represents a detected web endpoint."""
    method: str  # GET, POST, PUT, DELETE, etc.
    path: str
    function_name: str
    file: str
    line: int
    framework: str  # flask, fastapi, django
    docstring: Optional[str] = None
    params: List[str] = field(default_factory=list)
    return_type: Optional[str] = None


class EndpointDetector:
    """Detects web endpoints from decorator patterns in source code."""

    FLASK_PATTERNS = re.compile(
        r'@(?:app|blueprint|bp)\.(route|get|post|put|delete|patch)\s*\(\s*["\']([^"\']+)["\']'
    )
    FASTAPI_PATTERNS = re.compile(
        r'@(?:app|router)\.(get|post|put|delete|patch|options|head)\s*\(\s*["\']([^"\']+)["\']'
    )
    DJANGO_URL_PATTERN = re.compile(
        r'(?:path|re_path|url)\s*\(\s*["\']([^"\']+)["\']'
    )

    def detect(self, result: AnalysisResult, project_path: str) -> List[Endpoint]:
        """Detect all endpoints from the analysis result."""
        endpoints: List[Endpoint] = []

        for qualified_name, func_info in result.functions.items():
            file_path = func_info.file
            if not file_path:
                continue

            # Check decorators for route patterns
            for decorator in func_info.decorators:
                endpoint = self._parse_decorator(decorator, func_info)
                if endpoint:
                    endpoints.append(endpoint)

        # Also scan for Django URL patterns in urls.py files
        endpoints.extend(self._scan_django_urls(project_path))

        return endpoints

    def _parse_decorator(self, decorator: str, func: FunctionInfo) -> Optional[Endpoint]:
        """Try to parse a route decorator string."""
        # Flask patterns
        match = self.FLASK_PATTERNS.search(decorator)
        if match:
            method = match.group(1).upper()
            if method == "ROUTE":
                method = "GET"
            return Endpoint(
                method=method,
                path=match.group(2),
                function_name=func.name,
                file=func.file,
                line=func.line,
                framework="flask",
                docstring=func.docstring,
                params=func.args,
                return_type=func.returns,
            )

        # FastAPI patterns
        match = self.FASTAPI_PATTERNS.search(decorator)
        if match:
            return Endpoint(
                method=match.group(1).upper(),
                path=match.group(2),
                function_name=func.name,
                file=func.file,
                line=func.line,
                framework="fastapi",
                docstring=func.docstring,
                params=func.args,
                return_type=func.returns,
            )

        return None

    def _scan_django_urls(self, project_path: str) -> List[Endpoint]:
        """Scan urls.py files for Django URL patterns."""
        endpoints: List[Endpoint] = []
        project = Path(project_path)

        for urls_file in project.rglob("urls.py"):
            try:
                source = urls_file.read_text(encoding="utf-8")
                for match in self.DJANGO_URL_PATTERN.finditer(source):
                    endpoints.append(Endpoint(
                        method="GET",
                        path=match.group(1),
                        function_name="",
                        file=str(urls_file),
                        line=source[:match.start()].count("\n") + 1,
                        framework="django",
                    ))
            except (OSError, UnicodeDecodeError):
                continue

        return endpoints
