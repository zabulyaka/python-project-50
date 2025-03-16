OFFSET_NORMAL = '    '
OFFSET_ADD = '  + '
OFFSET_REMOVE = '  - '


def set_info_line(
        key: str,
        value: str,
        offset=OFFSET_NORMAL,
        is_nested=False) -> str:
    result = ''
    result += offset + key
    # if not value:
    #    return result + ':\n'
    if is_nested:
        result += f': {{\n{value}\n'
    else:
        result += f': {value}\n'
    return result


def set_stylish_view(diff: dict, depth=0) -> str:
    result = '' if depth > 0 else '{\n'
    offset: str = OFFSET_NORMAL * depth
    items: tuple = diff.items()
    for (key, value) in items:
        result += offset
        if isinstance(value, dict):
            status: str = value.get('_status')
            old_val: str = value.get('_old_value')
            if isinstance(old_val, dict):
                old_val = f'{{\n{set_stylish_view(old_val, depth=depth + 1)}'
            new_val: str = value.get('_new_value')
            if isinstance(new_val, dict):
                new_val = f'{{\n{set_stylish_view(new_val, depth=depth + 1)}'
            match status:
                case None:
                    nested: str = set_stylish_view(value, depth=depth + 1)
                    result += set_info_line(key, nested, is_nested=True)
                case 'remained':
                    result += set_info_line(key, old_val)
                case 'added':
                    result += set_info_line(key, new_val, offset=OFFSET_ADD)
                case 'removed':
                    result += set_info_line(key, old_val, offset=OFFSET_REMOVE)
                case 'updated':
                    result += set_info_line(key, old_val, offset=OFFSET_REMOVE)
                    result += offset
                    result += set_info_line(key, new_val, offset=OFFSET_ADD)
        else:
            result += set_info_line(key, value)
    result += offset + '}' if depth > 0 else offset + '}\n'
    return result

