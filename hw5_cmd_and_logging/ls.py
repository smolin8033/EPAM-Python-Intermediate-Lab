import argparse
import datetime
import os
import stat
from pwd import getpwuid
from grp import getgrgid


parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, nargs='?', default='.')
parser.add_argument('-a', action='store_true', help='List all files, including all "." files')
parser.add_argument('-l', action='store_true', help='Make the listing detailed')

args = parser.parse_args()


def sort_and_output(files):
    files.sort()
    for file in files:
        print(file)


def ls_a():
    files = [file for file in os.listdir(args.dir)]
    files += [os.curdir, os.pardir]
    sort_and_output(files)


def ls_l():
    for file in os.listdir(args.dir):
        make_long_list(args.dir, file)


def make_long_list(path, file):
    stats = os.stat(os.path.join(path, file))
    l_fields = [
            make_readable_perms(stats.st_mode),
            str(stats.st_nlink),
            getpwuid(stats.st_uid).pw_name,
            getgrgid(stats.st_gid).gr_name,
            str(stats.st_size),
            format_time(stats.st_mtime),
            file,
        ]
    print(l_fields)


def make_readable_perms(perm_stats):
    perm_chars = ['r', 'w', 'x']
    bin_perms = bin(perm_stats)[-9:]
    perms = file_or_dir(perm_stats)
    for i, perm, in enumerate(bin_perms):
        if perm == '0':
            perms += '-'
        else:
            perms += perm_chars[i % 3]
    return perms


def format_time(mod_time):
    datetime_time = datetime.datetime.fromtimestamp(mod_time)
    return datetime_time.strftime('%b %d %H:%M')


def file_or_dir(stats_mode):
    if stat.S_ISDIR(stats_mode):
        return 'd'
    else:
        return '-'


def ls():
    if args.a:
        ls_a()
    elif args.l:
        ls_l()
    else:
        files = [file for file in os.listdir(args.dir) if file[0] != '.']
        sort_and_output(files)


if __name__ == '__main__':
    try:
        ls()
    except OSError as err:
        print(err)
