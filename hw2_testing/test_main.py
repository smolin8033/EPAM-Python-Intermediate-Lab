import pytest

from hw2_testing.main import my_range


def test_my_range_no_parameters():
    with pytest.raises(TypeError) as e:
        my_range()

    assert str(e.value) == "my_range() missing 2 required positional " \
                           "arguments: 'start' and 'end'"


def test_my_range_one_parameter():
    with pytest.raises(TypeError) as e:
        my_range(10)

    assert str(e.value) == "my_range() missing 1 required positional argument: 'end'"


def test_my_range_too_many_params():
    with pytest.raises(TypeError):
        my_range(1, 10, 3, 15)


def test_my_range_initial():
    gen = my_range(1, 4)
    assert next(gen) == 1


def test_my_range_pos_pos():
    gen = my_range(1, 3)
    next(gen)
    assert next(gen) == 2


def test_my_range_stop_iter():
    gen = my_range(1, 2)
    next(gen)
    with pytest.raises(StopIteration):
        next(gen)


def test_my_range_neg_neg():
    gen = my_range(-10, -8)
    next(gen)
    assert next(gen) == -9


def test_my_range_with_step():
    gen = my_range(1, 9, 4)
    next(gen)
    assert next(gen) == 5


def test_my_range_end_not_included():
    gen = my_range(1, 9, 4)
    next(gen)
    next(gen)
    with pytest.raises(StopIteration):
        next(gen)


def test_my_range_float():
    gen = my_range(1.5, 9, 5)
    with pytest.raises(TypeError) as e:
        next(gen)

    assert str(e.value) == 'All parameters must be integers'


"""

def test_decorated_my_sum_default():
    decorated_func = my_cache()(my_sum)
    assert decorated_func(10, 5) == "The sum is 15\nCashed the following: ['The sum is 15']"
    cache_list.clear()


def test_decorated_my_sum_true():
    decorated_func = my_cache(should_save=True)(my_sum)
    assert decorated_func(11, 7) == "The sum is 18\nCashed the following: ['The sum is 18']"
    cache_list.clear()


def test_decorated_my_sum_false():
    decorated_func = my_cache(should_save=False)(my_sum)
    assert decorated_func(11, 7) == "The sum is 18"


def test_decorated_my_sum_not_boolean():
    with pytest.raises(TypeError) as e:
        decorated_func = my_cache(should_save='1')(my_sum)
        decorated_func(11, 7)

    assert str(e.value) == "should_save parameter must be boolean"


def test_decorated_my_sum_typo():
    with pytest.raises(TypeError) as e:
        decorated_func = my_cache(shoud_save='True')(my_sum)
        decorated_func(11, 7)

    assert str(e.value) == "my_cache() got an unexpected keyword argument 'shoud_save'"


def test_decorated_no_params():
    decorated_func = my_cache()(no_params)
    assert decorated_func() == "Something is written\n" \
                               "Cashed the following: ['Something is written']"
    cache_list.clear()
"""
