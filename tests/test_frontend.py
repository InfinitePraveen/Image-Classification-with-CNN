from pathlib import Path


def test_frontend_assets_exist():
    assert Path("templates/index.html").exists()
    assert Path("static/css/style.css").exists()
    assert Path("static/js/app.js").exists()
