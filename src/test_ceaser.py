import pytest
from ceaser import ceaser


TABLE = [
    ('', None, None),
    ("a", 2, "c"),
    ("M", 2, "o"),
    ("z", 2, "b"),
    ("aaa", 2, "ccc"),
    ('zzza', 4, "ddde"),
    ("a a z!", 2, 'c c b ')

]


def test_empty():
    assert ceaser() is None


def test_empty_string():
    assert ceaser('', 10) == ''


@pytest.mark.parametrize("message, shift, output", TABLE)
def test_shift_1(message, shift, output):
    assert ceaser(message, shift) == output
