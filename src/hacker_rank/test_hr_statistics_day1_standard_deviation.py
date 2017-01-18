import pytest
from hr_statistics_day1_standard_deviation import standard_deviation


TABLE1 = [
    ([10, 40, 30, 50, 20], 14.1),
    # ([3, 7, 8, 5, 12, 14, 21, 15, 18, 14], [7, 13, 15]),
    # ([0, 1, 2], 1.0, 1.0, 0),
    # ([0, 1, 1, 2], 1.0, 1.0, 1)
]


@pytest.mark.parametrize('lst, result', TABLE1)
def test_mean_standard_deviation(lst, result):
    """Test that quartiles returns the q1,q2,q3 in a list"""
    assert standard_deviation(lst) == result
