
from memory_profiler import profile


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
    array = []
    for i in range(-350, 0):
        array.append(abs(i))
        result = quick_sorting(array)
    return result


if __name__ == '__main__':
    run_quick_sorting()
