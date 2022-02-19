
from memory_profiler import profile
import numpy as np


def numpy_iteration(arr):
    new_arr = np.power(arr, 2).tolist()
    return new_arr


@profile
def run_numpy_iteration():
    array = []
    for i in range(5000, 20000, 100):
        array.append(i)
        result = numpy_iteration(array)
    return result


if __name__ == '__main__':
    run_numpy_iteration()
