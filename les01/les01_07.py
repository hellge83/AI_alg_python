# -*- coding: utf-8 -*-
"""
7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
num_year = input('year: ')

if not int(num_year) % 4:
    print(f'{num_year} is a leap year')
else:
    print(f'{num_year} is a non-leap year')

