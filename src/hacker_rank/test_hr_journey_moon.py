import pytest
from hr_journey_moon import journey_moon


PAR_TABLE = [
    ([2, 1], [1, 2]),
    ([1, 2], [1, 2]),
    ([0, 0, 0, 1], [0, 0, 0, 1]),
    ([1, 2, 4, 3], [1, 2, 3, 4]),
    ([2, 3, 4, 5, 6, 7, 8, 9, 10, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([], []),
]


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_journey_moon(arr, result):
    # import pdb; pdb.set_trace()
    # assert insertion_sort(arr) == result
    pass
