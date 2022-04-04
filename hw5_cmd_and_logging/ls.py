import argparse
import datetime
import os
import stat
from grp import getgrgid
from pwd import getpwuid

DESCRIPTION = '''This is a prototype of "ls" Linux command.'''
EPILOG = '(c) Alexander Smolin 2022'


parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
parser.add_argument('dir', type=str, nargs='?', default='.')
parser.add_argument('-a', action='store_true', help='List all files, including all "." files')
parser.add_argument('-l', action='store_true', help='Make the listing detailed')

args = parser.parse_args()


def ls_l(files: list):
    """
    Makes an empty array and fills it with rows
    of the future output, appending the result of
    make_long_rows() function. Also, it passes rows to
    reformat_rows function.
    """
    long_list = []
    for file in files:
        long_list.append(make_long_rows(args.dir, file))
        reformat_rows(long_list)


def reformat_rows(rows: list):
    """
    Adjust each cell/element's width for a better look.
    Finally, show the printed output, as in case with
    'ls -l'.
    """
    column_widths = get_columns_width(rows)
    for row in rows:
        format_row = ' '.join(
                [field.rjust(column_widths[index]) for index, field in enumerate(row[:-1])]
                + [row[-1]]
        )
    print(format_row)


def get_columns_width(rows: list) -> list:
    """
    Get each column's (of the future output) width,
    the width of the widest element in a column.
    """
    column_widths = []
    for i in range(0, len(rows[0]) - 1):
        column = [row[i] for row in rows]
        column_widths.append(len(max(column, key=len)))
    return column_widths


def make_long_rows(path: str, file: str) -> list:
    """
    For each cell/element in a row takes the necessary
    data, i.e., human-readable permissions, username, etc.
    """
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
    return l_fields


def make_readable_perms(perm_stats: int) -> str:
    """
    Reformat permissions from stats.st_mode to Linux valid,
    i.e. 'drwxr-xr-x'.
    """
    perm_chars = ['r', 'w', 'x']
    bin_perms = bin(perm_stats)[-9:]
    perms = file_or_dir(perm_stats)
    for i, perm, in enumerate(bin_perms):
        if perm == '0':
            perms += '-'
        else:
            perms += perm_chars[i % 3]
    return perms


def format_time(mod_time: float) -> str:
    """
    Reformats 'float' human-unreadable type to class 'datetime.datetime',
    then to string and readable format.
    """
    datetime_time = datetime.datetime.fromtimestamp(mod_time)
    if datetime_time < datetime.datetime.now() - datetime.timedelta(days=365):
        return datetime_time.strftime('%b %d  %Y')
    return datetime_time.strftime('%b %d %H:%M')


def file_or_dir(stats_mode: int) -> str:
    if stat.S_ISDIR(stats_mode):
        return 'd'
    else:
        return '-'


def ls():
    """
    The function handles 'ls' and 'ls -a'-like requests.
    In case 'ls -l' or 'ls -la' is given, the function calls ls_l,
    passing filtered array as a parameter.
    """
    files = os.listdir(args.dir)
    if args.a:
        files += [os.curdir, os.pardir]
    else:
        files = [file for file in files if file[0] != '.']
    files.sort()
    if args.l:
        ls_l(files)
    else:
        for file in files:
            print(file)


if __name__ == '__main__':
    try:
        ls()
    except OSError as err:
        print(err)
