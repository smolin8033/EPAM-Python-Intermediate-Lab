import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, nargs='?', default='.')
parser.add_argument('-a', action='store_true')
parser.add_argument('-l', action='store_true')

args = parser.parse_args()


def ls():
    # if
    for file in os.listdir(args.dir):
        print(file)


if __name__ == '__main__':
    ls()
