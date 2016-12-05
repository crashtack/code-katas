import pytest
from hacker_rank_insertion_sort import insertion_sort


PAR_TABLE = [
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([0, 0, 0, 1], [0, 0, 0, 1]),
    ([1, 2, 4, 3], [1, 2, 3, 4]),
    ([2, 3, 4, 5, 6, 7, 8, 9, 10, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([], []),
]


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_inserstion_sort(arr, result):
    # import pdb; pdb.set_trace()
    assert insertion_sort(arr) == result
