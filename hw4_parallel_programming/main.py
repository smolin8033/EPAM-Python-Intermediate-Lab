# python main.py urllist.txt --dir=:C/et_cetera/ --threads=4 --size=1000x1000

import argparse
import concurrent.futures
import os
import requests
import sys
import time
import queue
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from pathlib import Path


parser = argparse.ArgumentParser(description='Give entry parameters')


parser.add_argument('file')
parser.add_argument('--dir', default='os.getcwd()')
parser.add_argument('--threads', type=int, default=1)
parser.add_argument('--size', type=str, default='100x100')


args = parser.parse_args()
image_size = tuple([int(i) for i in args.size.split('x')])
q = queue.Queue()


def list_of_urls(arr: list):
    """make list of tuples (positional index of url, url)"""
    urls_with_index = []
    for index, value in enumerate(arr):
        urls_with_index.append((index, value))
    return urls_with_index


try:
    """Check if input file with urls exists else raise FileNotFoundError"""
    with open(args.file) as f:
        print('Found file')
        urls = f.read().split('\n')[:-1]
        urls = list_of_urls(urls)
except FileNotFoundError:
    print('File with urls not found')
    sys.exit()


def save_to_dir(image, url):
    """
    Save an image to the directory, given as a parameter.
    If the directory doesn't exist, create it.
    """
    file_path = str(args.dir)
    Path(file_path).mkdir(parents=True, exist_ok=True)
    file_name = f'{url[0]}.jpeg'
    new_file_path = os.path.join(file_path, file_name)
    image.save(new_file_path, 'JPEG')
    q.put(f'success:{os.path.getsize(os.path.join(new_file_path))}')


def pillow_handle_and_save(content, size: tuple, url):
    """Open response.content, make thumbnail's preview, handle 2 exceptions"""
    try:
        with Image.open(BytesIO(content)) as im:
            im.thumbnail(size)
            im.show()
            save_to_dir(im, url)
    except UnidentifiedImageError:
        print(f'The image on the {url[1]} was not identified')
        q.put(f'error: The image on the {url[1]} was not identified')
    except IOError:
        print('Cannot create thumbnail for', url[1])
        q.put(f'error: Cannot create thumbnail for {url[1]}')


def parse_image(url: tuple):
    """Check every url's validity"""
    response = requests.get(url[1])
    if response.status_code == 200:
        pillow_handle_and_save(response.content, image_size, url)
    else:
        print(url[1], '-', response)
        q.put(f'error: {url[1]} - {response}')


def do_parse_image(urls_for_parsing: list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(parse_image, urls_for_parsing)


if __name__ == '__main__':
    errors_counter = 0
    success_counter = 0
    bytes_downloaded = 0
    start_time = time.perf_counter()
    do_parse_image(urls_for_parsing=urls)
    for message in q.queue:
        if message.startswith('error'):
            errors_counter += 1
        else:
            success_counter += 1
            bytes_downloaded += int(message.split(':')[1])
    print(f'The number of errors: {errors_counter}')
    print(f'The number of downloaded and readable files: {success_counter}')
    print(f'The number of downloaded bytes: {bytes_downloaded}')
    duration = time.perf_counter() - start_time
    print(f'Finished in {duration} seconds')
