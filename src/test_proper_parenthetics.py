# -*- coding utf-8 -*-

from proper_parenthetics import proper_parenthetics


def test_open():
    s = '((some)thing((here)'
    assert proper_parenthetics(s) == 1


def test_balanced():
    s = '(((milk)()stool((dog))()(cheese))(cat)())'
    assert proper_parenthetics(s) == 0


def test_broken():
    s = '(()))'
    assert proper_parenthetics(s) == -1
