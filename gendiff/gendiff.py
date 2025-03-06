from gendiff.output import set_diff_json
from gendiff.parse import get_args, get_data


def generate_diff(file1: dict, file2: dict, output_format='json') -> str:
    diff: str = ''
    if output_format == 'json':
        diff = set_diff_json(file1, file2)
    return diff


def run() -> None:
    args: tuple[str, str, str] = get_args()
    (arg1, arg2, f) = args
    file1: dict = get_data(arg1)
    file2: dict = get_data(arg2)
    diff: str = generate_diff(file1, file2, output_format=f)
    print(diff)
