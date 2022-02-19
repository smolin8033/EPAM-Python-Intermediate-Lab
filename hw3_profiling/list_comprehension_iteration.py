
from memory_profiler import profile


def list_comprehension_iteration(arr):
    new_list = [i ** 2 for i in arr]
    return new_list


@profile
def run_list_comprehension_iteration():
    array = []
    for i in range(5000, 20000, 100):
        array.append(i)
        result = list_comprehension_iteration(array)
    return result


if __name__ == '__main__':
    run_list_comprehension_iteration()
