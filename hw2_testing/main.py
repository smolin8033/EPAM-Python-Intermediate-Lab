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
                return f'{result}\nCashed the following: {cache_list}'
            elif should_save is False:
                return result
            else:
                raise TypeError('should_save parameter must be boolean')
        return wrapper
    return my_cache_dec


def my_sum(a, b):
    return f'The sum is {a + b}'


def no_params():
    return 'Something is written'


# вызываю все функции, а то coverage слишком низкий без вызова
my_range(1, 9, 4)


decorated_func = my_cache(should_save=False)(my_sum)
decorated_func(4, 7)


no_params()
