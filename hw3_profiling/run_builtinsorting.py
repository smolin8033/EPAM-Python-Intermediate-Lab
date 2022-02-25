
from memory_profiler import profile

my_arr = [5, 9, 3, 6, 0, 1, 7, 2, 8, 4]

array = []


def builtin_sorting(arr):
    arr.sort()
    return arr


@profile
def run_builtin_sorting():
    for i in range(-350, 0):
        result = builtin_sorting(array)
    return result


if __name__ == '__main__':
    run_builtin_sorting()
