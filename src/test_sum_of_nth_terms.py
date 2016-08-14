# -*- coding: utf-8 -*-
import pytest


N_TABLE = [
    (1, '1.00'),
    (2, '1.25'),
    (3, '1.39'),
]


@pytest.mark.parametrize('n, result', N_TABLE)
def test_sum(n, result):
    from sum_of_nth_terms import series_sum
    assert series_sum(n) == result
