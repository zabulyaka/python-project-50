install:
	uv sync

help:
	uv run gendiff -h

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-upgrade:
	uv tool upgrade hexlet-code

package-uninstall:
	uv tool uninstall hexlet-code

update:
	uv tool update-shell

lint:
	uv run ruff check

fix:
	uv run ruff check --fix

test:
	uv run gendiff tests/JSON/file1.json tests/JSON/file2.json
