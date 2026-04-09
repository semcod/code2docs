"""Extract and analyze docstrings from source code."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from code2llm.api import AnalysisResult


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
        """Parse a docstring into structured sections (orchestrator)."""
        if not docstring:
            return DocstringInfo(raw="")

        lines = docstring.strip().splitlines()
        info = DocstringInfo(raw=docstring)
        info.summary = self._extract_summary(lines)
        self._parse_sections(lines[1:], info)
        return info

    @staticmethod
    def _extract_summary(lines: List[str]) -> str:
        """Extract the first-line summary."""
        return lines[0].strip() if lines else ""

    @staticmethod
    def _classify_section(line: str) -> Optional[str]:
        """Classify a line as a section header, or return None."""
        lower = line.strip().lower()
        if lower.startswith(("args:", "parameters:", "params:")):
            return "params"
        if lower.startswith(("returns:", "return:")):
            return "returns"
        if lower.startswith(("raises:", "raise:")):
            return "raises"
        if lower.startswith(("example:", "examples:", ">>>")):
            return "examples"
        return None

    _SECTION_PARSERS = {
        "params": "_parse_param_line",
        "returns": "_parse_returns_line",
        "raises": "_parse_raises_line",
        "examples": "_parse_examples_line",
    }

    def _parse_sections(self, lines: List[str], info: DocstringInfo) -> None:
        """Walk remaining lines, dispatching content to the right section."""
        current_section = "description"
        desc_lines: List[str] = []

        for line in lines:
            stripped = line.strip()

            new_section = self._classify_section(stripped)
            if new_section is not None:
                current_section = new_section
                if current_section == "examples" and stripped.startswith(">>>"):
                    info.examples.append(stripped)
                continue

            if current_section == "description":
                desc_lines.append(stripped)
            elif stripped and current_section in self._SECTION_PARSERS:
                getattr(self, self._SECTION_PARSERS[current_section])(info, stripped)

        info.description = "\n".join(desc_lines).strip()

    @staticmethod
    def _parse_param_line(info: DocstringInfo, line: str) -> None:
        """Parse a single param line: 'name: description'."""
        if ":" in line:
            pname, pdesc = line.split(":", 1)
            info.params[pname.strip()] = pdesc.strip()

    @staticmethod
    def _parse_returns_line(info: DocstringInfo, line: str) -> None:
        """Parse a returns line."""
        info.returns = line

    @staticmethod
    def _parse_raises_line(info: DocstringInfo, line: str) -> None:
        """Parse a raises line."""
        info.raises.append(line)

    @staticmethod
    def _parse_examples_line(info: DocstringInfo, line: str) -> None:
        """Parse an examples line."""
        info.examples.append(line)

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
