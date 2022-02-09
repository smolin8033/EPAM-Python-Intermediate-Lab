import pytest

from hw2_testing.main import my_range


def test_my_range_no_parameters():
    with pytest.raises(TypeError) as e:
        my_range()

    assert str(e.value) == "my_range() missing 2 required positional " \
                           "arguments: 'start' and 'end'"


def test_my_range_pos_pos():
    assert my_range(1, 5) == [1, 2, 3, 4]
