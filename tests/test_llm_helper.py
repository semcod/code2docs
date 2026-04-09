"""Tests for LLMHelper — mock litellm, verify fallback behavior."""

from unittest.mock import patch, MagicMock


from code2docs.config import LLMConfig, Code2DocsConfig
from code2docs.llm_helper import LLMHelper


# ── LLMConfig tests ──────────────────────────────────────────────────────


class TestLLMConfig:
    def test_defaults(self):
        cfg = LLMConfig()
        assert cfg.enabled is False
        assert cfg.model == ""
        assert cfg.api_key == ""
        assert cfg.max_tokens == 1024
        assert cfg.temperature == 0.3

    def test_from_env_no_vars(self):
        with patch.dict("os.environ", {}, clear=True):
            cfg = LLMConfig.from_env()
        assert cfg.enabled is False
        assert cfg.model == ""

    def test_from_env_with_model(self):
        env = {
            "CODE2DOCS_LLM_MODEL": "openai/gpt-5.4-mini",
            "CODE2DOCS_LLM_API_KEY": "sk-test123",
            "CODE2DOCS_LLM_MAX_TOKENS": "2048",
            "CODE2DOCS_LLM_TEMPERATURE": "0.5",
        }
        with patch.dict("os.environ", env, clear=True):
            cfg = LLMConfig.from_env()
        assert cfg.enabled is True
        assert cfg.model == "openai/gpt-5.4-mini"
        assert cfg.api_key == "sk-test123"
        assert cfg.max_tokens == 2048
        assert cfg.temperature == 0.5

    def test_from_env_with_api_base(self):
        env = {
            "CODE2DOCS_LLM_MODEL": "ollama/llama3",
            "CODE2DOCS_LLM_API_BASE": "http://localhost:11434",
        }
        with patch.dict("os.environ", env, clear=True):
            cfg = LLMConfig.from_env()
        assert cfg.enabled is True
        assert cfg.api_base == "http://localhost:11434"


# ── LLMHelper disabled tests ─────────────────────────────────────────────


class TestLLMHelperDisabled:
    """Test that LLMHelper returns None for everything when disabled."""

    def test_not_available_when_disabled(self):
        cfg = LLMConfig(enabled=False, model="openai/gpt-5.4-mini")
        helper = LLMHelper(cfg)
        assert helper.available is False

    def test_not_available_when_no_model(self):
        cfg = LLMConfig(enabled=True, model="")
        helper = LLMHelper(cfg)
        assert helper.available is False

    def test_complete_returns_none_when_disabled(self):
        cfg = LLMConfig(enabled=False)
        helper = LLMHelper(cfg)
        assert helper.complete("test prompt") is None

    def test_generate_project_description_returns_none(self):
        cfg = LLMConfig(enabled=False)
        helper = LLMHelper(cfg)
        assert helper.generate_project_description("proj", "mods", "eps") is None

    def test_generate_architecture_summary_returns_none(self):
        cfg = LLMConfig(enabled=False)
        helper = LLMHelper(cfg)
        assert helper.generate_architecture_summary("proj", "layers", "pat", "met") is None

    def test_generate_getting_started_returns_none(self):
        cfg = LLMConfig(enabled=False)
        helper = LLMHelper(cfg)
        assert helper.generate_getting_started_summary("proj", "cli", "api") is None

    def test_enhance_module_docstring_returns_none(self):
        cfg = LLMConfig(enabled=False)
        helper = LLMHelper(cfg)
        assert helper.enhance_module_docstring("mod", "funcs", "classes") is None


# ── LLMHelper enabled tests (mock litellm) ───────────────────────────────


class TestLLMHelperEnabled:
    """Test LLMHelper with mocked litellm."""

    @staticmethod
    def _make_helper():
        cfg = LLMConfig(
            enabled=True, model="openai/gpt-5.4-mini",
            api_key="sk-test", max_tokens=512, temperature=0.2,
        )
        return LLMHelper(cfg)

    @staticmethod
    def _mock_response(content: str):
        resp = MagicMock()
        resp.choices = [MagicMock()]
        resp.choices[0].message.content = content
        return resp

    def test_complete_calls_litellm(self):
        helper = self._make_helper()
        mock_litellm = MagicMock()
        mock_litellm.completion.return_value = self._mock_response("Hello world")

        with patch("code2docs.llm_helper._litellm", mock_litellm):
            with patch("code2docs.llm_helper._get_litellm", return_value=mock_litellm):
                helper._available = None  # reset cache
                result = helper.complete("test prompt", system="sys")

        assert result == "Hello world"
        mock_litellm.completion.assert_called_once()
        call_kwargs = mock_litellm.completion.call_args[1]
        assert call_kwargs["model"] == "openai/gpt-5.4-mini"
        assert call_kwargs["max_tokens"] == 512
        assert call_kwargs["temperature"] == 0.2
        assert len(call_kwargs["messages"]) == 2
        assert call_kwargs["messages"][0]["role"] == "system"

    def test_complete_returns_none_on_exception(self):
        helper = self._make_helper()
        mock_litellm = MagicMock()
        mock_litellm.completion.side_effect = Exception("API error")

        with patch("code2docs.llm_helper._litellm", mock_litellm):
            with patch("code2docs.llm_helper._get_litellm", return_value=mock_litellm):
                helper._available = None
                result = helper.complete("test prompt")

        assert result is None

    def test_generate_project_description_with_llm(self):
        helper = self._make_helper()
        mock_litellm = MagicMock()
        mock_litellm.completion.return_value = self._mock_response(
            "A CLI tool for auto-generating docs."
        )

        with patch("code2docs.llm_helper._litellm", mock_litellm):
            with patch("code2docs.llm_helper._get_litellm", return_value=mock_litellm):
                helper._available = None
                result = helper.generate_project_description("myproj", "cli, config", "main")

        assert result == "A CLI tool for auto-generating docs."

    def test_api_key_passed_when_set(self):
        cfg = LLMConfig(
            enabled=True, model="openai/gpt-5.4-mini",
            api_key="sk-secret", max_tokens=1024, temperature=0.3,
        )
        helper = LLMHelper(cfg)
        mock_litellm = MagicMock()
        mock_litellm.completion.return_value = self._mock_response("ok")

        with patch("code2docs.llm_helper._litellm", mock_litellm):
            with patch("code2docs.llm_helper._get_litellm", return_value=mock_litellm):
                helper._available = None
                helper.complete("test")

        call_kwargs = mock_litellm.completion.call_args[1]
        assert call_kwargs["api_key"] == "sk-secret"

    def test_api_base_passed_when_set(self):
        cfg = LLMConfig(
            enabled=True, model="ollama/llama3",
            api_base="http://localhost:11434",
            max_tokens=1024, temperature=0.3,
        )
        helper = LLMHelper(cfg)
        mock_litellm = MagicMock()
        mock_litellm.completion.return_value = self._mock_response("ok")

        with patch("code2docs.llm_helper._litellm", mock_litellm):
            with patch("code2docs.llm_helper._get_litellm", return_value=mock_litellm):
                helper._available = None
                helper.complete("test")

        call_kwargs = mock_litellm.completion.call_args[1]
        assert call_kwargs["api_base"] == "http://localhost:11434"

    def test_no_api_key_not_in_kwargs(self):
        cfg = LLMConfig(
            enabled=True, model="ollama/llama3",
            api_key="", max_tokens=1024, temperature=0.3,
        )
        helper = LLMHelper(cfg)
        mock_litellm = MagicMock()
        mock_litellm.completion.return_value = self._mock_response("ok")

        with patch("code2docs.llm_helper._litellm", mock_litellm):
            with patch("code2docs.llm_helper._get_litellm", return_value=mock_litellm):
                helper._available = None
                helper.complete("test")

        call_kwargs = mock_litellm.completion.call_args[1]
        assert "api_key" not in call_kwargs


# ── Integration: generators fall back when LLM disabled ───────────────────


class TestGeneratorFallback:
    """Verify generators work correctly without LLM (fallback to templates)."""

    def test_readme_without_llm(self):
        from code2docs.generators.readme_gen import ReadmeGenerator
        from code2llm.core.models import AnalysisResult, ModuleInfo

        result = AnalysisResult(project_path="/tmp/test")
        result.modules = {
            "mylib": ModuleInfo(
                name="mylib", file="/tmp/test/mylib/__init__.py",
                is_package=True,
            ),
        }
        cfg = LLMConfig(enabled=False)
        config = Code2DocsConfig(project_name="mylib", llm=cfg)
        gen = ReadmeGenerator(config, result)
        content = gen.generate()
        assert "mylib" in content
        assert "Installation" in content  # New default section instead of "How It Works"

    def test_architecture_without_llm(self):
        from code2docs.generators.architecture_gen import ArchitectureGenerator
        from code2llm.core.models import AnalysisResult, ModuleInfo

        result = AnalysisResult(project_path="/tmp/test")
        result.modules = {
            "mylib.core": ModuleInfo(
                name="mylib.core", file="/tmp/test/mylib/core.py",
            ),
        }
        cfg = LLMConfig(enabled=False)
        config = Code2DocsConfig(project_name="mylib", llm=cfg)
        gen = ArchitectureGenerator(config, result)
        content = gen.generate()
        assert "Architecture" in content
        assert "pipeline" in content.lower()

    def test_getting_started_without_llm(self):
        from code2docs.generators.getting_started_gen import GettingStartedGenerator
        from code2llm.core.models import AnalysisResult, ModuleInfo

        result = AnalysisResult(project_path="/tmp/test")
        result.modules = {
            "mylib": ModuleInfo(
                name="mylib", file="/tmp/test/mylib/__init__.py",
                is_package=True,
            ),
        }
        cfg = LLMConfig(enabled=False)
        config = Code2DocsConfig(project_name="mylib", llm=cfg)
        gen = GettingStartedGenerator(config, result)
        content = gen.generate()
        assert "Getting Started" in content
        assert "Installation" in content
