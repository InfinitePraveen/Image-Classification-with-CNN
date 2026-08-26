# Contributing Guide

Thank you for considering a contribution to **Image Classification with CNN**.

## Getting Started

1. Fork the repository.
2. Create a feature branch.
3. Create a Python virtual environment.
4. Install dependencies from `requirements.txt` and `requirements-dev.txt`.
5. Make your changes.
6. Run the tests and validate the notebooks affected by your change.
7. Open a pull request.

## Branch Naming

Use descriptive names:

- `feature/model-improvement`
- `fix/upload-validation`
- `docs/readme-update`
- `test/inference-tests`

## Notebook Guidelines

- Keep notebooks focused on one stage of the workflow.
- Do not place secrets or API keys in notebooks.
- Use deterministic random seeds where practical.
- Explain important preprocessing and modeling decisions.
- Avoid committing large generated datasets.
- Clear unnecessary output cells before committing when outputs are not useful.

## Code Guidelines

- Follow PEP 8 where practical.
- Use descriptive variable names.
- Add comments for non-obvious decisions.
- Keep Flask routes small and readable.
- Do not introduce a `src/` package for preprocessing or data loaders; this project intentionally keeps the educational workflow in notebooks.

## Testing

Run:

```bash
pytest -q
```

For the web application, also verify:

```bash
python app.py
```

and test a valid CIFAR-10 image plus an invalid upload.

## Pull Requests

A pull request should include:

- A clear title.
- A concise description of the change.
- Testing performed.
- Screenshots for significant frontend changes.
- Notes about changed model architecture or training behavior.

## Commit Messages

Prefer conventional, concise messages such as:

```text
feat: add CNN training notebook
fix: validate uploaded image extensions
docs: update dataset instructions
test: add prediction endpoint coverage
```

## Dataset and Model Files

Do not commit the full Kaggle dataset or large generated training artifacts unless specifically required. Store large files outside Git and document how to reproduce them.

## Code of Conduct

Please be respectful, constructive and welcoming to other contributors.
