
from memory_profiler import profile


def nonrecursive_flatten(arr):
    nested = True
    while nested:
        new = []
        nested = False
        for i in arr:
            if isinstance(i, list):
                new.extend(i)
                nested = True
            else:
                new.append(i)
        arr = new
    return arr


@profile
def run_nonrecursive_flatten():
    array = []
    for i in range(1000):
        array.append([1, [1, 1, [486, 453, 342, [3653, 3543, 76757, [2, 5, 3, 4]]]]])
        result = nonrecursive_flatten(array)
    return result


if __name__ == '__main__':
    run_nonrecursive_flatten()
