from json import load as j_load
from pathlib import Path

from yaml import load as yam_load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import pytest

from gendiff.gendiff import generate_diff


def get_test_data_path(directory, filename) -> str:
    return Path(__file__).parent / directory / filename


def read_json(filename) -> dict:
    path: str = get_test_data_path('test_data', filename)
    return j_load(open(path))


def read_yaml(filename) -> dict:
    path: str = get_test_data_path('test_data', filename)
    return yam_load(open(path), Loader=Loader)


@pytest.fixture
def json1():
    return read_json('file1.json')


@pytest.fixture
def json2():
    return read_json('file2.json')


@pytest.fixture
def json_deep1():
    return read_json('file1_deep.json')


@pytest.fixture
def json_deep2():
    return read_json('file2_deep.json')


@pytest.fixture
def yaml1():
    return read_yaml('file1.yaml')


@pytest.fixture
def yaml2():
    return read_yaml('file2.yaml')


@pytest.fixture
def yaml_deep1():
    return read_yaml('file1_deep.yaml')


@pytest.fixture
def yaml_deep2():
    return read_yaml('file2_deep.yaml')


def test_generate_diff_json_shallow(json1, json2):
    result_path: str = get_test_data_path('test_data', 'result_json.txt')
    assert generate_diff(json1, json2) == open(result_path).read()


def test_generate_diff_json_deep(json_deep1, json_deep2):
    result_path: str = get_test_data_path('test_data', 'result_json_deep.txt')
    assert generate_diff(json_deep1, json_deep2) == open(result_path).read()


def test_generate_diff_yaml_shallow(yaml1, yaml2):
    result_path: str = get_test_data_path('test_data', 'result_yaml.txt')
    assert generate_diff(yaml1, yaml2) == open(result_path).read()


def test_generate_diff_yaml_deep(yaml_deep1, yaml_deep2):
    result_path: str = get_test_data_path('test_data', 'result_yaml_deep.txt')
    assert generate_diff(yaml_deep1, yaml_deep2) == open(result_path).read()


def test_generate_diff_json_plain(json_deep1, json_deep2):
    result_path: str = get_test_data_path('test_data', 'result_json_plain.txt')
    assert generate_diff(json_deep1,
            json_deep2, format_name='plain') == open(result_path).read()

    
def test_generate_diff_yaml_plain(yaml_deep1, yaml_deep2):
    result_path: str = get_test_data_path('test_data', 'result_yaml_plain.txt')
    assert generate_diff(yaml_deep1,
            yaml_deep2, format_name='plain') == open(result_path).read()
