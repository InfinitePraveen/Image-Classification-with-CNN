import json
from pathlib import Path


def test_notebooks_are_valid_json():
    for path in Path("notebooks").glob("*.ipynb"):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["nbformat"] == 4
        assert data["cells"]
