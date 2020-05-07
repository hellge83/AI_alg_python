"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""

num = '1234567890'
even = [itm for itm in num if not int(itm) % 2]
odd = [itm for itm in num if int(itm) % 2]
# print(f'{len(even)} even digits')
# print(f'{len(odd)} odd digits')