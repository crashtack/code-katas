import pytest
from merge_sorted_lists import merge_sorted_lists

PAR_TABLE = [
    ([1], [2], [1, 2]),
    ([1], [], [1]),
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
]


@pytest.mark.parametrize('list1, list2, result', PAR_TABLE)
def test_merge_sorted_lists(list1, list2, result):
    """Test that merge_sorted_lists returns a sorted list
       containing list1 and list2
    """
    assert merge_sorted_lists(list1, list2) == result
