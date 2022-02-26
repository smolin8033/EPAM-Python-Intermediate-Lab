import argparse
# import os
import requests
import sys
from io import BytesIO
from PIL import Image, UnidentifiedImageError


errors_counter = 0

parser = argparse.ArgumentParser(description='Give entry parameters')

# python download.py urllist.txt --dir=thumbnails/ --threads=4 --size=128x128
parser.add_argument('file')
parser.add_argument('--dir', default='os.getcwd()')
parser.add_argument('--threads', type=int, default=1)
parser.add_argument('--size', type=str, default='100x100')


args = parser.parse_args()
image_size = tuple([int(i) for i in args.size.split('x')])


try:
    with open(args.file) as f:
        print('Found file')
except FileNotFoundError:
    print('File with urls not found')
    sys.exit()


def pillow_handle(content, size, counter):
    try:
        with Image.open(BytesIO(content)) as im:
            im.thumbnail(size)
            im.show()
    except UnidentifiedImageError:
        counter += 1


def parse_image(url_file, counter):
    with open(url_file) as file:
        for url in file:
            response = requests.get(url)
            if response.status_code == 200:
                pillow_handle(response.content, image_size, errors_counter)
            else:
                print(response.status_code)
                counter += 1
    print(counter)


print(parse_image(args.file, errors_counter))
