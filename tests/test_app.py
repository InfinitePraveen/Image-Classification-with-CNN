import io
import app


def test_home_page():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"CIFAR-10 Image Classifier" in response.data


def test_about_page():
    client = app.app.test_client()
    response = client.get("/about")
    assert response.status_code == 200


def test_health():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_predict_without_file():
    client = app.app.test_client()
    response = client.post("/predict")
    assert response.status_code == 400


def test_predict_without_model_returns_service_error(monkeypatch):
    monkeypatch.setattr(app.os.path, "exists", lambda _: False)
    client = app.app.test_client()
    response = client.post(
        "/predict",
        data={"image": (io.BytesIO(b"not-an-image"), "test.jpg")},
        content_type="multipart/form-data",
    )
    assert response.status_code in (400, 503)
