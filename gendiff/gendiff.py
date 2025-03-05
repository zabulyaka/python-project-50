import argparse
import copy
import json


def bool_to_str(data: dict) -> dict:
    result: dict = copy.deepcopy(data)
    for key in result.keys():
        if type(result[key]) is bool:
            if result[key]:
                result[key] = 'true'
            else:
                result[key] = 'false'
    return result


def generate_diff(json1: dict, json2: dict) -> str:
    result: str = ''
    json1 = bool_to_str(json1)
    json2 = bool_to_str(json2)
    keys1: set = set(json1.keys())
    keys2: set = set(json2.keys())
    result += '{\n'
    for key in sorted(keys1 | keys2):
        if key in keys1 - keys2:
            result += f'  - {key}: {json1[key]}\n'
        elif key in keys2 - keys1:
            result += f'  + {key}: {json2[key]}\n' 
        else:
            if json1[key] == json2[key]:
                result += f'    {key}: {json1[key]}\n'
            else:
                result += f'  - {key}: {json1[key]}\n'
                result += f'  + {key}: {json2[key]}\n'
    result += '}'
    return result


def run() -> None:
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files\
                            and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    diff = generate_diff(file1, file2)
    print(diff)
