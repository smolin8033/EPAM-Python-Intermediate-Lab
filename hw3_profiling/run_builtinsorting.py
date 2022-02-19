
from memory_profiler import profile


array = []


def builtin_sorting(arr):
    arr.sort()
    return arr


@profile
def run_builtin_sorting():
    array = []
    for i in range(-350, 0):
        array.append(abs(i))
        result = builtin_sorting(array)
    return result


if __name__ == '__main__':
    run_builtin_sorting()
