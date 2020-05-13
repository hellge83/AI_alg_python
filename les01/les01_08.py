# -*- coding: utf-8 -*-
"""
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = a + b + c - min(a, b, c) - max(a, b, c)

print(f'middle number is {d}')