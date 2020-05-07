# -*- coding: utf-8 -*-
"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random



a = [random.randint(0, 5) for _ in range(20)]
print(a)

num = set(a)
tmp = {}
for itm in num:
    qty = [el for el in a if el == itm]
    tmp[itm] = len(qty)

# print(tmp)    

# максимум, не используя встроенную max    
mx = 0
for itm in tmp.values():
    if itm > mx:
        mx = itm

res = [k for k, v in tmp.items() if v == mx]

# беру самый первый элемент, ткк в условии сказано 
# "один любой по вашему выбору"
print(res[0])