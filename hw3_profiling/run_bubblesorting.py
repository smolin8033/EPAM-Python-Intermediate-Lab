
from memory_profiler import profile


array = []


def bubble_sorting(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


@profile
def run_bubble_sorting():
    array = []
    for i in range(-350, 0):
        array.append(abs(i))
        result = bubble_sorting(array)
    return result


if __name__ == '__main__':
    run_bubble_sorting()
