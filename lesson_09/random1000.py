# coding:utf-8
# В условии не описаны ситуации с несколькими элементами, равными минимальному (максимальному)

import random

def gen_list(n=1000, mi=-1000, ma=1000):
    L = []
    for i in range(n):
        L.append(random.randint(mi, ma))
    return L

def count_negative(L):
    A = L.index(min(L))
    B = L.index(max(L))
    if B < A:
        B, A = A, B
    neg = 0
    for i in range(A, B+1):
        if L[i] < 0:
            neg += 1
    return neg

t = gen_list()
# print(t)
print(count_negative(t))
