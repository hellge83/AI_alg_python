# -*- coding: utf-8 -*-
"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
import random

def bubble(x):
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return(x)


a = [random.randint(-10, 10) for _ in range(10)]
print(a)

b = bubble([itm for itm in a if itm < 0])

res = b[len(b)-1]
print(res)