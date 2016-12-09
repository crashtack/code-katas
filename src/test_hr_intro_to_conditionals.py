import pytest
from hr_intro_to_conditionals import conditional


PAR_TABLE = [
    (1, "Weird"),
    (2, "Not Weird"),
    (8, "Weird"),
    (22, "Not Weird"),
]


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_conditional(arr, result):
    assert conditional(arr) == result
