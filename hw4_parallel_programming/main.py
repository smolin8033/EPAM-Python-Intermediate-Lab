import argparse
# import os


errors_counter = 0

parser = argparse.ArgumentParser(description='Give entry parameters')

# python download.py urllist.txt --dir=thumbnails/ --threads=4 --size=128x128
parser.add_argument('file')
parser.add_argument('--dir', default='os.getcwd()')
parser.add_argument('--threads', type=int, default=1)
parser.add_argument('--size', type=str, default='100x100')


args = parser.parse_args()


print('Argument values:')
print(args.file)
print(args.dir)
print(args.threads)
print(args.size)
