
from memory_profiler import profile

my_arr = [4, 5, 6, [4, 7], 7, 4, [2, 8], 7, [4, 7, [3, 8, 5]], 9, 7, 8,
          [4, 9, [3, 9, [4, 8, [3, 6, 7, 3], 3], 5], 4], 9]


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
    for i in range(1000):
        result = recursive_flatten(arr=my_arr)
    return result


if __name__ == '__main__':
    run_recursive_flatten()
