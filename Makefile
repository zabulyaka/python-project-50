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

try:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json

try2:
	uv run gendiff tests/test_data/file1.yaml tests/test_data/file2.json

try3:
	uv run gendiff tests/test_data/file1_deep.json tests/test_data/file2_deep.json

try4:
	uv run gendiff --format plain tests/test_data/file1_deep.json tests/test_data/file2_deep.json

try5:
	uv run gendiff --format json tests/test_data/file1_deep.json tests/test_data/file2_deep.json

test:
	uv run pytest

test-cov:
	uv run pytest --cov=gendiff

test-coverage:
	uv run pytest --cov --cov-report xml
