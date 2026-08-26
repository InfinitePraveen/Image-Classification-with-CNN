install:
	pip install -r requirements.txt

dev:
	pip install -r requirements-dev.txt

run:
	python app.py

test:
	pytest -q

lint:
	ruff check app.py tests
