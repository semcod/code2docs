"""LLM helper — optional LLM-assisted documentation generation via litellm.

If litellm is not installed or LLM is not configured, all methods return None
and generators fall back to algorithm-based template output.
"""

import logging
from typing import Optional

from .config import LLMConfig

logger = logging.getLogger(__name__)

# Lazy import: litellm is an optional dependency
_litellm = None


def _get_litellm():
    """Import litellm lazily."""
    global _litellm
    if _litellm is None:
        try:
            import litellm
            litellm.suppress_debug_info = True
            _litellm = litellm
        except ImportError:
            _litellm = False  # sentinel: tried and failed
    return _litellm if _litellm is not False else None


class LLMHelper:
    """Thin wrapper around litellm for documentation generation.

    If LLM is unavailable or disabled, every method returns None so callers
    can fall through to template-based generation.
    """

    def __init__(self, config: LLMConfig):
        self.config = config
        self._available: Optional[bool] = None

    @property
    def available(self) -> bool:
        """Check if LLM is configured and litellm is installed."""
        if self._available is None:
            self._available = (
                self.config.enabled
                and bool(self.config.model)
                and _get_litellm() is not None
            )
            if self._available:
                logger.info("LLM enabled: model=%s", self.config.model)
            else:
                logger.debug("LLM disabled (enabled=%s, model=%s, litellm=%s)",
                             self.config.enabled, bool(self.config.model),
                             _get_litellm() is not None)
        return self._available

    def complete(self, prompt: str, system: str = "") -> Optional[str]:
        """Send a completion request. Returns None on any failure."""
        if not self.available:
            return None
        litellm = _get_litellm()
        if litellm is None:
            return None

        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        kwargs = {
            "model": self.config.model,
            "messages": messages,
            "max_tokens": self.config.max_tokens,
            "temperature": self.config.temperature,
        }
        if self.config.api_key:
            kwargs["api_key"] = self.config.api_key
        if self.config.api_base:
            kwargs["api_base"] = self.config.api_base

        try:
            response = litellm.completion(**kwargs)
            return response.choices[0].message.content.strip()
        except Exception as exc:
            logger.warning("LLM call failed: %s", exc)
            return None

    # ── High-level doc helpers (return None if LLM unavailable) ────────

    def generate_project_description(self, project_name: str,
                                     modules_summary: str,
                                     entry_points: str) -> Optional[str]:
        """Generate a concise project description from analysis data."""
        system = (
            "You are a technical writer generating concise project documentation. "
            "Write clear, factual descriptions. No marketing language. "
            "Output plain Markdown, 2-4 sentences."
        )
        prompt = (
            f"Project: {project_name}\n\n"
            f"Modules:\n{modules_summary}\n\n"
            f"Entry points:\n{entry_points}\n\n"
            "Write a concise description of what this project does and how to use it."
        )
        return self.complete(prompt, system)

    def generate_architecture_summary(self, project_name: str,
                                      layers: str,
                                      patterns: str,
                                      metrics: str) -> Optional[str]:
        """Generate a natural-language architecture overview."""
        system = (
            "You are a software architect explaining a codebase. "
            "Be precise and concise. Use technical terms correctly. "
            "Output plain Markdown, 3-6 sentences."
        )
        prompt = (
            f"Project: {project_name}\n\n"
            f"Architecture layers:\n{layers}\n\n"
            f"Detected patterns:\n{patterns}\n\n"
            f"Metrics:\n{metrics}\n\n"
            "Write a concise architecture overview explaining how the components "
            "work together and the key design decisions."
        )
        return self.complete(prompt, system)

    def generate_getting_started_summary(self, project_name: str,
                                         cli_commands: str,
                                         public_api: str) -> Optional[str]:
        """Generate a getting-started introduction."""
        system = (
            "You are writing a getting-started guide for developers. "
            "Be practical and action-oriented. "
            "Output plain Markdown, 2-4 sentences."
        )
        prompt = (
            f"Project: {project_name}\n\n"
            f"CLI commands:\n{cli_commands}\n\n"
            f"Public API:\n{public_api}\n\n"
            "Write a brief introduction explaining what the user will learn "
            "and what they can do with this tool."
        )
        return self.complete(prompt, system)

    def enhance_module_docstring(self, module_name: str,
                                 functions: str,
                                 classes: str) -> Optional[str]:
        """Generate a module-level summary from its contents."""
        system = (
            "You are a technical writer documenting a Python module. "
            "Be concise. Output 1-2 sentences of plain text (no Markdown)."
        )
        prompt = (
            f"Module: {module_name}\n\n"
            f"Functions:\n{functions}\n\n"
            f"Classes:\n{classes}\n\n"
            "Write a one-line summary of what this module does."
        )
        return self.complete(prompt, system)
