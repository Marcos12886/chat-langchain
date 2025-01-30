.PHONY: start, format, lint

format:
	uv run ruff format .
	uvrun ruff --select I --fix .

lint:
	uvrun ruff .
	uv run ruff format . --diff
	uv run ruff --select I .

