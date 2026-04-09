from tests.generators.conftest import _make_result, _make_config
from code2docs.generators.api_reference_gen import ApiReferenceGenerator

class TestApiReferenceGenerator:
    def test_generate_produces_single_file(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen.generate()
        assert 'API Reference' in content
        assert isinstance(content, str)

    def test_contains_modules(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen.generate()
        assert 'mylib.core' in content
        assert 'mylib.utils' in content

    def test_contains_classes(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen.generate()
        assert 'Engine' in content

    def test_contains_functions(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen.generate()
        assert 'process' in content
        assert 'validate' in content

    def test_skips_trivial_modules(self) -> None:
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        assert not gen._has_content('nonexistent.module')