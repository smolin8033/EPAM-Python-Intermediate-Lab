# import pytest

from hw2_testing.main import my_range


def test_my_range_pos_pos():
    assert my_range(1, 5) == [1, 2, 3, 4]
