import argparse
import json


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
    print(file1)
    file2 = json.load(open(args.second_file))
    print(file2)
