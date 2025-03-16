IGNORED_VALUES = ['null', 'true', 'false', '[complex value]']


def set_info_line(key: str, *args, mode='r') -> str:
    result = ''
    args = list(map(lambda val: f"'{val}'"
            if val not in IGNORED_VALUES and isinstance(val, str)
            else val, args))
    result += f"Property '{key}' was "
    match mode:
        case 'r':
            result += 'removed\n'
        case 'a':
            new_val: str = args[0]
            result += f'added with value: {new_val}\n'
        case 'u':
            [old_val, new_val] = args
            result += f'updated. From {old_val} to {new_val}\n'
    return result


def set_plain_view(diff: dict, path='') -> str:
    result = ''
    items: tuple = diff.items()
    for (key, value) in items:
        if isinstance(value, dict):
            status: str = value.get('_status')
            old_val: str = value.get('_old_value')
            if isinstance(old_val, dict):
                old_val = '[complex value]'
            new_val: str = value.get('_new_value')
            if isinstance(new_val, dict):
                new_val = '[complex value]'
            match status:
                case None:
                    result += set_plain_view(value,
                            path=path + f'{key}.') + '\n'
                case 'added':
                    result += set_info_line(path + key, new_val, mode='a')
                case 'removed':
                    result += set_info_line(path + key)
                case 'updated':
                    result += set_info_line(path + key,
                            old_val, new_val, mode='u')
    return result.rstrip()
