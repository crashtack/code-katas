import pytest
from hr_day7_arrays import reverse_list


PAR_TABLE = [
    ([1], [1]),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
]


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_reverse_list(arr, result):
    assert reverse_list(arr) == result
