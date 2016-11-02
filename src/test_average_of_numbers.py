import pytest
from average_of_numbers import averages


PAR_TABLE = [
    ([2, 2, 2, 2], [2, 2, 2, 2, 2]),
    ([0, 0, 0, 0], [2, -2, 2, -2, 2]),
    ([2, 4, 3, -4.5], [1, 3, 5, 1, -10]),
    ([], []),
    ([], None),
]


@pytest.mark.parametrize('result, arr', PAR_TABLE)
def test_averages(result, arr):
    # import pdb; pdb.set_trace()
    assert averages(arr) == result
