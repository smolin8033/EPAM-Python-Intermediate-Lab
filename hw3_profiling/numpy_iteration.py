
from memory_profiler import profile
import numpy as np

my_arr = [22, 55, 77, 34, 65, 23, 76, 45, 323, 76]


def numpy_iteration(arr):
    new_arr = np.power(arr, 2).tolist()
    return new_arr


@profile
def run_numpy_iteration():
    for i in range(5000, 20000, 100):
        result = numpy_iteration(arr=my_arr)
    return result


if __name__ == '__main__':
    run_numpy_iteration()
