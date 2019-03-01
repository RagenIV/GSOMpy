# coding: utf-8
# postfix_test.py

def calc(expr):
    '''
    >>> calc("1 2 + 4 * 3 +")
    '15'
    >>> calc("1 2 3 * + 2 -")
    '5'
    '''
    s = []
    for i in expr.split(" "):
        if i.isdigit():
            s.append(i)
        else:
            s.append(str(eval("({1}) {2} ({0})".format(s.pop(),s.pop(),i.replace('^','**')))))
    return s[0]

#print(calc("1 2 3 * + 2 -"))

print(calc("3 4 2 * 1 5 - 2 ^ / +"))
print(eval("3 + 4 * 2 / (1 - 5)**2"))

import doctest
doctest.testmod()
