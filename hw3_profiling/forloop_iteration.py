
from memory_profiler import profile


def forloop_iteration(arr):
    new_list = []
    for i in arr:
        new_list.append(i ** 2)
    return new_list


@profile
def run_forloop_iteration():
    array = []
    for i in range(5000, 20000, 100):
        array.append(i)
        result = forloop_iteration(array)
    return result


if __name__ == '__main__':
    run_forloop_iteration()
