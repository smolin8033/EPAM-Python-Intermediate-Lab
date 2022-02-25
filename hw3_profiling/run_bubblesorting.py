
from memory_profiler import profile

my_arr = [5, 9, 3, 6, 0, 1, 7, 2, 8, 4]


def bubble_sorting(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


@profile
def run_bubble_sorting():
    for i in range(-350, 0):
        result = bubble_sorting(arr=my_arr)
    return result


if __name__ == '__main__':
    run_bubble_sorting()
