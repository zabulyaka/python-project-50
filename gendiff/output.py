import copy


def bool_to_str(data: dict) -> dict:
    result: dict = copy.deepcopy(data)
    for key in result.keys():
        if type(result[key]) is bool:
            if result[key]:
                result[key] = 'true'
            else:
                result[key] = 'false'
    return result


def set_diff_json(file1: dict, file2: dict) -> str:
    result = ''
    json1 = bool_to_str(file1)
    json2 = bool_to_str(file2)
    keys1: set = set(file1.keys())
    keys2: set = set(file2.keys())
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
    result += '}\n'
    return result
