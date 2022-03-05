import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, nargs='?', default='.')
parser.add_argument('-a', action='store_true', help='List all files, including all "." files')
parser.add_argument('-l', action='store_true')

args = parser.parse_args()


def sort_and_output(files):
    files.sort()
    for file in files:
        print(file)


def ls_a():
    files = [file for file in os.listdir(args.dir)]
    files += [os.curdir, os.pardir]
    sort_and_output(files)


def ls():
    if args.a:
        ls_a()
    files = [file for file in os.listdir(args.dir) if file[0] != '.']
    sort_and_output(files)


if __name__ == '__main__':
    ls()
