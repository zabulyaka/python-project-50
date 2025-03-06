import argparse
from json import load as j_load

from yaml import load as yam_load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def get_args(default_format='json') -> tuple:    
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files\
                            and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    arg1: str = args.first_file
    arg2: str = args.second_file
    f: str = args.format if args.format else default_format
    return (arg1, arg2, f)


def get_data(filepath: str) -> dict:
    data: dict = {}
    if filepath.endswith('.json'):
        data = j_load(open(filepath))
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        data = yam_load(open(filepath), Loader=Loader)
    return data
