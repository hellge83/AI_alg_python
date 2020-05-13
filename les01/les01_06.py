# -*- coding: utf-8 -*-
"""
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""
a = int(input('1st side:'))
b = int(input('2nd side:'))
c = int(input('3rd side:'))

if ((a < b + c) & (b < a + c) & (c < a + b)):
    if (a == b) & (b == c):
        print('the triangle has 3 equal sides')
    elif (a == b) | (b == c) | (c == a):
        print('the triangle has 2 equal sides')
    else:
        print('the triangle has no equal sides')
else:
    print('the triangle doesn\'t exist')

