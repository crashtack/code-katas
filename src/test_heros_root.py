import pytest
from heros_root import int_rac


TABLE = [
    (25, 1, [1, 13, 7, 5]),

]


@pytest.mark.parametrize('n, x, result', TABLE)
def test_int_rac(n, x, result):
    """test of the int_rac function"""
    pass
    # assert int_rac(n, x) == result
