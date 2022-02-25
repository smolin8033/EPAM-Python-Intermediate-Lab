
from memory_profiler import profile

my_arr = [22, 55, 77, 34, 65, 23, 76, 45, 323, 76]


def forloop_iteration(arr):
    new_list = []
    for i in arr:
        new_list.append(i ** 2)
    return new_list


@profile
def run_forloop_iteration():
    for i in range(5000, 20000, 100):
        result = forloop_iteration(arr=my_arr)
    return result


if __name__ == '__main__':
    run_forloop_iteration()
