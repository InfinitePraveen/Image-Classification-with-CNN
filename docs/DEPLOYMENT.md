# Deployment

The included `Procfile` supports WSGI platforms that provide a `$PORT` environment variable.

Before deployment:

1. Install requirements.
2. Produce `models/cifar10_cnn.keras`.
3. Configure an appropriate upload limit.
4. Run a production WSGI server such as Gunicorn.
5. Do not enable Flask debug mode in production.
