# -*- coding: utf-8 -*-
"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба минимальны), так и различаться.
"""
import random

def bubble(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return(x)


a = [random.randint(1, 50) for _ in range(10)]
print(a)

# b = sorted(a)
b = bubble(a)


res = b[:2]
# print(b)
print(res)