from functools import wraps
from typing import Generator


def my_range(start: int, end: int, step=1) -> Generator[int, None, None]:
    """
    :param start: start of range
    :type start: int
    :param end: end of range
    :type end: int
    :param step: step of range
    :type step: int
    :return generator object
    """
    if type(start) is int and \
            type(end) is int and \
            type(step) is int:
        while start < end:
            yield start
            start += step
    else:
        raise TypeError('All parameters must be integers')


def my_cache(should_save=True):
    def my_cache_dec(func):
        cache_dict = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            if args in cache_dict:
                return cache_dict[args]
            else:
                result = func(*args, **kwargs)
                if should_save is True:
                    cache_dict[args] = result
                    return result
                elif should_save is False:
                    return result
                else:
                    raise TypeError('should_save parameter '
                                    'must be boolean')

        return wrapper

    return my_cache_dec


def my_sum(a, b):
    return f'The sum is {a + b}'


def no_params():
    return 'Something is written'
