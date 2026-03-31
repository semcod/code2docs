# System Architecture Analysis

## Overview

- **Project**: /home/tom/github/wronai/code2docs
- **Primary Language**: python
- **Languages**: python: 54, shell: 1
- **Analysis Mode**: static
- **Total Functions**: 298
- **Total Classes**: 60
- **Modules**: 55
- **Entry Points**: 281

## Architecture by Module

### code2docs.generators._registry_adapters
- **Functions**: 31
- **Classes**: 15
- **File**: `_registry_adapters.py`

### code2docs.generators.readme_gen
- **Functions**: 18
- **Classes**: 1
- **File**: `readme_gen.py`

### code2docs.generators.examples_gen
- **Functions**: 15
- **Classes**: 1
- **File**: `examples_gen.py`

### code2docs.cli
- **Functions**: 14
- **Classes**: 1
- **File**: `cli.py`

### code2docs.formatters.markdown
- **Functions**: 13
- **Classes**: 1
- **File**: `markdown.py`

### examples.05_custom_generators
- **Functions**: 13
- **Classes**: 3
- **File**: `05_custom_generators.py`

### code2docs.generators.org_readme_gen
- **Functions**: 10
- **Classes**: 1
- **File**: `org_readme_gen.py`

### code2docs.generators.architecture_gen
- **Functions**: 10
- **Classes**: 1
- **File**: `architecture_gen.py`

### code2docs.analyzers.docstring_extractor
- **Functions**: 10
- **Classes**: 2
- **File**: `docstring_extractor.py`

### code2docs.analyzers.dependency_scanner
- **Functions**: 10
- **Classes**: 3
- **File**: `dependency_scanner.py`

### code2docs.generators.depgraph_gen
- **Functions**: 9
- **Classes**: 1
- **File**: `depgraph_gen.py`

### code2docs.generators.module_docs_gen
- **Functions**: 9
- **Classes**: 1
- **File**: `module_docs_gen.py`

### code2docs.generators.api_changelog_gen
- **Functions**: 9
- **Classes**: 2
- **File**: `api_changelog_gen.py`

### code2docs.generators.getting_started_gen
- **Functions**: 8
- **Classes**: 1
- **File**: `getting_started_gen.py`

### code2docs.generators.contributing_gen
- **Functions**: 8
- **Classes**: 1
- **File**: `contributing_gen.py`

### code2docs.sync.differ
- **Functions**: 7
- **Classes**: 2
- **File**: `differ.py`

### code2docs.generators.coverage_gen
- **Functions**: 7
- **Classes**: 1
- **File**: `coverage_gen.py`

### code2docs.generators.api_reference_gen
- **Functions**: 7
- **Classes**: 1
- **File**: `api_reference_gen.py`

### code2docs.llm_helper
- **Functions**: 7
- **Classes**: 1
- **File**: `llm_helper.py`

### code2docs.generators._source_links
- **Functions**: 6
- **Classes**: 1
- **File**: `_source_links.py`

## Key Entry Points

Main execution flows into the system:

### code2docs.generators.examples_gen.ExamplesGenerator._generate_advanced
> Generate advanced_usage.py — individual generator usage, sync, etc.
- **Calls**: self._find_generator_classes, self._find_class_by_name, lines.append, None.join, lines.append, lines.append, lines.append, lines.append

### code2docs.config.Code2DocsConfig.from_yaml
> Load configuration from code2docs.yaml.
- **Calls**: Path, cls, data.get, project.get, project.get, project.get, project.get, project.get

### code2docs.generators.examples_gen.ExamplesGenerator._generate_quickstart
> Generate quickstart.py — minimal working example.
- **Calls**: self._find_convenience_functions, self._find_api_classes, set, lines.extend, lines.append, self._find_class_by_name, lines.append, lines.append

### code2docs.generators.architecture_gen.ArchitectureGenerator.generate
> Generate architecture documentation.
- **Calls**: lines.append, self._generate_llm_summary, lines.append, self._detect_layers, lines.append, lines.append, lines.append, lines.append

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_module_section
> Render a module as a subsection within the consolidated doc.
- **Calls**: self._linker.file_link, None.join, lines.append, lines.append, sorted, lines.append, sorted, lines.append

### code2docs.generators.readme_gen.ReadmeGenerator._extract_project_metadata
> Extract project metadata (author, license, version) from pyproject.toml or git.
- **Calls**: Path, Path, license_path.exists, pyproject_path.exists, subprocess.run, subprocess.run, subprocess.run, Path

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_module_detail
> Render a single module's detail section.
- **Calls**: self._linker.file_link, self._get_module_docstring, None.join, lines.append, sorted, sorted, lines.append, self.result.classes.items

### examples.06_formatters.generate_complex_document
> Generate a complex markdown document using the formatter.
- **Calls**: MarkdownFormatter, sections.append, sections.append, sections.append, sections.append, sections.append, sections.append, sections.append

### code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate
> Generate a single modules.md with all modules grouped by package.
- **Calls**: lines.append, lines.append, lines.append, sorted, lines.append, self._group_modules, groups.items, None.join

### examples.06_formatters.markdown_formatting_examples
> Demonstrate markdown formatting utilities.
- **Calls**: MarkdownFormatter, print, print, print, print, print, print, print

### code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_classes
> Diff class definitions.
- **Calls**: set, set, old.get, new.get, old.keys, new.keys, changes.append, ApiChange

### code2docs.generators.contributing_gen.ContributingGenerator._render_code_style
> Render code style guidelines.
- **Calls**: tools.get, None.join, tools.get, tools.get, tools.get, lines.append, lines.append, lines.append

### examples.06_formatters.build_custom_readme
> Build a custom README using formatters.
- **Calls**: MarkdownFormatter, parts.append, parts.append, parts.append, parts.append, parts.append, parts.append, None.join

### examples.05_custom_generators.MetricsReportGenerator.generate
> Generate the metrics report.
- **Calls**: lines.append, lines.append, lines.append, lines.append, lines.append, self._calculate_stats, lines.append, lines.append

### code2docs.generators.org_readme_gen.OrgReadmeGenerator._extract_description
> Extract short description from project (max 5 lines).
- **Calls**: result.modules.values, readme.exists, pyproject.exists, hasattr, self._truncate_description, readme.read_text, content.split, enumerate

### code2docs.generators._registry_adapters.IndexHtmlAdapter._generate_html
- **Calls**: None.exists, None.exists, None.exists, None.exists, None.exists, None.exists, None.exists, None.exists

### code2docs.generators.readme_gen.ReadmeGenerator._build_context
> Build template context from analysis result.
- **Calls**: DependencyScanner, dep_scanner.scan, EndpointDetector, endpoint_detector.detect, self._calc_avg_complexity, self._build_module_tree, self._generate_description, self._extract_project_metadata

### code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate
> Generate a single api.md with all public API grouped by package.
- **Calls**: len, len, self._group_modules, lines.append, groups.items, lines.append, groups.items, None.join

### examples.04_sync_and_watch.custom_watcher_with_hooks
> Set up a custom watcher with pre/post generation hooks.
- **Calls**: Code2DocsConfig, signal.signal, Differ, Updater, print, print, print, print

### code2docs.sync.updater.Updater.apply
> Regenerate documentation for changed modules.
- **Calls**: None.resolve, ProjectScanner, scanner.analyze, ReadmeGenerator, readme_gen.generate, readme_gen.write, docs_dir.mkdir, Differ

### code2docs.generators.architecture_gen.ArchitectureGenerator._generate_metrics_table
> Generate metrics summary table.
- **Calls**: stats.get, lines.append, None.join, f.complexity.get, round, lines.append, lines.append, f.complexity.get

### code2docs.generators.code2llm_gen.Code2LlmGenerator._run_code2llm
> Execute code2llm CLI with appropriate options.
- **Calls**: code2docs.generators.code2llm_gen.parse_gitignore, subprocess.run, str, None.join, str, str, cmd.append, cmd.append

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject
> Parse pyproject.toml for dependencies.
- **Calls**: ProjectDependencies, data.get, project.get, project.get, project.get, project.get, project.get, project.get

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_package_json
> Parse package.json for dependencies.
- **Calls**: ProjectDependencies, data.get, data.get, data.get, engines.get, None.items, None.items, lock_pnpm.exists

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_go_mod
> Parse go.mod for Go dependencies.
- **Calls**: ProjectDependencies, path.read_text, re.search, re.search, re.finditer, go_ver.group, None.splitlines, deps.dependencies.append

### code2docs.sync.differ.Differ.detect_changes
> Compare current file hashes with saved state. Return list of changes.
- **Calls**: None.resolve, self._load_state, self._compute_state, new_state.items, old_state.items, old_state.get, Path, changes.append

### code2docs.generators.config_docs_gen.ConfigDocsGenerator._render_section
> Render a dataclass as a Markdown table.
- **Calls**: fields, None.join, getattr, type_str.replace, isinstance, self._FIELD_DOCS.get, lines.append, str

### code2docs.generators.architecture_gen.ArchitectureGenerator._generate_class_diagram
> Generate Mermaid class diagram for key classes.
- **Calls**: lines.append, None.join, sorted, lines.append, lines.append, self.result.classes.values, len, lines.append

### examples.03_programmatic_api.inspect_project_structure
> Inspect project structure from analysis.
- **Calls**: code2docs.analyzers.project_scanner.ProjectScanner.analyze, print, print, print, print, print, print, result.functions.items

### code2docs.generators.getting_started_gen.GettingStartedGenerator._render_first_usage
> Render first usage example — CLI + Python API.
- **Calls**: public_funcs.sort, lines.append, None.join, None.join, lines.append, lines.append, lines.append, lines.append

## Process Flows

Key execution flows identified:

### Flow 1: _generate_advanced
```
_generate_advanced [code2docs.generators.examples_gen.ExamplesGenerator]
```

### Flow 2: from_yaml
```
from_yaml [code2docs.config.Code2DocsConfig]
```

### Flow 3: _generate_quickstart
```
_generate_quickstart [code2docs.generators.examples_gen.ExamplesGenerator]
```

### Flow 4: generate
```
generate [code2docs.generators.architecture_gen.ArchitectureGenerator]
```

### Flow 5: _render_module_section
```
_render_module_section [code2docs.generators.api_reference_gen.ApiReferenceGenerator]
```

### Flow 6: _extract_project_metadata
```
_extract_project_metadata [code2docs.generators.readme_gen.ReadmeGenerator]
```

### Flow 7: _render_module_detail
```
_render_module_detail [code2docs.generators.module_docs_gen.ModuleDocsGenerator]
```

### Flow 8: generate_complex_document
```
generate_complex_document [examples.06_formatters]
```

### Flow 9: markdown_formatting_examples
```
markdown_formatting_examples [examples.06_formatters]
```

### Flow 10: _diff_classes
```
_diff_classes [code2docs.generators.api_changelog_gen.ApiChangelogGenerator]
```

## Key Classes

### code2docs.generators.readme_gen.ReadmeGenerator
> Generate README.md from AnalysisResult.
- **Methods**: 17
- **Key Methods**: code2docs.generators.readme_gen.ReadmeGenerator.__init__, code2docs.generators.readme_gen.ReadmeGenerator.generate, code2docs.generators.readme_gen.ReadmeGenerator._build_context, code2docs.generators.readme_gen.ReadmeGenerator._calc_avg_complexity, code2docs.generators.readme_gen.ReadmeGenerator._build_module_tree, code2docs.generators.readme_gen.ReadmeGenerator._generate_description, code2docs.generators.readme_gen.ReadmeGenerator._extract_project_description, code2docs.generators.readme_gen.ReadmeGenerator._extract_project_metadata, code2docs.generators.readme_gen.ReadmeGenerator._extract_extras, code2docs.generators.readme_gen.ReadmeGenerator._build_manual

### code2docs.generators.examples_gen.ExamplesGenerator
> Generate examples/ — usage examples from public API signatures.
- **Methods**: 15
- **Key Methods**: code2docs.generators.examples_gen.ExamplesGenerator.__init__, code2docs.generators.examples_gen.ExamplesGenerator._get_example_value, code2docs.generators.examples_gen.ExamplesGenerator.generate_all, code2docs.generators.examples_gen.ExamplesGenerator._generate_quickstart, code2docs.generators.examples_gen.ExamplesGenerator._generate_advanced, code2docs.generators.examples_gen.ExamplesGenerator._detect_package_name, code2docs.generators.examples_gen.ExamplesGenerator._find_convenience_functions, code2docs.generators.examples_gen.ExamplesGenerator._find_api_classes, code2docs.generators.examples_gen.ExamplesGenerator._find_generator_classes, code2docs.generators.examples_gen.ExamplesGenerator._find_function_by_name

### code2docs.formatters.markdown.MarkdownFormatter
> Helper for constructing Markdown documents.
- **Methods**: 13
- **Key Methods**: code2docs.formatters.markdown.MarkdownFormatter.__init__, code2docs.formatters.markdown.MarkdownFormatter.heading, code2docs.formatters.markdown.MarkdownFormatter.paragraph, code2docs.formatters.markdown.MarkdownFormatter.blockquote, code2docs.formatters.markdown.MarkdownFormatter.code_block, code2docs.formatters.markdown.MarkdownFormatter.inline_code, code2docs.formatters.markdown.MarkdownFormatter.bold, code2docs.formatters.markdown.MarkdownFormatter.link, code2docs.formatters.markdown.MarkdownFormatter.list_item, code2docs.formatters.markdown.MarkdownFormatter.table

### code2docs.generators.org_readme_gen.OrgReadmeGenerator
> Generate organization README with list of projects and brief descriptions.
- **Methods**: 10
- **Key Methods**: code2docs.generators.org_readme_gen.OrgReadmeGenerator.__init__, code2docs.generators.org_readme_gen.OrgReadmeGenerator.generate, code2docs.generators.org_readme_gen.OrgReadmeGenerator._discover_projects, code2docs.generators.org_readme_gen.OrgReadmeGenerator._analyze_project, code2docs.generators.org_readme_gen.OrgReadmeGenerator._extract_description, code2docs.generators.org_readme_gen.OrgReadmeGenerator._truncate_description, code2docs.generators.org_readme_gen.OrgReadmeGenerator._get_version, code2docs.generators.org_readme_gen.OrgReadmeGenerator._get_repo_url, code2docs.generators.org_readme_gen.OrgReadmeGenerator._render_project_section, code2docs.generators.org_readme_gen.OrgReadmeGenerator.write

### code2docs.generators.architecture_gen.ArchitectureGenerator
> Generate docs/architecture.md — architecture overview with diagrams.
- **Methods**: 10
- **Key Methods**: code2docs.generators.architecture_gen.ArchitectureGenerator.__init__, code2docs.generators.architecture_gen.ArchitectureGenerator.generate, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_pipeline_overview, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_layer_diagram, code2docs.generators.architecture_gen.ArchitectureGenerator._get_public_entry_points, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_llm_summary, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_module_graph, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_class_diagram, code2docs.generators.architecture_gen.ArchitectureGenerator._detect_layers, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_metrics_table

### code2docs.analyzers.docstring_extractor.DocstringExtractor
> Extract and parse docstrings from AnalysisResult.
- **Methods**: 10
- **Key Methods**: code2docs.analyzers.docstring_extractor.DocstringExtractor.extract_all, code2docs.analyzers.docstring_extractor.DocstringExtractor.parse, code2docs.analyzers.docstring_extractor.DocstringExtractor._extract_summary, code2docs.analyzers.docstring_extractor.DocstringExtractor._classify_section, code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_sections, code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_param_line, code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_returns_line, code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_raises_line, code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_examples_line, code2docs.analyzers.docstring_extractor.DocstringExtractor.coverage_report

### code2docs.analyzers.dependency_scanner.DependencyScanner
> Scan and parse project dependency files.
- **Methods**: 10
- **Key Methods**: code2docs.analyzers.dependency_scanner.DependencyScanner.scan, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_package_json, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_cargo_toml, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_go_mod, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string, code2docs.analyzers.dependency_scanner.DependencyScanner._detect_version

### code2docs.generators.depgraph_gen.DepGraphGenerator
> Generate docs/dependency-graph.md with Mermaid diagrams.
- **Methods**: 9
- **Key Methods**: code2docs.generators.depgraph_gen.DepGraphGenerator.__init__, code2docs.generators.depgraph_gen.DepGraphGenerator.generate, code2docs.generators.depgraph_gen.DepGraphGenerator._collect_edges, code2docs.generators.depgraph_gen.DepGraphGenerator._extract_imports_from_file, code2docs.generators.depgraph_gen.DepGraphGenerator._import_matches, code2docs.generators.depgraph_gen.DepGraphGenerator._render_mermaid, code2docs.generators.depgraph_gen.DepGraphGenerator._render_matrix, code2docs.generators.depgraph_gen.DepGraphGenerator._calc_degrees, code2docs.generators.depgraph_gen.DepGraphGenerator._render_degree_table

### code2docs.generators.module_docs_gen.ModuleDocsGenerator
> Generate docs/modules.md — consolidated module documentation.
- **Methods**: 9
- **Key Methods**: code2docs.generators.module_docs_gen.ModuleDocsGenerator.__init__, code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate, code2docs.generators.module_docs_gen.ModuleDocsGenerator._group_modules, code2docs.generators.module_docs_gen.ModuleDocsGenerator._has_content, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_module_detail, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_public_methods, code2docs.generators.module_docs_gen.ModuleDocsGenerator._count_file_lines, code2docs.generators.module_docs_gen.ModuleDocsGenerator._calc_module_avg_cc, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_docstring

### code2docs.generators.api_changelog_gen.ApiChangelogGenerator
> Generate API changelog by diffing current analysis with a saved snapshot.
- **Methods**: 9
- **Key Methods**: code2docs.generators.api_changelog_gen.ApiChangelogGenerator.__init__, code2docs.generators.api_changelog_gen.ApiChangelogGenerator.generate, code2docs.generators.api_changelog_gen.ApiChangelogGenerator.save_snapshot, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._build_snapshot, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._load_snapshot, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_functions, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_classes, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._render

### code2docs.generators.getting_started_gen.GettingStartedGenerator
> Generate docs/getting-started.md from entry points and dependencies.
- **Methods**: 8
- **Key Methods**: code2docs.generators.getting_started_gen.GettingStartedGenerator.__init__, code2docs.generators.getting_started_gen.GettingStartedGenerator.generate, code2docs.generators.getting_started_gen.GettingStartedGenerator._render_prerequisites, code2docs.generators.getting_started_gen.GettingStartedGenerator._render_installation, code2docs.generators.getting_started_gen.GettingStartedGenerator._render_first_usage, code2docs.generators.getting_started_gen.GettingStartedGenerator._generate_intro, code2docs.generators.getting_started_gen.GettingStartedGenerator._render_next_steps, code2docs.generators.getting_started_gen.GettingStartedGenerator._get_top_level_modules

### code2docs.generators.contributing_gen.ContributingGenerator
> Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml.
- **Methods**: 8
- **Key Methods**: code2docs.generators.contributing_gen.ContributingGenerator.__init__, code2docs.generators.contributing_gen.ContributingGenerator.generate, code2docs.generators.contributing_gen.ContributingGenerator._detect_dev_tools, code2docs.generators.contributing_gen.ContributingGenerator._render_setup, code2docs.generators.contributing_gen.ContributingGenerator._render_development, code2docs.generators.contributing_gen.ContributingGenerator._render_testing, code2docs.generators.contributing_gen.ContributingGenerator._render_code_style, code2docs.generators.contributing_gen.ContributingGenerator._render_pull_request

### code2docs.generators.coverage_gen.CoverageGenerator
> Generate docs/coverage.md — docstring coverage report.
- **Methods**: 7
- **Key Methods**: code2docs.generators.coverage_gen.CoverageGenerator.__init__, code2docs.generators.coverage_gen.CoverageGenerator.generate, code2docs.generators.coverage_gen.CoverageGenerator._render_summary, code2docs.generators.coverage_gen.CoverageGenerator._render_per_module, code2docs.generators.coverage_gen.CoverageGenerator._collect_module_stats, code2docs.generators.coverage_gen.CoverageGenerator._format_coverage_table, code2docs.generators.coverage_gen.CoverageGenerator._render_undocumented

### code2docs.generators.api_reference_gen.ApiReferenceGenerator
> Generate docs/api.md — consolidated API reference.
- **Methods**: 7
- **Key Methods**: code2docs.generators.api_reference_gen.ApiReferenceGenerator.__init__, code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate, code2docs.generators.api_reference_gen.ApiReferenceGenerator._group_modules, code2docs.generators.api_reference_gen.ApiReferenceGenerator._has_content, code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_module_section, code2docs.generators.api_reference_gen.ApiReferenceGenerator._get_public_methods, code2docs.generators.api_reference_gen.ApiReferenceGenerator._format_signature

### code2docs.llm_helper.LLMHelper
> Thin wrapper around litellm for documentation generation.

If LLM is unavailable or disabled, every 
- **Methods**: 7
- **Key Methods**: code2docs.llm_helper.LLMHelper.__init__, code2docs.llm_helper.LLMHelper.available, code2docs.llm_helper.LLMHelper.complete, code2docs.llm_helper.LLMHelper.generate_project_description, code2docs.llm_helper.LLMHelper.generate_architecture_summary, code2docs.llm_helper.LLMHelper.generate_getting_started_summary, code2docs.llm_helper.LLMHelper.enhance_module_docstring

### code2docs.sync.differ.Differ
> Detect changes between current source and previous state.
- **Methods**: 6
- **Key Methods**: code2docs.sync.differ.Differ.__init__, code2docs.sync.differ.Differ.detect_changes, code2docs.sync.differ.Differ.save_state, code2docs.sync.differ.Differ._load_state, code2docs.sync.differ.Differ._compute_state, code2docs.sync.differ.Differ._file_to_module

### code2docs.generators._source_links.SourceLinker
> Build source-code links (relative paths + optional GitHub/GitLab URLs).
- **Methods**: 6
- **Key Methods**: code2docs.generators._source_links.SourceLinker.__init__, code2docs.generators._source_links.SourceLinker.source_link, code2docs.generators._source_links.SourceLinker.file_link, code2docs.generators._source_links.SourceLinker._relative_path, code2docs.generators._source_links.SourceLinker._find_git_root, code2docs.generators._source_links.SourceLinker._detect_branch

### code2docs.generators.changelog_gen.ChangelogGenerator
> Generate CHANGELOG.md from git log and analysis diff.
- **Methods**: 6
- **Key Methods**: code2docs.generators.changelog_gen.ChangelogGenerator.__init__, code2docs.generators.changelog_gen.ChangelogGenerator.generate, code2docs.generators.changelog_gen.ChangelogGenerator._get_git_log, code2docs.generators.changelog_gen.ChangelogGenerator._classify_message, code2docs.generators.changelog_gen.ChangelogGenerator._group_by_type, code2docs.generators.changelog_gen.ChangelogGenerator._render

### examples.05_custom_generators.MetricsReportGenerator
> Generate a metrics report from code analysis.
- **Methods**: 6
- **Key Methods**: examples.05_custom_generators.MetricsReportGenerator.__init__, examples.05_custom_generators.MetricsReportGenerator.generate, examples.05_custom_generators.MetricsReportGenerator._calculate_stats, examples.05_custom_generators.MetricsReportGenerator._format_stats_table, examples.05_custom_generators.MetricsReportGenerator._list_largest_files, examples.05_custom_generators.MetricsReportGenerator._analyze_functions

### code2docs.generators.mkdocs_gen.MkDocsGenerator
> Generate mkdocs.yml from the docs/ directory structure.
- **Methods**: 5
- **Key Methods**: code2docs.generators.mkdocs_gen.MkDocsGenerator.__init__, code2docs.generators.mkdocs_gen.MkDocsGenerator.generate, code2docs.generators.mkdocs_gen.MkDocsGenerator._read_pyproject_mkdocs, code2docs.generators.mkdocs_gen.MkDocsGenerator._build_nav, code2docs.generators.mkdocs_gen.MkDocsGenerator.write

## Data Transformation Functions

Key functions that process and transform data:

### code2docs.generators.coverage_gen.CoverageGenerator._format_coverage_table
> Format coverage stats as a Markdown table.
- **Output to**: None.join, lines.append

### code2docs.generators.code2llm_gen.parse_gitignore
> Parse .gitignore file and return list of patterns to exclude.

Filters out:
- Empty lines
- Comments
- **Output to**: gitignore_path.exists, gitignore_path.read_text, content.split, line.strip, line.startswith

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._format_signature
> Format a function signature string.
- **Output to**: None.join, len

### code2docs.cli.DefaultGroup.parse_args
- **Output to**: None.parse_args, super

### code2docs.analyzers.docstring_extractor.DocstringExtractor.parse
> Parse a docstring into structured sections (orchestrator).
- **Output to**: None.splitlines, DocstringInfo, self._extract_summary, self._parse_sections, DocstringInfo

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_sections
> Walk remaining lines, dispatching content to the right section.
- **Output to**: None.strip, line.strip, self._classify_section, desc_lines.append, None.join

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_param_line
> Parse a single param line: 'name: description'.
- **Output to**: line.split, pdesc.strip, pname.strip

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_returns_line
> Parse a returns line.

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_raises_line
> Parse a raises line.
- **Output to**: info.raises.append

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_examples_line
> Parse an examples line.
- **Output to**: info.examples.append

### code2docs.analyzers.endpoint_detector.EndpointDetector._parse_decorator
> Try to parse a route decorator string.
- **Output to**: self.FASTAPI_PATTERNS.search, self.FLASK_PATTERNS.search, Endpoint, Endpoint, None.upper

### examples.05_custom_generators.MetricsReportGenerator._format_stats_table
> Format statistics as markdown table.
- **Output to**: stats.items, None.join, lines.append

### examples.06_formatters.markdown_formatting_examples
> Demonstrate markdown formatting utilities.
- **Output to**: MarkdownFormatter, print, print, print, print

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject
> Parse pyproject.toml for dependencies.
- **Output to**: ProjectDependencies, data.get, project.get, project.get, project.get

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex
> Fallback regex-based pyproject.toml parser.
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.findall

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py
> Parse setup.py for dependencies (regex-based, no exec).
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.findall

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt
> Parse requirements.txt.
- **Output to**: ProjectDependencies, None.splitlines, line.strip, deps.dependencies.append, path.read_text

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_package_json
> Parse package.json for dependencies.
- **Output to**: ProjectDependencies, data.get, data.get, data.get, engines.get

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_cargo_toml
> Parse Cargo.toml for Rust dependencies.
- **Output to**: ProjectDependencies, path.read_text, re.search, content.splitlines, ver_match.group

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_go_mod
> Parse go.mod for Go dependencies.
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.finditer

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string
> Parse a dependency string like 'package>=1.0'.
- **Output to**: re.match, DependencyInfo, dep_str.strip, DependencyInfo, dep_str.strip

## Behavioral Patterns

### recursion_analyze
- **Type**: recursion
- **Confidence**: 0.90
- **Functions**: code2docs.analyzers.project_scanner.ProjectScanner.analyze

### state_machine_Differ
- **Type**: state_machine
- **Confidence**: 0.70
- **Functions**: code2docs.sync.differ.Differ.__init__, code2docs.sync.differ.Differ.detect_changes, code2docs.sync.differ.Differ.save_state, code2docs.sync.differ.Differ._load_state, code2docs.sync.differ.Differ._compute_state

## Public API Surface

Functions exposed as public API (no underscore prefix):

- `code2docs.config.Code2DocsConfig.from_yaml` - 53 calls
- `code2docs.generators.architecture_gen.ArchitectureGenerator.generate` - 42 calls
- `examples.06_formatters.generate_complex_document` - 32 calls
- `code2docs.sync.watcher.start_watcher` - 29 calls
- `code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate` - 29 calls
- `examples.06_formatters.markdown_formatting_examples` - 29 calls
- `examples.06_formatters.build_custom_readme` - 27 calls
- `examples.07_web_frameworks.generate_api_docs_from_endpoints` - 27 calls
- `examples.05_custom_generators.MetricsReportGenerator.generate` - 24 calls
- `code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate` - 20 calls
- `examples.04_sync_and_watch.custom_watcher_with_hooks` - 20 calls
- `code2docs.sync.updater.Updater.apply` - 19 calls
- `code2docs.sync.differ.Differ.detect_changes` - 16 calls
- `examples.03_programmatic_api.inspect_project_structure` - 16 calls
- `code2docs.generators.generate_docs` - 15 calls
- `code2docs.cli.generate` - 15 calls
- `code2docs.analyzers.dependency_scanner.DependencyScanner.scan` - 15 calls
- `examples.05_custom_generators.APIChangelogGenerator.generate` - 14 calls
- `code2docs.generators.config_docs_gen.ConfigDocsGenerator.generate` - 12 calls
- `examples.04_sync_and_watch.detect_changes_example` - 12 calls
- `examples.03_programmatic_api.generate_full_documentation` - 12 calls
- `code2docs.generators.code2llm_gen.parse_gitignore` - 11 calls
- `code2docs.generators._registry_adapters.ReadmeGeneratorAdapter.run` - 11 calls
- `code2docs.generators._registry_adapters.OrgReadmeAdapter.run` - 11 calls
- `examples.04_sync_and_watch.sync_with_git_changes` - 11 calls
- `code2docs.formatters.toc.extract_headings` - 10 calls
- `code2docs.cli.init` - 10 calls
- `examples.03_programmatic_api.generate_docs_if_needed` - 10 calls
- `code2docs.config.LLMConfig.from_env` - 9 calls
- `code2docs.generators.readme_gen.ReadmeGenerator.write` - 9 calls
- `examples.05_custom_generators.generate_custom_report` - 9 calls
- `examples.07_web_frameworks.document_web_project` - 9 calls
- `code2docs.formatters.markdown.MarkdownFormatter.table` - 8 calls
- `code2docs.generators.depgraph_gen.DepGraphGenerator.generate` - 8 calls
- `code2docs.generators.getting_started_gen.GettingStartedGenerator.generate` - 8 calls
- `code2docs.generators.code2llm_gen.Code2LlmGenerator.generate_all` - 8 calls
- `code2docs.generators.org_readme_gen.OrgReadmeGenerator.generate` - 8 calls
- `code2docs.cli.sync` - 8 calls
- `examples.03_programmatic_api.custom_documentation_pipeline` - 8 calls
- `code2docs.generators._registry_adapters.Code2LlmAdapter.run` - 7 calls

## System Interactions

How components interact:

```mermaid
graph TD
    _generate_advanced --> _find_generator_clas
    _generate_advanced --> _find_class_by_name
    _generate_advanced --> append
    _generate_advanced --> join
    from_yaml --> Path
    from_yaml --> cls
    from_yaml --> get
    _generate_quickstart --> _find_convenience_fu
    _generate_quickstart --> _find_api_classes
    _generate_quickstart --> set
    _generate_quickstart --> extend
    _generate_quickstart --> append
    generate --> append
    generate --> _generate_llm_summar
    generate --> _detect_layers
    _render_module_secti --> file_link
    _render_module_secti --> join
    _render_module_secti --> append
    _render_module_secti --> sorted
    _extract_project_met --> Path
    _extract_project_met --> exists
    _extract_project_met --> run
    _render_module_detai --> file_link
    _render_module_detai --> _get_module_docstrin
    _render_module_detai --> join
    _render_module_detai --> append
    _render_module_detai --> sorted
    generate_complex_doc --> MarkdownFormatter
    generate_complex_doc --> append
    generate --> sorted
```

## Reverse Engineering Guidelines

1. **Entry Points**: Start analysis from the entry points listed above
2. **Core Logic**: Focus on classes with many methods
3. **Data Flow**: Follow data transformation functions
4. **Process Flows**: Use the flow diagrams for execution paths
5. **API Surface**: Public API functions reveal the interface

## Context for LLM

Maintain the identified architectural patterns and public API surface when suggesting changes.