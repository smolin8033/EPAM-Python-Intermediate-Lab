
from memory_profiler import profile

my_arr = [5, 9, 3, 6, 0, 1, 7, 2, 8, 4]


def quick_sorting(arr):
    if len(arr) < 2:
        return arr
    else:
        base = arr[0]
        less = [i for i in arr[1:] if i <= base]
        more = [i for i in arr[1:] if i > base]
        return quick_sorting(less) + [base] + quick_sorting(more)


@profile
def run_quick_sorting():
    for i in range(-350, 0):
        result = quick_sorting(arr=my_arr)
    return result


if __name__ == '__main__':
    run_quick_sorting()
