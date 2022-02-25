
from memory_profiler import profile

my_arr = [10, 50, 100, 35]


def second_dict(arr):
    new_dict = {}
    for i in arr:
        new_dict.update({i: f'The value is {i}'})
    return new_dict


@profile
def run_second_dict():
    for i in range(100, 1000000, 200):
        result = second_dict(my_arr)
    return result


if __name__ == '__main__':
    run_second_dict()
