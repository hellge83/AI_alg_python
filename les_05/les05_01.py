# -*- coding: utf-8 -*-
"""
1. Пользователь вводит данные о количестве предприятий, 
их наименования и прибыль за четыре квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) 
и отдельно вывести наименования предприятий, чья прибыль выше среднего 
и ниже среднего.
"""
import collections as c

num = int(input('factories total: '))
factory = {}

while num > 0:
    p = input('input factory name: ')
    defdict = c.defaultdict(list)
    for i in range(1, 5):
        val = int(input(f'q{i} revenue: '))
        defdict[p].append(val)
    factory.update(defdict)
    num-=1

totals = {k: sum(v) for (k, v) in factory.items()}
avg = sum(totals.values()) / len(totals.values())

less, more = [], []
for k, v in totals.items():
    if v < avg:
        less.append(k)
    elif v > avg:
        more.append(k)

# print(factory)
print(f'factory totals: {totals}')
# print(f'average rev: {avg}')
print(f'factory rev less than average {avg}: {less}')    
print(f'factory rev more than average {avg}: {more}')      