# -*- coding: utf-8 -*-
"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого — 
цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как 
[‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], 
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque


def hex_sum(x, y):
    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)
        
    z = deque()
    k = 0
    
    while x:
        if y:
            ind = (hexlist.index(x.pop()) + hexlist.index(y.pop()) + k)
        else:
            ind = (hexlist.index(x.pop()) + k)
        z.appendleft(hexlist[(ind % 16)])
    
        if ind > 15:
            k = 1
        else:
            k = 0

    if k:
        z.appendleft('1')
    return list(z)


def hex_mult(x, y):
    spam = deque()
    x, y = a.copy(), deque(b)
    zero = []
    while y:
        k = 0
        n = hexlist.index(y.pop())
        z = deque()
        for j in range(len(x)-1, -1, -1):
            ind = hexlist.index(x[j]) * n + k
            z.appendleft(hexlist[(ind % 16)])
            k = ind // 16
        if k:
            z.appendleft(str(k))
        z.extend(zero)
        zero.append('0')
        spam.appendleft(list(z))
        
    res = spam.popleft()
    while spam:
        res = hex_sum(res, spam.popleft())
    return(res)  


hexlist = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

a = list(input('input first hex nubmer: ').upper())
b = list(input('input second hex nubmer: ').upper())

print(f' HEX sum: {"".join(hex_sum(a, b))}')
print(f' HEX mult: {"".join(hex_mult(a, b))}')

 
        
    