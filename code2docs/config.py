"""Configuration for code2docs documentation generation."""
import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import List
import yaml
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

@dataclass
class ReadmeConfig:
    """Configuration for README generation."""
    sections: List[str] = field(default_factory=lambda: ['overview', 'install', 'quickstart', 'architecture', 'api', 'structure', 'requirements', 'endpoints', 'contributing', 'docs_nav'])
    badges: List[str] = field(default_factory=lambda: ['version', 'python', 'coverage', 'complexity'])
    sync_markers: bool = True

@dataclass
class DocsConfig:
    """Configuration for docs/ generation."""
    api_reference: bool = True
    module_docs: bool = True
    architecture: bool = True
    changelog: bool = True

@dataclass
class ExamplesConfig:
    """Configuration for examples/ generation."""
    auto_generate: bool = True
    from_entry_points: bool = True

@dataclass
class SyncConfig:
    """Configuration for synchronization."""
    strategy: str = 'markers'
    watch: bool = False
    ignore: List[str] = field(default_factory=lambda: ['tests/', '__pycache__'])

@dataclass
class Code2LlmConfig:
    """Configuration for code2llm analysis generation."""
    enabled: bool = True
    formats: List[str] = field(default_factory=lambda: ['all'])
    strategy: str = 'standard'
    output_dir: str = 'project'
    chunk: bool = False
    no_png: bool = True
    max_depth: int = 6
    exclude_patterns: List[str] = field(default_factory=lambda: ['venv', '.venv', 'env', '.env', 'node_modules', 'bower_components', '__pycache__', '.pytest_cache', '.mypy_cache', '.git', '.hg', '.svn', 'dist', 'build', 'target', 'out', '.tox', '.eggs', '*.egg-info', 'vendor', 'third_party', 'third-party', 'site-packages', 'lib/python*'])

@dataclass
class LLMConfig:
    """Configuration for optional LLM-assisted documentation generation."""
    enabled: bool = False
    model: str = ''
    api_key: str = ''
    api_base: str = ''
    max_tokens: int = 1024
    temperature: float = 0.3

    @classmethod
    def from_env(cls) -> 'LLMConfig':
        """Build LLMConfig from environment variables."""
        model = os.environ.get('CODE2DOCS_LLM_MODEL', '')
        api_key = os.environ.get('CODE2DOCS_LLM_API_KEY', '')
        api_base = os.environ.get('CODE2DOCS_LLM_API_BASE', '')
        max_tokens = int(os.environ.get('CODE2DOCS_LLM_MAX_TOKENS', '1024'))
        temperature = float(os.environ.get('CODE2DOCS_LLM_TEMPERATURE', '0.3'))
        enabled = bool(model)
        return cls(enabled=enabled, model=model, api_key=api_key, api_base=api_base, max_tokens=max_tokens, temperature=temperature)

@dataclass
class Code2DocsConfig:
    """Main configuration for code2docs."""
    project_name: str = ''
    source: str = './'
    output: str = './docs/'
    readme_output: str = './README.md'
    repo_url: str = ''
    org_name: str = ''
    readme: ReadmeConfig = field(default_factory=ReadmeConfig)
    docs: DocsConfig = field(default_factory=DocsConfig)
    examples: ExamplesConfig = field(default_factory=ExamplesConfig)
    sync: SyncConfig = field(default_factory=SyncConfig)
    llm: LLMConfig = field(default_factory=LLMConfig.from_env)
    code2llm: Code2LlmConfig = field(default_factory=Code2LlmConfig)
    verbose: bool = False
    exclude_tests: bool = True
    skip_private: bool = False

    def __post_init__(self):
        """Auto-detect repo_url from git remote if not set."""
        if not self.repo_url:
            self.repo_url = self._detect_repo_url()

    @staticmethod
    def _detect_repo_url() -> str:
        """Try to detect repository URL from git remote origin."""
        try:
            url = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], stderr=subprocess.DEVNULL, text=True).strip()
            if url.startswith('git@'):
                url = url.replace(':', '/', 1).replace('git@', 'https://', 1)
            url = url.removesuffix('.git')
            return url
        except (subprocess.CalledProcessError, FileNotFoundError):
            return ''

    @classmethod
    def from_yaml(cls, path: str) -> 'Code2DocsConfig':
        """Load configuration from code2docs.yaml."""
        config_path = Path(path)
        if not config_path.exists():
            return cls()
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}
        config = cls()
        project = data.get('project', {})
        config.project_name = project.get('name', '')
        config.source = project.get('source', './')
        config.output = project.get('output', './docs/')
        config.readme_output = project.get('readme_output', './README.md')
        config.verbose = project.get('verbose', False)
        config.exclude_tests = project.get('exclude_tests', True)
        config.skip_private = project.get('skip_private', False)
        if project.get('repo_url'):
            config.repo_url = project['repo_url']
        readme_data = data.get('readme', {})
        if readme_data:
            config.readme = ReadmeConfig(sections=readme_data.get('sections', config.readme.sections), badges=readme_data.get('badges', config.readme.badges), sync_markers=readme_data.get('sync_markers', True))
        docs_data = data.get('docs', {})
        if docs_data:
            config.docs = DocsConfig(api_reference=docs_data.get('api_reference', True), module_docs=docs_data.get('module_docs', True), architecture=docs_data.get('architecture', True), changelog=docs_data.get('changelog', True))
        examples_data = data.get('examples', {})
        if examples_data:
            config.examples = ExamplesConfig(auto_generate=examples_data.get('auto_generate', True), from_entry_points=examples_data.get('from_entry_points', True))
        sync_data = data.get('sync', {})
        if sync_data:
            config.sync = SyncConfig(strategy=sync_data.get('strategy', 'markers'), watch=sync_data.get('watch', False), ignore=sync_data.get('ignore', ['tests/', '__pycache__']))
        llm_data = data.get('llm', {})
        if llm_data:
            env_llm = config.llm
            config.llm = LLMConfig(enabled=llm_data.get('enabled', env_llm.enabled), model=llm_data.get('model', env_llm.model), api_key=llm_data.get('api_key', env_llm.api_key), api_base=llm_data.get('api_base', env_llm.api_base), max_tokens=llm_data.get('max_tokens', env_llm.max_tokens), temperature=llm_data.get('temperature', env_llm.temperature))
        code2llm_data = data.get('code2llm', {})
        if code2llm_data:
            config.code2llm = Code2LlmConfig(enabled=code2llm_data.get('enabled', True), formats=code2llm_data.get('formats', ['all']), strategy=code2llm_data.get('strategy', 'standard'), output_dir=code2llm_data.get('output_dir', 'project'), chunk=code2llm_data.get('chunk', False), no_png=code2llm_data.get('no_png', True), max_depth=code2llm_data.get('max_depth', 3), exclude_patterns=code2llm_data.get('exclude_patterns', ['venv', '.venv', 'env', '.env', 'node_modules', 'bower_components', '__pycache__', '.pytest_cache', '.mypy_cache', '.git', '.hg', '.svn', 'dist', 'build', 'target', 'out', '.tox', '.eggs', '*.egg-info', 'vendor', 'third_party', 'third-party', 'site-packages', 'lib/python*']))
        return config

    def to_yaml(self, path: str) -> None:
        """Save configuration to YAML file."""
        data = {'project': {'name': self.project_name, 'source': self.source, 'output': self.output, 'readme_output': self.readme_output, 'repo_url': self.repo_url, 'verbose': self.verbose, 'exclude_tests': self.exclude_tests, 'skip_private': self.skip_private}, 'readme': {'sections': self.readme.sections, 'badges': self.readme.badges, 'sync_markers': self.readme.sync_markers}, 'docs': {'api_reference': self.docs.api_reference, 'module_docs': self.docs.module_docs, 'architecture': self.docs.architecture, 'changelog': self.docs.changelog}, 'examples': {'auto_generate': self.examples.auto_generate, 'from_entry_points': self.examples.from_entry_points}, 'sync': {'strategy': self.sync.strategy, 'watch': self.sync.watch, 'ignore': self.sync.ignore}, 'llm': {'enabled': self.llm.enabled, 'model': self.llm.model, 'api_base': self.llm.api_base, 'max_tokens': self.llm.max_tokens, 'temperature': self.llm.temperature}, 'code2llm': {'enabled': self.code2llm.enabled, 'formats': self.code2llm.formats, 'strategy': self.code2llm.strategy, 'output_dir': self.code2llm.output_dir, 'chunk': self.code2llm.chunk, 'no_png': self.code2llm.no_png, 'max_depth': self.code2llm.max_depth, 'exclude_patterns': self.code2llm.exclude_patterns}}
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)