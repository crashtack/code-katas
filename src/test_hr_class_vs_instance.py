import pytest
from hr_class_vs_instance import class_vs_instance


PAR_TABLE = [
    (1, "Weird"),
    (2, "Not Weird"),
    (8, "Weird"),
    (22, "Not Weird"),
]


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_class_vs_instance(arr, result):
    assert class_vs_instance(arr) == result
