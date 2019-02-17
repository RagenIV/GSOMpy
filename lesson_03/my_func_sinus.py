# coding: utf-8

import math

def f(x):
    if .2 <= x <= .9:
        return math.sin(x)
    else:
        return 1

print(f(float(input())))

