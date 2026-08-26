import os
from io import BytesIO

import numpy as np
from flask import Flask, jsonify, render_template, request
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_UPLOAD_MB", "5")) * 1024 * 1024

MODEL_PATH = os.path.join("models", "cifar10_cnn.keras")
CLASS_NAMES = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck",
]

_model = None


def load_model():
    """Load the Keras model lazily so the app can start without a model file."""
    global _model
    if _model is None and os.path.exists(MODEL_PATH):
        import tensorflow as tf
        _model = tf.keras.models.load_model(MODEL_PATH)
    return _model


def predict_image(image_bytes):
    """Return the predicted CIFAR-10 class and confidence."""
    image = Image.open(BytesIO(image_bytes)).convert("RGB").resize((32, 32))
    array = np.asarray(image, dtype=np.float32) / 255.0
    model = load_model()

    if model is None:
        raise FileNotFoundError(
            "Model not found. Run notebook 06_inference_and_export.ipynb first."
        )

    probabilities = model.predict(np.expand_dims(array, axis=0), verbose=0)[0]
    index = int(np.argmax(probabilities))
    return CLASS_NAMES[index], float(probabilities[index]), probabilities


@app.get("/")
def index():
    return render_template("index.html", model_ready=os.path.exists(MODEL_PATH))


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/health")
def health():
    return jsonify({"status": "ok", "model_ready": os.path.exists(MODEL_PATH)})


@app.post("/predict")
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image file was uploaded."}), 400

    uploaded = request.files["image"]
    if not uploaded.filename:
        return jsonify({"error": "Please choose an image."}), 400

    try:
        image_bytes = uploaded.read()
        label, confidence, probabilities = predict_image(image_bytes)
        ranking = sorted(
            zip(CLASS_NAMES, probabilities),
            key=lambda item: item[1],
            reverse=True,
        )[:3]
        return jsonify({
            "label": label,
            "confidence": round(confidence * 100, 2),
            "top_predictions": [
                {"label": name, "confidence": round(float(score) * 100, 2)}
                for name, score in ranking
            ],
        })
    except (UnidentifiedImageError, OSError):
        return jsonify({"error": "The uploaded file is not a valid image."}), 400
    except FileNotFoundError as exc:
        return jsonify({"error": str(exc)}), 503
    except Exception as exc:
        app.logger.exception("Prediction failed")
        return jsonify({"error": f"Prediction failed: {exc}"}), 500


@app.errorhandler(413)
def request_too_large(_):
    return jsonify({"error": "Image is too large. Maximum size is 5 MB."}), 413


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
