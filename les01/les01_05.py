# -*- coding: utf-8 -*-
"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква
"""
import string

num = input('input letter position (1..26):')

c = string.ascii_lowercase[int(num) - 1]

print(f'the {num}-th letter is: {c}')

