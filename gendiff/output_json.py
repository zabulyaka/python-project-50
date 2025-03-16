OFFSET_NORMAL = '    '
IGNORED_VALUES = ['null', 'true', 'false']


def json_formatted(data, depth=1) -> str:
    if isinstance(data, dict):
        result = ''
        offset: str = OFFSET_NORMAL * depth
        items: tuple = data.items()
        for (key, value) in items:
            result += offset
            if isinstance(value, dict):
                result += f'{json_formatted(key)}: {{\n{json_formatted(value,
                        depth=depth + 1)}{offset}}},\n' 
            else:
                result += f'{json_formatted(key)}: {json_formatted(value)},\n'
        return result[:len(result) - 2] + '\n'
    if data in IGNORED_VALUES or not isinstance(data, str):
        data = f'{data}'
    else:
        data = f'"{data}"'
    return data


def set_json_view(diff: dict) -> str:
    result = '{\n'
    result += json_formatted(diff)
#    return result + '}\n'
    return result + '}'

