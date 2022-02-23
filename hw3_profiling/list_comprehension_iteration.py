
from memory_profiler import profile

my_arr = [22, 55, 77, 34, 65, 23, 76, 45, 323, 76]


def list_comprehension_iteration(arr):
    new_list = [i ** 2 for i in arr]
    return new_list


@profile
def run_list_comprehension_iteration():
    for i in range(5000, 20000, 100):
        result = list_comprehension_iteration(arr=my_arr)
    return result


if __name__ == '__main__':
    run_list_comprehension_iteration()
