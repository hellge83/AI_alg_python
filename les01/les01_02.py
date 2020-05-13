# -*- coding: utf-8 -*-
"""
2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
"""
x1 = int(input('input x1: '))
y1 = int(input('input y1: '))
x2 = int(input('input x2: '))
y2 = int(input('input y2: '))

k = (y2 - y1)/(x2 - x1)
b = (x2 * y1 - x1 * y2)/(x2 - x1)

print(f'y = {k} * x + {b}')