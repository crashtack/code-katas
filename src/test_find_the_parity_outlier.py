import pytest
from find_the_parity_outlier import find_outlier


TABLE = [
    ([1, 7, 3, 5, 2], 2),
    ([2, 3, 4], 3),
    ([2, 4, 0, 100, 11, 202], 11)
]


@pytest.mark.parametrize('list1, result', TABLE)
def test_find_outlier(list1, result):
    assert find_outlier(list1) == result
