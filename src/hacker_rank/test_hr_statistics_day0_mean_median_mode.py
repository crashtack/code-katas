import pytest
from hr_statistics_day0_mean_median_mode import mean, median, mode


TABLE1 = [
    ([1], 1.0, 1.0, 1),
    ([0, 1, 2, 3], 1.5, 1.5, 0),
    ([0, 1, 2], 1.0, 1.0, 0),
    ([0, 1, 1, 2], 1.0, 1.0, 1)
]


@pytest.mark.parametrize('lst, mean_, median_, mode_', TABLE1)
def test_mean(lst, mean_, median_, mode_):
    """Test that mean returns the mean of a list"""
    assert mean(lst) == mean_


@pytest.mark.parametrize('lst, mean_, median_, mode_', TABLE1)
def test_median(lst, mean_, median_, mode_):
    """Test that mean returns the mean of a list"""
    assert median(lst) == median_


@pytest.mark.parametrize('lst, mean_, median_, mode_', TABLE1)
def test_mode(lst, mean_, median_, mode_):
    """Test that mean returns the mean of a list"""
    assert mode(lst) == mode_
