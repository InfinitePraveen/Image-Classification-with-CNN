from pathlib import Path


def test_no_src_directory():
    assert not Path("src").exists()


def test_required_docs():
    assert Path("README.md").exists()
    assert Path("CONTRIBUTING.md").exists()
    assert Path("CHANGELOG.md").exists()
