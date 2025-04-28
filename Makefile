.PHONY: install dev test lint clean

# Install dependencies
install:
	uv pip install -e ".[dev]"
	pre-commit install

# Install development dependencies
dev:
	uv pip install -e ".[dev]"

# Run tests
test:
	pytest tests/

# Run linting
lint:
	ruff check .
	black --check .
	isort --check-only .
	mypy .

# Format code
format:
	ruff check --fix .
	black .
	isort .

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete 