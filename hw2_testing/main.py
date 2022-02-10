from functools import wraps

cache_list = []


def my_range(start, end, step=1):
    arr = [start]
    while start + step < end:
        start += step
        arr.append(start)
    return arr


def my_cache(should_save=True):
    def my_cache_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if should_save is True:
                cache_list.append(result)
                print(f'Cashed the following: {cache_list}')
                return result
            elif should_save is False:
                return result
            else:
                raise TypeError('should_save parameter must be boolean')
        return wrapper
    return my_cache_dec


@my_cache()
def my_sum(a, b):
    return f'The sum is {a + b}'


@my_cache()
def no_params():
    return 'Something is written'
