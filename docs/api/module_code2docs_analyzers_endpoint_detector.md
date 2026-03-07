# `code2docs.analyzers.endpoint_detector`

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/endpoint_detector.py`

## Classes

### `Endpoint`

Represents a detected web endpoint.

### `EndpointDetector`

Detects web endpoints from decorator patterns in source code.

#### Methods

- `detect(self, result, project_path)` — Detect all endpoints from the analysis result.
- `_parse_decorator(self, decorator, func)` — Try to parse a route decorator string.
- `_scan_django_urls(self, project_path)` — Scan urls.py files for Django URL patterns.
