# System Architecture Analysis

## Overview

- **Project**: /home/tom/github/wronai/code2docs
- **Analysis Mode**: static
- **Total Functions**: 154
- **Total Classes**: 30
- **Modules**: 31
- **Entry Points**: 144

## Architecture by Module

### code2docs.generators.module_docs_gen
- **Functions**: 17
- **Classes**: 1
- **File**: `module_docs_gen.py`

### code2docs.generators.readme_gen
- **Functions**: 14
- **Classes**: 1
- **File**: `readme_gen.py`

### code2docs.formatters.markdown
- **Functions**: 13
- **Classes**: 1
- **File**: `markdown.py`

### code2docs.generators.examples_gen
- **Functions**: 12
- **Classes**: 1
- **File**: `examples_gen.py`

### code2docs.generators.api_reference_gen
- **Functions**: 11
- **Classes**: 1
- **File**: `api_reference_gen.py`

### code2docs.cli
- **Functions**: 10
- **Classes**: 1
- **File**: `cli.py`

### code2docs.generators.depgraph_gen
- **Functions**: 9
- **Classes**: 1
- **File**: `depgraph_gen.py`

### code2docs.generators.api_changelog_gen
- **Functions**: 9
- **Classes**: 2
- **File**: `api_changelog_gen.py`

### code2docs.sync.differ
- **Functions**: 7
- **Classes**: 2
- **File**: `differ.py`

### code2docs.generators.changelog_gen
- **Functions**: 6
- **Classes**: 2
- **File**: `changelog_gen.py`

### code2docs.generators.architecture_gen
- **Functions**: 6
- **Classes**: 1
- **File**: `architecture_gen.py`

### code2docs.analyzers.dependency_scanner
- **Functions**: 6
- **Classes**: 3
- **File**: `dependency_scanner.py`

### code2docs.analyzers.docstring_extractor
- **Functions**: 6
- **Classes**: 2
- **File**: `docstring_extractor.py`

### code2docs.generators.coverage_gen
- **Functions**: 5
- **Classes**: 1
- **File**: `coverage_gen.py`

### code2docs.generators.mkdocs_gen
- **Functions**: 4
- **Classes**: 1
- **File**: `mkdocs_gen.py`

### code2docs.analyzers.project_scanner
- **Functions**: 4
- **Classes**: 1
- **File**: `project_scanner.py`

### code2docs.formatters.toc
- **Functions**: 3
- **File**: `toc.py`

### code2docs.analyzers.endpoint_detector
- **Functions**: 3
- **Classes**: 2
- **File**: `endpoint_detector.py`

### code2docs.sync.updater
- **Functions**: 2
- **Classes**: 1
- **File**: `updater.py`

### code2docs.formatters.badges
- **Functions**: 2
- **File**: `badges.py`

## Key Entry Points

Main execution flows into the system:

### code2docs.config.Code2DocsConfig.from_yaml
> Load configuration from code2docs.yaml.
- **Calls**: Path, cls, data.get, project.get, project.get, project.get, project.get, project.get

### code2docs.generators.architecture_gen.ArchitectureGenerator.generate
> Generate architecture documentation.
- **Calls**: lines.append, lines.append, lines.append, self._detect_layers, lines.append, lines.append, lines.append, lines.append

### code2docs.sync.updater.Updater.apply
> Regenerate documentation for changed modules.
- **Calls**: None.resolve, ProjectScanner, scanner.analyze, ReadmeGenerator, readme_gen.generate, readme_gen.write, Differ, differ.save_state

### code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_classes
> Diff class definitions.
- **Calls**: set, set, old.get, new.get, old.keys, new.keys, changes.append, ApiChange

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_classes_section
> Render classes and their method tables.
- **Calls**: self._get_module_classes, module_classes.items, None.join, lines.append, self._get_class_methods, lines.append, lines.append, lines.append

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_api_classes
> Render classes with their method signatures.
- **Calls**: sorted, None.join, module_classes.items, lines.append, self._get_class_methods, self.result.classes.items, lines.append, lines.append

### code2docs.generators.architecture_gen.ArchitectureGenerator._generate_metrics_table
> Generate metrics summary table.
- **Calls**: stats.get, lines.append, None.join, f.complexity.get, round, lines.append, lines.append, self.result.functions.values

### code2docs.sync.differ.Differ.detect_changes
> Compare current file hashes with saved state. Return list of changes.
- **Calls**: None.resolve, self._load_state, self._compute_state, new_state.items, old_state.items, old_state.get, Path, changes.append

### code2docs.generators.mkdocs_gen.MkDocsGenerator._build_nav
> Build navigation structure from docs tree and analysis.
- **Calls**: nav.append, nav.append, nav.append, sorted, nav.append, sorted, nav.append, self.result.modules.keys

### code2docs.generators.examples_gen.ExamplesGenerator._generate_class_examples
> Generate examples for major classes.
- **Calls**: lines.append, lines.append, None.join, lines.append, lines.append, self._get_init_args, self._get_public_methods, lines.append

### code2docs.generators.architecture_gen.ArchitectureGenerator._generate_class_diagram
> Generate Mermaid class diagram for key classes.
- **Calls**: lines.append, None.join, sorted, lines.append, lines.append, self.result.classes.values, len, lines.append

### code2docs.generators.generate_docs
> High-level function to generate all documentation.
- **Calls**: ProjectScanner, scanner.analyze, None.generate, None.generate, None.generate, Code2DocsConfig, None.generate_all, None.generate_all

### code2docs.generators.coverage_gen.CoverageGenerator._render_per_module
> Render per-module coverage table.
- **Calls**: sorted, None.join, self.result.modules.keys, rows.append, len, len, sum, sum

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_api_functions
> Render standalone functions with signatures and complexity.
- **Calls**: sorted, None.join, module_functions.items, self._format_signature, lines.append, func_info.complexity.get, lines.append, self.result.functions.items

### code2docs.generators.readme_gen.ReadmeGenerator._build_api_section
> Build API overview section with classes and functions.
- **Calls**: parts.append, parts.append, None.join, list, parts.append, list, None.join, parts.append

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_metrics
- **Calls**: self._count_file_lines, self._calc_module_avg_cc, str, str, self.result.functions.values, str, str, len

### code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_functions
> Diff function signatures.
- **Calls**: set, set, old.get, new.get, old.keys, new.keys, None.get, changes.append

### code2docs.cli.generate
> Generate documentation (default command).
- **Calls**: main.command, click.argument, click.option, click.option, click.option, click.option, click.option, click.option

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject
> Parse pyproject.toml for dependencies.
- **Calls**: ProjectDependencies, data.get, project.get, project.get, None.items, project.get, self._parse_pyproject_regex, open

### code2docs.generators.depgraph_gen.DepGraphGenerator._render_matrix
> Render a coupling matrix as a Markdown table.
- **Calls**: sorted, set, None.join, self.result.modules.keys, rows.append, m.split, None.join, None.join

### code2docs.generators.api_changelog_gen.ApiChangelogGenerator._render
> Render changelog as Markdown.
- **Calls**: lines.append, None.join, lines.append, None.join, lines.append, None.join, lines.append, lines.append

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_sections
> Walk remaining lines, dispatching content to the right section.
- **Calls**: None.strip, line.strip, self._classify_section, desc_lines.append, None.join, stripped.startswith, info.examples.append, stripped.split

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_index
> Generate API index page.
- **Calls**: sorted, self.result.modules.keys, None.replace, len, len, lines.append, None.join, len

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_functions_section
> Render standalone functions with signatures and call info.
- **Calls**: self._get_module_functions, module_functions.items, None.join, None.join, lines.append, lines.append, lines.append, lines.append

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_dependencies_section
> Render imports split into internal and stdlib.
- **Calls**: None.join, lines.append, sorted, lines.append, lines.append, sorted, lines.append, i.startswith

### code2docs.generators.examples_gen.ExamplesGenerator._generate_entry_point_examples
> Generate examples based on entry points.
- **Calls**: None.join, self.result.functions.get, Path, lines.append, lines.append, None.join, lines.append, lines.append

### code2docs.generators.architecture_gen.ArchitectureGenerator._generate_module_graph
> Generate Mermaid module dependency graph.
- **Calls**: set, self.result.modules.items, sorted, lines.append, None.join, lines.append, lines.append, mod_name.split

### code2docs.generators.changelog_gen.ChangelogGenerator._render
> Render grouped changelog to Markdown.
- **Calls**: self.CONVENTIONAL_TYPES.items, grouped.get, None.join, grouped.get, lines.append, lines.append, lines.append, lines.append

### code2docs.generators.examples_gen.ExamplesGenerator._generate_class_usage_section
> Generate class instantiation and method call examples.
- **Calls**: lines.append, self._get_init_args, lines.append, self._get_public_methods, None.join, None.join, lines.append, lines.append

### code2docs.generators.architecture_gen.ArchitectureGenerator._detect_layers
> Detect architectural layers from module names.
- **Calls**: sorted, self.result.modules.keys, mod_name.lower, layer_keywords.items, any, None.append, layers.items, None.append

## Process Flows

Key execution flows identified:

### Flow 1: from_yaml
```
from_yaml [code2docs.config.Code2DocsConfig]
```

### Flow 2: generate
```
generate [code2docs.generators.architecture_gen.ArchitectureGenerator]
```

### Flow 3: apply
```
apply [code2docs.sync.updater.Updater]
```

### Flow 4: _diff_classes
```
_diff_classes [code2docs.generators.api_changelog_gen.ApiChangelogGenerator]
```

### Flow 5: _render_classes_section
```
_render_classes_section [code2docs.generators.module_docs_gen.ModuleDocsGenerator]
```

### Flow 6: _render_api_classes
```
_render_api_classes [code2docs.generators.api_reference_gen.ApiReferenceGenerator]
```

### Flow 7: _generate_metrics_table
```
_generate_metrics_table [code2docs.generators.architecture_gen.ArchitectureGenerator]
```

### Flow 8: detect_changes
```
detect_changes [code2docs.sync.differ.Differ]
```

### Flow 9: _build_nav
```
_build_nav [code2docs.generators.mkdocs_gen.MkDocsGenerator]
```

### Flow 10: _generate_class_examples
```
_generate_class_examples [code2docs.generators.examples_gen.ExamplesGenerator]
```

## Key Classes

### code2docs.generators.module_docs_gen.ModuleDocsGenerator
> Generate docs/modules/ — detailed per-module documentation.
- **Methods**: 17
- **Key Methods**: code2docs.generators.module_docs_gen.ModuleDocsGenerator.__init__, code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate_all, code2docs.generators.module_docs_gen.ModuleDocsGenerator._generate_module, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_header, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_overview, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_classes_section, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_functions_section, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_dependencies_section, code2docs.generators.module_docs_gen.ModuleDocsGenerator._render_metrics_section, code2docs.generators.module_docs_gen.ModuleDocsGenerator._count_file_lines

### code2docs.formatters.markdown.MarkdownFormatter
> Helper for constructing Markdown documents.
- **Methods**: 13
- **Key Methods**: code2docs.formatters.markdown.MarkdownFormatter.__init__, code2docs.formatters.markdown.MarkdownFormatter.heading, code2docs.formatters.markdown.MarkdownFormatter.paragraph, code2docs.formatters.markdown.MarkdownFormatter.blockquote, code2docs.formatters.markdown.MarkdownFormatter.code_block, code2docs.formatters.markdown.MarkdownFormatter.inline_code, code2docs.formatters.markdown.MarkdownFormatter.bold, code2docs.formatters.markdown.MarkdownFormatter.link, code2docs.formatters.markdown.MarkdownFormatter.list_item, code2docs.formatters.markdown.MarkdownFormatter.table

### code2docs.generators.readme_gen.ReadmeGenerator
> Generate README.md from AnalysisResult.
- **Methods**: 13
- **Key Methods**: code2docs.generators.readme_gen.ReadmeGenerator.__init__, code2docs.generators.readme_gen.ReadmeGenerator.generate, code2docs.generators.readme_gen.ReadmeGenerator._build_context, code2docs.generators.readme_gen.ReadmeGenerator._calc_avg_complexity, code2docs.generators.readme_gen.ReadmeGenerator._build_module_tree, code2docs.generators.readme_gen.ReadmeGenerator._build_manual, code2docs.generators.readme_gen.ReadmeGenerator._build_overview_section, code2docs.generators.readme_gen.ReadmeGenerator._build_install_section, code2docs.generators.readme_gen.ReadmeGenerator._build_quickstart_section, code2docs.generators.readme_gen.ReadmeGenerator._build_api_section

### code2docs.generators.examples_gen.ExamplesGenerator
> Generate examples/ — usage examples from public API signatures.
- **Methods**: 12
- **Key Methods**: code2docs.generators.examples_gen.ExamplesGenerator.__init__, code2docs.generators.examples_gen.ExamplesGenerator.generate_all, code2docs.generators.examples_gen.ExamplesGenerator._generate_basic_usage, code2docs.generators.examples_gen.ExamplesGenerator._generate_import_section, code2docs.generators.examples_gen.ExamplesGenerator._generate_class_usage_section, code2docs.generators.examples_gen.ExamplesGenerator._generate_function_usage_section, code2docs.generators.examples_gen.ExamplesGenerator._generate_entry_point_examples, code2docs.generators.examples_gen.ExamplesGenerator._generate_class_examples, code2docs.generators.examples_gen.ExamplesGenerator._get_major_classes, code2docs.generators.examples_gen.ExamplesGenerator._get_init_args

### code2docs.generators.api_reference_gen.ApiReferenceGenerator
> Generate docs/api/ — per-module API reference from signatures.
- **Methods**: 11
- **Key Methods**: code2docs.generators.api_reference_gen.ApiReferenceGenerator.__init__, code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate_all, code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_index, code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_module_api, code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_api_header, code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_api_classes, code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_api_functions, code2docs.generators.api_reference_gen.ApiReferenceGenerator._render_api_imports, code2docs.generators.api_reference_gen.ApiReferenceGenerator._get_class_methods, code2docs.generators.api_reference_gen.ApiReferenceGenerator._format_signature

### code2docs.generators.depgraph_gen.DepGraphGenerator
> Generate docs/dependency-graph.md with Mermaid diagrams.
- **Methods**: 9
- **Key Methods**: code2docs.generators.depgraph_gen.DepGraphGenerator.__init__, code2docs.generators.depgraph_gen.DepGraphGenerator.generate, code2docs.generators.depgraph_gen.DepGraphGenerator._collect_edges, code2docs.generators.depgraph_gen.DepGraphGenerator._extract_imports_from_file, code2docs.generators.depgraph_gen.DepGraphGenerator._import_matches, code2docs.generators.depgraph_gen.DepGraphGenerator._render_mermaid, code2docs.generators.depgraph_gen.DepGraphGenerator._render_matrix, code2docs.generators.depgraph_gen.DepGraphGenerator._calc_degrees, code2docs.generators.depgraph_gen.DepGraphGenerator._render_degree_table

### code2docs.generators.api_changelog_gen.ApiChangelogGenerator
> Generate API changelog by diffing current analysis with a saved snapshot.
- **Methods**: 9
- **Key Methods**: code2docs.generators.api_changelog_gen.ApiChangelogGenerator.__init__, code2docs.generators.api_changelog_gen.ApiChangelogGenerator.generate, code2docs.generators.api_changelog_gen.ApiChangelogGenerator.save_snapshot, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._build_snapshot, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._load_snapshot, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_functions, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._diff_classes, code2docs.generators.api_changelog_gen.ApiChangelogGenerator._render

### code2docs.sync.differ.Differ
> Detect changes between current source and previous state.
- **Methods**: 6
- **Key Methods**: code2docs.sync.differ.Differ.__init__, code2docs.sync.differ.Differ.detect_changes, code2docs.sync.differ.Differ.save_state, code2docs.sync.differ.Differ._load_state, code2docs.sync.differ.Differ._compute_state, code2docs.sync.differ.Differ._file_to_module

### code2docs.generators.changelog_gen.ChangelogGenerator
> Generate CHANGELOG.md from git log and analysis diff.
- **Methods**: 6
- **Key Methods**: code2docs.generators.changelog_gen.ChangelogGenerator.__init__, code2docs.generators.changelog_gen.ChangelogGenerator.generate, code2docs.generators.changelog_gen.ChangelogGenerator._get_git_log, code2docs.generators.changelog_gen.ChangelogGenerator._classify_message, code2docs.generators.changelog_gen.ChangelogGenerator._group_by_type, code2docs.generators.changelog_gen.ChangelogGenerator._render

### code2docs.generators.architecture_gen.ArchitectureGenerator
> Generate docs/architecture.md — architecture overview with diagrams.
- **Methods**: 6
- **Key Methods**: code2docs.generators.architecture_gen.ArchitectureGenerator.__init__, code2docs.generators.architecture_gen.ArchitectureGenerator.generate, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_module_graph, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_class_diagram, code2docs.generators.architecture_gen.ArchitectureGenerator._detect_layers, code2docs.generators.architecture_gen.ArchitectureGenerator._generate_metrics_table

### code2docs.analyzers.dependency_scanner.DependencyScanner
> Scan and parse project dependency files.
- **Methods**: 6
- **Key Methods**: code2docs.analyzers.dependency_scanner.DependencyScanner.scan, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string

### code2docs.analyzers.docstring_extractor.DocstringExtractor
> Extract and parse docstrings from AnalysisResult.
- **Methods**: 6
- **Key Methods**: code2docs.analyzers.docstring_extractor.DocstringExtractor.extract_all, code2docs.analyzers.docstring_extractor.DocstringExtractor.parse, code2docs.analyzers.docstring_extractor.DocstringExtractor._extract_summary, code2docs.analyzers.docstring_extractor.DocstringExtractor._classify_section, code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_sections, code2docs.analyzers.docstring_extractor.DocstringExtractor.coverage_report

### code2docs.generators.coverage_gen.CoverageGenerator
> Generate docs/coverage.md — docstring coverage report.
- **Methods**: 5
- **Key Methods**: code2docs.generators.coverage_gen.CoverageGenerator.__init__, code2docs.generators.coverage_gen.CoverageGenerator.generate, code2docs.generators.coverage_gen.CoverageGenerator._render_summary, code2docs.generators.coverage_gen.CoverageGenerator._render_per_module, code2docs.generators.coverage_gen.CoverageGenerator._render_undocumented

### code2docs.generators.mkdocs_gen.MkDocsGenerator
> Generate mkdocs.yml from the docs/ directory structure.
- **Methods**: 4
- **Key Methods**: code2docs.generators.mkdocs_gen.MkDocsGenerator.__init__, code2docs.generators.mkdocs_gen.MkDocsGenerator.generate, code2docs.generators.mkdocs_gen.MkDocsGenerator._build_nav, code2docs.generators.mkdocs_gen.MkDocsGenerator.write

### code2docs.analyzers.project_scanner.ProjectScanner
> Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.
- **Methods**: 3
- **Key Methods**: code2docs.analyzers.project_scanner.ProjectScanner.__init__, code2docs.analyzers.project_scanner.ProjectScanner._build_llm_config, code2docs.analyzers.project_scanner.ProjectScanner.analyze

### code2docs.analyzers.endpoint_detector.EndpointDetector
> Detects web endpoints from decorator patterns in source code.
- **Methods**: 3
- **Key Methods**: code2docs.analyzers.endpoint_detector.EndpointDetector.detect, code2docs.analyzers.endpoint_detector.EndpointDetector._parse_decorator, code2docs.analyzers.endpoint_detector.EndpointDetector._scan_django_urls

### code2docs.sync.updater.Updater
> Apply selective documentation updates based on detected changes.
- **Methods**: 2
- **Key Methods**: code2docs.sync.updater.Updater.__init__, code2docs.sync.updater.Updater.apply

### code2docs.config.Code2DocsConfig
> Main configuration for code2docs.
- **Methods**: 2
- **Key Methods**: code2docs.config.Code2DocsConfig.from_yaml, code2docs.config.Code2DocsConfig.to_yaml

### code2docs.sync.differ.ChangeInfo
> Describes a detected change.
- **Methods**: 1
- **Key Methods**: code2docs.sync.differ.ChangeInfo.__str__

### code2docs.generators.api_changelog_gen.ApiChange
> A single API change between two analysis snapshots.
- **Methods**: 1
- **Key Methods**: code2docs.generators.api_changelog_gen.ApiChange.emoji

## Data Transformation Functions

Key functions that process and transform data:

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._format_signature
> Format a function signature string.
- **Output to**: None.join

### code2docs.cli.DefaultGroup.parse_args
- **Output to**: None.parse_args, super

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject
> Parse pyproject.toml for dependencies.
- **Output to**: ProjectDependencies, data.get, project.get, project.get, None.items

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex
> Fallback regex-based pyproject.toml parser.
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.findall

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py
> Parse setup.py for dependencies (regex-based, no exec).
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.findall

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt
> Parse requirements.txt.
- **Output to**: ProjectDependencies, None.splitlines, line.strip, deps.dependencies.append, path.read_text

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string
> Parse a dependency string like 'package>=1.0'.
- **Output to**: re.match, DependencyInfo, dep_str.strip, DependencyInfo, dep_str.strip

### code2docs.analyzers.docstring_extractor.DocstringExtractor.parse
> Parse a docstring into structured sections (orchestrator).
- **Output to**: None.splitlines, DocstringInfo, self._extract_summary, self._parse_sections, DocstringInfo

### code2docs.analyzers.docstring_extractor.DocstringExtractor._parse_sections
> Walk remaining lines, dispatching content to the right section.
- **Output to**: None.strip, line.strip, self._classify_section, desc_lines.append, None.join

### code2docs.analyzers.endpoint_detector.EndpointDetector._parse_decorator
> Try to parse a route decorator string.
- **Output to**: self.FASTAPI_PATTERNS.search, self.FLASK_PATTERNS.search, Endpoint, Endpoint, None.upper

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

- `code2docs.config.Code2DocsConfig.from_yaml` - 34 calls
- `code2docs.generators.architecture_gen.ArchitectureGenerator.generate` - 32 calls
- `code2docs.sync.watcher.start_watcher` - 29 calls
- `code2docs.sync.updater.Updater.apply` - 28 calls
- `code2docs.sync.differ.Differ.detect_changes` - 16 calls
- `code2docs.generators.generate_docs` - 15 calls
- `code2docs.cli.generate` - 13 calls
- `code2docs.formatters.toc.extract_headings` - 10 calls
- `code2docs.cli.init` - 10 calls
- `code2docs.generators.readme_gen.ReadmeGenerator.write` - 9 calls
- `code2docs.formatters.markdown.MarkdownFormatter.table` - 8 calls
- `code2docs.generators.depgraph_gen.DepGraphGenerator.generate` - 8 calls
- `code2docs.cli.sync` - 8 calls
- `code2docs.analyzers.dependency_scanner.DependencyScanner.scan` - 8 calls
- `code2docs.cli.watch` - 7 calls
- `code2docs.generators.readme_gen.generate_readme` - 6 calls
- `code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate_all` - 6 calls
- `code2docs.generators.api_changelog_gen.ApiChangelogGenerator.generate` - 6 calls
- `code2docs.analyzers.docstring_extractor.DocstringExtractor.parse` - 6 calls
- `code2docs.analyzers.docstring_extractor.DocstringExtractor.coverage_report` - 6 calls
- `code2docs.generators.readme_gen.ReadmeGenerator.generate` - 5 calls
- `code2docs.generators.coverage_gen.CoverageGenerator.generate` - 5 calls
- `code2docs.sync.differ.Differ.save_state` - 5 calls
- `code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate_all` - 5 calls
- `code2docs.generators.api_changelog_gen.ApiChangelogGenerator.save_snapshot` - 5 calls
- `code2docs.analyzers.endpoint_detector.EndpointDetector.detect` - 5 calls
- `code2docs.formatters.toc.generate_toc` - 4 calls
- `code2docs.generators.changelog_gen.ChangelogGenerator.generate` - 4 calls
- `code2docs.generators.api_reference_gen.ApiReferenceGenerator.write_all` - 4 calls
- `code2docs.generators.module_docs_gen.ModuleDocsGenerator.write_all` - 4 calls
- `code2docs.generators.examples_gen.ExamplesGenerator.generate_all` - 4 calls
- `code2docs.generators.examples_gen.ExamplesGenerator.write_all` - 4 calls
- `code2docs.analyzers.docstring_extractor.DocstringExtractor.extract_all` - 4 calls
- `code2docs.formatters.markdown.MarkdownFormatter.code_block` - 3 calls
- `code2docs.formatters.badges.generate_badges` - 3 calls
- `code2docs.generators.mkdocs_gen.MkDocsGenerator.generate` - 2 calls
- `code2docs.generators.mkdocs_gen.MkDocsGenerator.write` - 2 calls
- `code2docs.cli.DefaultGroup.parse_args` - 2 calls
- `code2docs.config.Code2DocsConfig.to_yaml` - 2 calls
- `code2docs.analyzers.project_scanner.analyze_and_document` - 2 calls

## System Interactions

How components interact:

```mermaid
graph TD
    from_yaml --> Path
    from_yaml --> cls
    from_yaml --> get
    generate --> append
    generate --> _detect_layers
    apply --> resolve
    apply --> ProjectScanner
    apply --> analyze
    apply --> ReadmeGenerator
    apply --> generate
    _diff_classes --> set
    _diff_classes --> get
    _diff_classes --> keys
    _render_classes_sect --> _get_module_classes
    _render_classes_sect --> items
    _render_classes_sect --> join
    _render_classes_sect --> append
    _render_classes_sect --> _get_class_methods
    _render_api_classes --> sorted
    _render_api_classes --> join
    _render_api_classes --> items
    _render_api_classes --> append
    _render_api_classes --> _get_class_methods
    _generate_metrics_ta --> get
    _generate_metrics_ta --> append
    _generate_metrics_ta --> join
    _generate_metrics_ta --> round
    detect_changes --> resolve
    detect_changes --> _load_state
    detect_changes --> _compute_state
```

## Reverse Engineering Guidelines

1. **Entry Points**: Start analysis from the entry points listed above
2. **Core Logic**: Focus on classes with many methods
3. **Data Flow**: Follow data transformation functions
4. **Process Flows**: Use the flow diagrams for execution paths
5. **API Surface**: Public API functions reveal the interface

## Context for LLM

Maintain the identified architectural patterns and public API surface when suggesting changes.