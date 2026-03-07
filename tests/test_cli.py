"""CLI smoke tests using Click's CliRunner."""

import tempfile
from pathlib import Path

from click.testing import CliRunner

from code2docs.cli import main


class TestCLI:
    def setup_method(self):
        self.runner = CliRunner()

    def test_help(self):
        result = self.runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "code2docs" in result.output
        assert "generate" in result.output
        assert "sync" in result.output
        assert "init" in result.output

    def test_generate_help(self):
        result = self.runner.invoke(main, ["generate", "--help"])
        assert result.exit_code == 0
        assert "--readme-only" in result.output
        assert "--dry-run" in result.output
        assert "--verbose" in result.output

    def test_sync_help(self):
        result = self.runner.invoke(main, ["sync", "--help"])
        assert result.exit_code == 0
        assert "Synchronize" in result.output

    def test_init_creates_config(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = self.runner.invoke(main, ["init", tmpdir])
            assert result.exit_code == 0
            assert (Path(tmpdir) / "code2docs.yaml").exists()

    def test_generate_dry_run(self):
        result = self.runner.invoke(main, [".", "--dry-run"])
        assert result.exit_code == 0
        assert "code2docs" in result.output
        assert "README.md" in result.output
        assert "dry-run" in result.output
        assert "Done!" in result.output

    def test_readme_only_dry_run(self):
        result = self.runner.invoke(main, [".", "--readme-only", "--dry-run"])
        assert result.exit_code == 0
        assert "README.md" in result.output
        # Should NOT have docs/api since --readme-only
        assert "docs/api" not in result.output

    def test_default_group_routes_path(self):
        """Ensure bare path argument is routed to generate."""
        result = self.runner.invoke(main, [".", "--dry-run"])
        assert result.exit_code == 0
        assert "Done!" in result.output

    def test_verbose(self):
        result = self.runner.invoke(main, [".", "--verbose", "--dry-run"])
        assert result.exit_code == 0
        assert "Functions:" in result.output
        assert "Classes:" in result.output
        assert "Modules:" in result.output
