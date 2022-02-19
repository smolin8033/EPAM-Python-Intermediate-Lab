
from memory_profiler import profile


def builtin_methods_dict(arr):
    new_dict = dict()
    for i in arr:
        new_dict.update({i: f'The value is {i}'})
    return new_dict.get('someting', None)


@profile
def run_builtin_methods_dict():
    array = []
    for i in range(100, 1000000, 200):
        array.append(i)
        result = builtin_methods_dict(array)
    return result


if __name__ == '__main__':
    run_builtin_methods_dict()
