import argparse
import os
import requests
import sys
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from pathlib import Path


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


def pillow_handle_and_save(content, size, url_index):
    global errors_counter
    file_path = str(args.dir)
    Path(file_path).mkdir(parents=True, exist_ok=True)
    try:
        with Image.open(BytesIO(content)) as im:
            im.thumbnail(size)
            im.show()
            file_name = f'{url_index}.jpeg'
            new_file_path = os.path.join(file_path, file_name)
            im.save(new_file_path, 'JPEG')
    except UnidentifiedImageError:
        print(f'The image on the url №{url_index} was not identified')
        errors_counter += 1
    except IOError:
        print('Cannot create thumbnail for', new_file_path)
        errors_counter += 1


def parse_image(url_file):
    global errors_counter
    with open(url_file) as file:
        file_list = file.readlines()
        for url in file_list:
            url_index = file_list.index(url)
            response = requests.get(url)
            if response.status_code == 200:
                pillow_handle_and_save(response.content, image_size, url_index)
            else:
                print(url_index, '-', response)
                errors_counter += 1


print(parse_image(args.file))
print(f'The number of errors: {errors_counter}')
