
from memory_profiler import profile

my_arr = [10, 50, 100, 35]


def first_dict(arr):
    new_dict = {}
    for i in arr:
        new_dict[i] = f'The value is {i}'
    return new_dict


@profile
def run_first_dict():
    for i in range(100, 1000000, 200):
        result = first_dict(my_arr)
    return result


if __name__ == '__main__':
    run_first_dict()
