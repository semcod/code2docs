"""Tests for sync (differ)."""

import tempfile
from pathlib import Path


from code2docs.sync.differ import Differ, ChangeInfo


class TestDiffer:
    def test_detect_new_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a Python file
            (Path(tmpdir) / "hello.py").write_text("print('hello')")

            differ = Differ()
            changes = differ.detect_changes(tmpdir)

            assert len(changes) == 1
            assert changes[0].change_type == "added"
            assert changes[0].module == "hello"

    def test_detect_no_changes_after_save(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            (Path(tmpdir) / "hello.py").write_text("print('hello')")

            differ = Differ()
            differ.save_state(tmpdir)
            changes = differ.detect_changes(tmpdir)
            assert len(changes) == 0

    def test_detect_modified(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            f = Path(tmpdir) / "hello.py"
            f.write_text("print('v1')")

            differ = Differ()
            differ.save_state(tmpdir)

            f.write_text("print('v2')")
            changes = differ.detect_changes(tmpdir)

            assert len(changes) == 1
            assert changes[0].change_type == "modified"

    def test_detect_deleted(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            f = Path(tmpdir) / "hello.py"
            f.write_text("print('hello')")

            differ = Differ()
            differ.save_state(tmpdir)

            f.unlink()
            changes = differ.detect_changes(tmpdir)

            assert len(changes) == 1
            assert changes[0].change_type == "deleted"

    def test_ignore_patterns(self):
        from code2docs.config import Code2DocsConfig
        config = Code2DocsConfig()
        config.sync.ignore = ["tests/"]

        with tempfile.TemporaryDirectory() as tmpdir:
            tests_dir = Path(tmpdir) / "tests"
            tests_dir.mkdir()
            (tests_dir / "test_x.py").write_text("pass")
            (Path(tmpdir) / "main.py").write_text("pass")

            differ = Differ(config)
            changes = differ.detect_changes(tmpdir)

            # Only main.py should be detected
            assert len(changes) == 1
            assert "main" in changes[0].module

    def test_change_info_str(self):
        change = ChangeInfo(module="foo.bar", file="foo/bar.py", change_type="modified")
        assert "[modified]" in str(change)
        assert "foo.bar" in str(change)
