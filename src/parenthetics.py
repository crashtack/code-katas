# -*- coding utf-8 -*-
from stack import Stack


def parenthetics(s):
    '''tests for Proper Parenthetics
        returns 1 if string is 'open' (non-closed open parens)
        returns 0 of string is balenced (open and closing parens match)
        returns -1 if string is broken (a closing paren has not been followed
                                        by an open paren)
    '''
    stk = Stack()
    for c in s:
        if c == '(':
            stk.push(c)
        if c == ')':
            try:
                stk.pop()
            except IndexError:
                return -1
    try:
        stk.pop()
        return 1
    except IndexError:
        return 0
