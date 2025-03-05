import json
from pathlib import Path

import pytest

from gendiff.gendiff import generate_diff


def get_test_data_path(directory, filename) -> str:
    return Path(__file__).parent / directory / filename


def read_json(filename) -> dict:
    path: str = get_test_data_path('JSON', filename)
    return json.load(open(path))


@pytest.fixture
def json1():
    return read_json('file1.json')


@pytest.fixture
def json2():
    return read_json('file2.json')


def test_generate_diff(json1, json2):
    assert generate_diff(json1, json2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
