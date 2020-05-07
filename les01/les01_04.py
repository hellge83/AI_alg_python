# -*- coding: utf-8 -*-
"""
4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
import string

a = input('input first letter:')
b = input('input second letter:')

a1 = string.ascii_lowercase.index(a.lower(), 0) + 1
b1 = string.ascii_lowercase.index(b.lower(), 0) + 1

c = abs(b1 - a1) - 1

print(f'{a} position: {a1}')
print(f'{b} position: {b1}')
print(f'there are {c} letters between {a} and {b}')