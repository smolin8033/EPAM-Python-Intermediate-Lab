import pytest

from hw2_testing.main import my_cache, my_range, my_sum, cache_list


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


def test_my_range_give_string():
    with pytest.raises(TypeError):
        my_range('1', 10)


def test_my_range_give_2_strings():
    with pytest.raises(TypeError):
        my_range('1', '10')


def test_my_range_pos_pos():
    assert my_range(1, 5) == [1, 2, 3, 4]


def test_my_range_neg_neg():
    assert my_range(-10, -4) == [-10, -9, -8, -7, -6, -5]


def test_my_range_zero():
    assert my_range(0, 0) == [0]


def test_my_range_with_step():
    assert my_range(1, 9, 4) == [1, 5]


def test_my_range_float():
    assert my_range(1.5, 10.5, 4.5) == [1.5, 6]


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
