# -*- coding utf-8 -*-

from parenthetics import parenthetics


def test_open():
    s = '((some)thing((here)'
    assert parenthetics(s) == 1


def test_balanced():
    s = '(((milk)()stool((dog))()(cheese))(cat)())'
    assert parenthetics(s) == 0


def test_broken():
    s = '(()))'
    assert parenthetics(s) == -1


def test_broken2():
    s = ')))((('
    assert parenthetics(s) == -1
