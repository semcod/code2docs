# code2docs — Dependency Graph

> 38 modules, 68 dependency edges

## Module Dependencies

```mermaid
graph LR
    __main__ --> cli
    project_scanner --> config
    base --> config
    cli --> analyzers
    cli --> docstring_extractor
    cli --> project_scanner
    cli --> base
    cli --> config
    cli --> generators
    cli --> _registry_adapters
    cli --> registry
    cli --> sync
    cli --> differ
    cli --> updater
    cli --> watcher
    code2docs --> analyzers
    code2docs --> project_scanner
    code2docs --> config
    code2docs --> generators
    code2docs --> readme_gen
    advanced_usage --> code2docs
    quickstart --> code2docs
    generators --> analyzers
    generators --> project_scanner
    generators --> config
    _registry_adapters --> base
    _registry_adapters --> config
    _source_links --> config
    api_changelog_gen --> config
    api_reference_gen --> config
    architecture_gen --> config
    architecture_gen --> llm_helper
    changelog_gen --> config
    config_docs_gen --> config
    contributing_gen --> analyzers
    contributing_gen --> dependency_scanner
    contributing_gen --> config
    coverage_gen --> analyzers
    coverage_gen --> docstring_extractor
    coverage_gen --> config
    depgraph_gen --> config
    examples_gen --> config
    getting_started_gen --> analyzers
    getting_started_gen --> dependency_scanner
    getting_started_gen --> config
    getting_started_gen --> llm_helper
    mkdocs_gen --> config
    module_docs_gen --> config
    readme_gen --> analyzers
    readme_gen --> dependency_scanner
    readme_gen --> endpoint_detector
    readme_gen --> project_scanner
    readme_gen --> config
    readme_gen --> formatters
    readme_gen --> badges
    readme_gen --> toc
    readme_gen --> llm_helper
    llm_helper --> config
    registry --> base
    differ --> config
    updater --> analyzers
    updater --> project_scanner
    updater --> config
    updater --> generators
    updater --> api_reference_gen
    updater --> module_docs_gen
    updater --> readme_gen
    watcher --> config
```

## Coupling Matrix

| | __main__ | analyzers | dependency_scanner | docstring_extractor | endpoint_detector | project_scanner | base | cli | code2docs | config | advanced_usage | quickstart | formatters | badges | markdown | toc | generators | _registry_adapters | _source_links | api_changelog_gen | api_reference_gen | architecture_gen | changelog_gen | config_docs_gen | contributing_gen | coverage_gen | depgraph_gen | examples_gen | getting_started_gen | mkdocs_gen | module_docs_gen | readme_gen | llm_helper | registry | sync | differ | updater | watcher |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **__main__** | · |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **analyzers** |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **dependency_scanner** |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **docstring_extractor** |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **endpoint_detector** |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **project_scanner** |  |  |  |  |  | · |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **base** |  |  |  |  |  |  | · |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **cli** |  | → |  | → |  | → | → | · |  | → |  |  |  |  |  |  | → | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | → | → | → | → | → |
| **code2docs** |  | → |  |  |  | → |  |  | · | → |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |
| **config** |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **advanced_usage** |  |  |  |  |  |  |  |  | → |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **quickstart** |  |  |  |  |  |  |  |  | → |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **formatters** |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **badges** |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **markdown** |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **toc** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **generators** |  | → |  |  |  | → |  |  |  | → |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **_registry_adapters** |  |  |  |  |  |  | → |  |  | → |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **_source_links** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **api_changelog_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **api_reference_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **architecture_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |
| **changelog_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **config_docs_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **contributing_gen** |  | → | → |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **coverage_gen** |  | → |  | → |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |  |
| **depgraph_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |  |
| **examples_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |  |  |
| **getting_started_gen** |  | → | → |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  | → |  |  |  |  |  |
| **mkdocs_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |  |
| **module_docs_gen** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |  |  |
| **readme_gen** |  | → | → |  | → | → |  |  |  | → |  |  | → | → |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · | → |  |  |  |  |  |
| **llm_helper** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |  |
| **registry** |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |  |
| **sync** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |  |
| **differ** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |  |  |
| **updater** |  | → |  |  |  | → |  |  |  | → |  |  |  |  |  |  | → |  |  |  | → |  |  |  |  |  |  |  |  |  | → | → |  |  |  |  | · |  |
| **watcher** |  |  |  |  |  |  |  |  |  | → |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | · |

## Fan-in / Fan-out

| Module | Fan-in | Fan-out |
|--------|--------|---------|
| `__main__` | 0 | 1 |
| `analyzers` | 8 | 0 |
| `analyzers.dependency_scanner` | 3 | 0 |
| `analyzers.docstring_extractor` | 2 | 0 |
| `analyzers.endpoint_detector` | 1 | 0 |
| `analyzers.project_scanner` | 5 | 1 |
| `base` | 3 | 1 |
| `cli` | 1 | 12 |
| `code2docs` | 2 | 5 |
| `config` | 24 | 0 |
| `examples.advanced_usage` | 0 | 1 |
| `examples.quickstart` | 0 | 1 |
| `formatters` | 1 | 0 |
| `formatters.badges` | 1 | 0 |
| `formatters.markdown` | 0 | 0 |
| `formatters.toc` | 1 | 0 |
| `generators` | 3 | 3 |
| `generators._registry_adapters` | 1 | 2 |
| `generators._source_links` | 0 | 1 |
| `generators.api_changelog_gen` | 0 | 1 |
| `generators.api_reference_gen` | 1 | 1 |
| `generators.architecture_gen` | 0 | 2 |
| `generators.changelog_gen` | 0 | 1 |
| `generators.config_docs_gen` | 0 | 1 |
| `generators.contributing_gen` | 0 | 3 |
| `generators.coverage_gen` | 0 | 3 |
| `generators.depgraph_gen` | 0 | 1 |
| `generators.examples_gen` | 0 | 1 |
| `generators.getting_started_gen` | 0 | 4 |
| `generators.mkdocs_gen` | 0 | 1 |
| `generators.module_docs_gen` | 1 | 1 |
| `generators.readme_gen` | 2 | 9 |
| `llm_helper` | 3 | 1 |
| `registry` | 1 | 1 |
| `sync` | 1 | 0 |
| `sync.differ` | 1 | 1 |
| `sync.updater` | 1 | 7 |
| `sync.watcher` | 1 | 1 |
