# -*- coding: utf-8 -*-
"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

def bubble(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                buff = x[j]
                x[j] = x[j+1]
                x[j+1] = buff
    return(x)


a = [random.randint(1, 100) for _ in range(10)]
print(a)


tmp = a.copy()
b = bubble(tmp)


res = [0 for _ in range(len(a))]
for i in range(len(a)):
    if i == a.index(b[0]):
        res[i] = b[len(b)-1]
    elif i == a.index(b[len(b)-1]):
        res[i] = b[0]
    else:
        res[i] = a[i]

print(res)

