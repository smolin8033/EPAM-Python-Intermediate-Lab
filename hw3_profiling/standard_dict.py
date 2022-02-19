
from memory_profiler import profile


def standard_dict(arr):
    new_dict = {}
    for i in arr:
        new_dict[i] = f'The value is {i}'
    try:
        print(new_dict['someting'])
    except KeyError:
        return None


@profile
def run_standard_dict():
    array = []
    for i in range(100, 1000000, 200):
        array.append(i)
        result = standard_dict(array)
    return result


if __name__ == '__main__':
    run_standard_dict()
