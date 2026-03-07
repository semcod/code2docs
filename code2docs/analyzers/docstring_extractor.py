"""Extract and analyze docstrings from source code."""

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from code2llm.core.models import AnalysisResult, FunctionInfo, ClassInfo


@dataclass
class DocstringInfo:
    """Parsed docstring with sections."""
    raw: str
    summary: str = ""
    description: str = ""
    params: Dict[str, str] = field(default_factory=dict)
    returns: str = ""
    raises: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)


class DocstringExtractor:
    """Extract and parse docstrings from AnalysisResult."""

    def extract_all(self, result: AnalysisResult) -> Dict[str, DocstringInfo]:
        """Extract docstrings for all functions and classes."""
        docs: Dict[str, DocstringInfo] = {}

        for name, func in result.functions.items():
            if func.docstring:
                docs[name] = self.parse(func.docstring)

        for name, cls in result.classes.items():
            if cls.docstring:
                docs[name] = self.parse(cls.docstring)

        return docs

    def parse(self, docstring: str) -> DocstringInfo:
        """Parse a docstring into structured sections."""
        if not docstring:
            return DocstringInfo(raw="")

        lines = docstring.strip().splitlines()
        info = DocstringInfo(raw=docstring)

        if lines:
            info.summary = lines[0].strip()

        # Simple parser for Google/Numpy/Sphinx styles
        current_section = "description"
        desc_lines: List[str] = []
        param_lines: List[Tuple[str, str]] = []

        for line in lines[1:]:
            stripped = line.strip()
            lower = stripped.lower()

            if lower.startswith(("args:", "parameters:", "params:")):
                current_section = "params"
                continue
            elif lower.startswith(("returns:", "return:")):
                current_section = "returns"
                continue
            elif lower.startswith(("raises:", "raise:")):
                current_section = "raises"
                continue
            elif lower.startswith(("example:", "examples:", ">>>")):
                current_section = "examples"
                if stripped.startswith(">>>"):
                    info.examples.append(stripped)
                continue

            if current_section == "description":
                desc_lines.append(stripped)
            elif current_section == "params" and stripped:
                # Parse "name: description" or "name (type): description"
                if ":" in stripped:
                    pname, pdesc = stripped.split(":", 1)
                    info.params[pname.strip()] = pdesc.strip()
            elif current_section == "returns" and stripped:
                info.returns = stripped
            elif current_section == "raises" and stripped:
                info.raises.append(stripped)
            elif current_section == "examples" and stripped:
                info.examples.append(stripped)

        info.description = "\n".join(desc_lines).strip()
        return info

    def coverage_report(self, result: AnalysisResult) -> Dict[str, float]:
        """Calculate docstring coverage statistics."""
        total_funcs = len(result.functions)
        total_classes = len(result.classes)
        documented_funcs = sum(1 for f in result.functions.values() if f.docstring)
        documented_classes = sum(1 for c in result.classes.values() if c.docstring)

        return {
            "functions_total": total_funcs,
            "functions_documented": documented_funcs,
            "functions_coverage": (documented_funcs / total_funcs * 100) if total_funcs else 0,
            "classes_total": total_classes,
            "classes_documented": documented_classes,
            "classes_coverage": (documented_classes / total_classes * 100) if total_classes else 0,
            "overall_coverage": (
                (documented_funcs + documented_classes)
                / (total_funcs + total_classes)
                * 100
            ) if (total_funcs + total_classes) else 0,
        }
