import json
from pathlib import Path


def test_class_metadata():
    classes = json.loads(Path("models/classes.json").read_text())
    assert len(classes) == 10
    assert "cat" in classes
    assert "truck" in classes
