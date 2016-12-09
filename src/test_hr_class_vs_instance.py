import pytest
# from hr_class_vs_instance import class_vs_instance
from hr_class_vs_instance import Person


PAR_TABLE = [
    (1, 1),
    (-1, 0),
    (8, 8),
    (0, 0),
]

OLD_TABLE = [
    (0, "You are young."),
    (12, "You are young."),
    (13, "You are a teenager."),
    (17, "You are a teenager."),
    (19, "You are old."),
    (99, "You are old."),
]


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_class_vs_instance_init(arr, result):
    """Test the init method for class Person"""
    p1 = Person(arr)
    assert p1.age == result


@pytest.mark.parametrize('arr, result', PAR_TABLE)
def test_class_vs_instance_yearPasses(arr, result):
    """Test the yearPasses method for class Person"""
    p1 = Person(arr)
    p1.yearPasses()
    assert p1.age == result + 1


@pytest.mark.parametrize('arr, result', OLD_TABLE)
def test_class_vs_instance_amIOld(arr, result):
    """Test the yearPasses method for class Person"""
    p1 = Person(arr)
    assert p1.amIOld() == result
