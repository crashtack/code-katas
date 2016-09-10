# -*- coding utf-8 -*-
import pytest
from parenthetics import parenthetics


PAR_TABLE = [
    ('((some)thing((here)', 1),
    ('(((milk)()stool((dog))()(cheese))(cat)())', 0),
    ('(()))', -1),
    (')))(((', -1)
]


@pytest.mark.parametrize('s, result', PAR_TABLE)
def test_parenthetics(s, result):
    assert parenthetics(s) == result
