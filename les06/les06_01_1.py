"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""
import sys

def show_size(x, level=0):
    memory = 0
    print('\t' * level, f'type= {x.__class__}, size={sys.getsizeof(x)}, object= {x})')
    spam = sys.getsizeof(x) 
    
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                spam += show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                spam += show_size(xx, level + 1)
    
    memory += spam

    return memory

num = '1234567890'
even = [itm for itm in num if not int(itm) % 2]
odd = [itm for itm in num if int(itm) % 2]


print(len(even), len(odd))
print('--------------------')

_total = 0 # _ исключает саму _total из списка
for itm in dir():
    if itm[0] != '_' and not hasattr(locals()[itm], '__name__'):
        print(f'Variable: {itm}')
        _total += show_size(locals()[itm])
        
print(f'Total memory: {_total}') 




# 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] win32
# _total = 855