import pytest
from hr_statistics_day0_weightedmean import weighted_mean


TABLE1 = [
    ([1], [1], 1.0),
    ([10, 40, 30, 50, 20], [1, 2, 3, 4, 5], 32.0)
    # ([0, 1, 2], 1.0, 1.0, 0),
    # ([0, 1, 1, 2], 1.0, 1.0, 1)
]


@pytest.mark.parametrize('lst, weight, wm', TABLE1)
def test_mean_mean(lst, weight, wm):
    """Test that mean returns the mean of a list"""
    assert weighted_mean(lst, weight) == wm
