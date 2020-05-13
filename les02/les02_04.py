# -*- coding: utf-8 -*-
"""
4. Найти сумму n элементов следующего ряда чисел: 
1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""

series = 1
res = 1
num = int(input('input length: '))
for i in range(num-1):
    series = series / (-2)
    res += series
print(res)

# res = []
# num = int(input('input length: '))
# while num>0:
#     res.append(1/((-2)**(num-1)))
#     num-=1

# print(res)
# print(sum([itm for itm in res]))
