import pytest

from hw0_intro.main import make_sum


def test_make_sum_positive_numbers():
    assert make_sum(10, 40) == 50


def test_make_sum_zero_number():
    assert make_sum(0, 30) == 30


def test_raise_type_error():
    with pytest.raises(TypeError):
        make_sum('a', 3)
