# -*- coding: utf-8 -*-
"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр
 и вывести на экран. Например, если введено число 3486, надо вывести 6843.
"""

# res = []
num = int(input('input number: '))
# while num >0:
#     res.append(str(num % 10))
#     num //= 10
    
# print(int(''.join(map(str, res))))

res = ''
while num >0:
    res = res + str(num % 10)
    num //= 10
    
print(res)