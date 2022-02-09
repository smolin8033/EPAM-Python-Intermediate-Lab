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


def test_my_range_give_string():
    with pytest.raises(TypeError):
        my_range('1', 10)


def test_my_range_give_2_strings():
    with pytest.raises(TypeError):
        my_range('1', '10')


def test_my_range_pos_pos():
    assert my_range(1, 5) == [1, 2, 3, 4]


def test_my_range_zero():
    assert my_range(0, 0) == [0]


def test_my_range_with_step():
    assert my_range(1, 9, 4) == [1, 5]
