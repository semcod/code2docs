from tests.generators.conftest import _make_result, _make_config
from code2docs.generators.readme_gen import ReadmeGenerator, MARKER_START, MARKER_END

class TestReadmeGenerator:
    def test_manual_fallback_contains_sections(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        context = gen._build_context('mockproject')
        content = gen._build_manual('mockproject', config.readme.sections, context)
        assert '# mockproject' in content
        assert '## API Overview' in content
        assert '## Quick Start' in content

    def test_manual_fallback_sync_markers(self) -> None:
        config = _make_config()
        config.readme.sync_markers = True
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        context = gen._build_context('mockproject')
        context['sync_markers'] = True
        content = gen._build_manual('mockproject', config.readme.sections, context)
        assert MARKER_START in content
        assert MARKER_END in content

    def test_generate_produces_output(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        content = gen.generate()
        assert len(content) > 100
        assert 'mockproject' in content

    def test_build_api_section_lists_classes(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        context = gen._build_context('mockproject')
        section = gen._build_api_section('mockproject', context)
        assert 'Engine' in section

    def test_build_endpoints_section_empty(self) -> None:
        section = ReadmeGenerator._build_endpoints_section('x', {'endpoints': []})
        assert section == ''