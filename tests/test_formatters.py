"""Tests for formatters (markdown, badges, toc)."""


from code2docs.formatters.markdown import MarkdownFormatter
from code2docs.formatters.badges import generate_badges
from code2docs.formatters.toc import generate_toc, extract_headings


class TestMarkdownFormatter:
    def test_heading(self):
        md = MarkdownFormatter()
        md.heading("Title", level=1)
        assert "# Title" in md.render()

    def test_heading_level2(self):
        md = MarkdownFormatter()
        md.heading("Section", level=2)
        assert "## Section" in md.render()

    def test_code_block(self):
        md = MarkdownFormatter()
        md.code_block("print('hello')", "python")
        result = md.render()
        assert "```python" in result
        assert "print('hello')" in result

    def test_table(self):
        md = MarkdownFormatter()
        md.table(["Name", "Value"], [["a", "1"], ["b", "2"]])
        result = md.render()
        assert "| Name | Value |" in result
        assert "| a | 1 |" in result

    def test_list_item(self):
        md = MarkdownFormatter()
        md.list_item("Item one")
        md.list_item("Sub item", indent=1)
        result = md.render()
        assert "- Item one" in result
        assert "  - Sub item" in result

    def test_inline_helpers(self):
        md = MarkdownFormatter()
        assert md.inline_code("var") == "`var`"
        assert md.bold("text") == "**text**"
        assert md.link("click", "http://x") == "[click](http://x)"


class TestBadges:
    def test_generate_badges_version(self):
        result = generate_badges("myproject", ["version"], {})
        assert "version" in result
        assert "0.1.0" in result

    def test_generate_badges_python(self):
        result = generate_badges("myproject", ["python"], {})
        assert "python" in result

    def test_generate_badges_complexity(self):
        result = generate_badges("myproject", ["complexity"], {"functions_found": 42})
        assert "42" in result

    def test_generate_badges_empty(self):
        result = generate_badges("myproject", [], {})
        assert result == ""


class TestToc:
    def test_extract_headings(self):
        content = "# Title\n## Section 1\n### Sub\n## Section 2\n"
        headings = extract_headings(content, max_depth=3)
        assert len(headings) == 4
        assert headings[0] == (1, "Title", "title")
        assert headings[1] == (2, "Section 1", "section-1")

    def test_extract_headings_skips_code_blocks(self):
        content = "# Real\n```\n# Not a heading\n```\n## Also Real\n"
        headings = extract_headings(content, max_depth=3)
        assert len(headings) == 2

    def test_generate_toc(self):
        content = "# Title\n## Section A\n## Section B\n"
        toc = generate_toc(content)
        assert "Table of Contents" in toc
        assert "[Section A]" in toc
        assert "[Section B]" in toc

    def test_generate_toc_empty(self):
        toc = generate_toc("")
        assert toc == ""
