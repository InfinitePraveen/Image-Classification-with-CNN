# Web Application

The Flask app provides:

- `GET /` — classifier UI
- `GET /about` — project information
- `GET /health` — service/model health
- `POST /predict` — image prediction endpoint

The frontend uses vanilla JavaScript and sends the selected image to `/predict`.
