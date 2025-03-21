import copy

from gendiff.output.output_json import set_json_view
from gendiff.output.output_plain import set_plain_view
from gendiff.output.output_stylish import set_stylish_view
from gendiff.parse import get_args, get_data


def bool_null_to_str(data: dict) -> dict:
    result: dict = copy.deepcopy(data)
    for key in result.keys():
        if isinstance(result.get(key), dict):
            result[key] = bool_null_to_str(result[key])
        elif isinstance(result.get(key), bool):
            if result[key]:
                result[key] = 'true'
            else:
                result[key] = 'false'
        elif result[key] is None:
            result[key] = 'null'
    return result


def get_diff(file1: dict, file2: dict) -> dict:
    result: dict = {}
    keys1: set = set(file1.keys())
    keys2: set = set(file2.keys())
    for key in sorted(keys1 | keys2):
        if type(file1.get(key)) is type(file2.get(key)) is dict:
            result[key] = get_diff(file1[key], file2[key])
        elif key in keys1 - keys2:
            result[key] = {'_old_value': file1[key], '_status': 'removed'}
        elif key in keys2 - keys1:
            result[key] = {'_new_value': file2[key], '_status': 'added'}
        else:
            if file1.get(key) == file2.get(key):
                result[key] = {'_old_value': file1[key], '_status': 'remained'}
            else:
                result[key] = {'_old_value': file1[key],
                        '_new_value': file2[key], '_status': 'updated'}
    return result


def generate_diff(file1_path: str, file2_path: str,
        format_name='stylish') -> str:
    result: str = ''
    file1: dict = bool_null_to_str(get_data(file1_path))
    file2: dict = bool_null_to_str(get_data(file2_path))
    diff: dict = get_diff(file1, file2)
    if format_name == 'stylish':
        result = set_stylish_view(diff)
    elif format_name == 'plain':
        result = set_plain_view(diff)
    elif format_name == 'json':
        result = set_json_view(diff)
    return result


def run() -> None:
    args: tuple[str, str, str] = get_args()
    (arg1, arg2, f) = args
    diff: str = generate_diff(arg1, arg2, format_name=f)
    print(diff)

