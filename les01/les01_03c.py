# -*- coding: utf-8 -*-
"""
3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random
import string

a = input('input start letter:')
b = input('input end letter:')

a1 = string.ascii_lowercase.index(a, 0)
b1 = string.ascii_lowercase.index(b, 0)
c1 = random.randint(a1, b1)

c = string.ascii_lowercase[c1]

print(f'random letter from {a} to {b}: {c}')
