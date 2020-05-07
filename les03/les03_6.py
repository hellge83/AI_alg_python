# -*- coding: utf-8 -*-
"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

def bubble(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return(x)


a = [random.randint(1, 100) for _ in range(10)]
print(a)

# b = sorted(a)
tmp = a.copy()
b = bubble(tmp)


# print(a.index(b[0]), a[a.index(b[0])])
# print(a.index(b[len(b)-1]), a[a.index(b[len(b)-1])])

if a.index(b[0]) < a.index(b[len(b)-1]):
    res = a[a.index(b[0])+1:a.index(b[len(b)-1])]
elif a.index(b[0]) > a.index(b[len(b)-1]):
    res = a[a.index(b[len(b)-1])+1:a.index(b[0])]
else:
    res = [a[a.index(b[0])]]

print(res)

total = 0
for i in range(len(res)):
    total += res[i]

print(total)    