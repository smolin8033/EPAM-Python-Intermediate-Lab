import argparse
import concurrent.futures
import os
import requests
import sys
import time
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from pathlib import Path


index_counter = -1
errors_counter = 0

parser = argparse.ArgumentParser(description='Give entry parameters')

# python main.py urllist.txt --dir=:C/et_cetera/ --threads=4 --size=1000x1000
parser.add_argument('file')
parser.add_argument('--dir', default='os.getcwd()')
parser.add_argument('--threads', type=int, default=1)
parser.add_argument('--size', type=str, default='100x100')


args = parser.parse_args()
image_size = tuple([int(i) for i in args.size.split('x')])


try:
    """Check if input file with urls exists else raise FileNotFoundError"""
    with open(args.file) as f:
        print('Found file')
        urls = open(args.file).readlines()
except FileNotFoundError:
    print('File with urls not found')
    sys.exit()


def save_to_dir(image, ind: int):
    """
    Save an image to the directory, given as a parameter.
    If the directory doesn't exist, create it.
    """
    file_path = str(args.dir)
    Path(file_path).mkdir(parents=True, exist_ok=True)
    file_name = f'{ind}.jpeg'
    new_file_path = os.path.join(file_path, file_name)
    image.save(new_file_path, 'JPEG')


def pillow_handle_and_save(content, size: tuple, index: int):
    """Open response.content, make thumbnail's preview, handle 2 exceptions"""
    global errors_counter
    try:
        with Image.open(BytesIO(content)) as im:
            im.thumbnail(size)
            im.show()
            save_to_dir(im, index)
    except UnidentifiedImageError:
        print(f'The image on the url №{index} was not identified')
        errors_counter += 1
    except IOError:
        print('Cannot create thumbnail for', str(args.dir))
        errors_counter += 1


def parse_image(url: str):
    """Check every url's validity"""
    global errors_counter
    global index_counter
    response = requests.get(url)
    index_counter += 1
    if response.status_code == 200:
        pillow_handle_and_save(response.content, image_size, index_counter)
    else:
        print(index_counter, '-', response)
        errors_counter += 1


def do_parse_image(urls_for_parsing: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(parse_image, urls_for_parsing)


if __name__ == '__main__':
    start_time = time.perf_counter()
    do_parse_image(urls_for_parsing=urls)
    print(f'The number of errors: {errors_counter}')
    print(f'The number of downloaded files:'
          f' {len([f for f in os.listdir(args.dir)])}')
    print(f'The size of the folder with downloaded files:'
          f' {sum([os.path.getsize(os.path.join(str(args.dir), f)) for f in os.listdir(args.dir)])}')
    duration = time.perf_counter() - start_time
    print(f'Finished in {duration} seconds')
