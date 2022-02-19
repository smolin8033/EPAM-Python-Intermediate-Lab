
from memory_profiler import profile


def recursive_flatten(arr):
    new_list = []
    for i in arr:
        if isinstance(i, list):
            new_list.extend(recursive_flatten(i))
        else:
            new_list.append(i)
    return new_list


@profile
def run_recursive_flatten():
    array = []
    for i in range(1000):
        array.append([1, [1, 1, [486, 453, 342, [3653, 3543, 76757, [2, 5, 3, 4]]]]])
        result = recursive_flatten(array)
    return result


if __name__ == '__main__':
    run_recursive_flatten()
