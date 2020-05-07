# -*- coding: utf-8 -*-
"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""

import cProfile

def main(num):
    num = int(num)
    even, odd = 0, 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    return even, odd         

# print(main('1234567890'))   
    
cProfile.run("main('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')")

# "les04_01_2.main('1234567890')"
# 1000 loops, best of 5: 1.57 usec per loop 
# 4 function calls in 0.000 seconds 
    
# "les04_01_2.main('12345678901234567890123456789012345678901234567890')"
# 1000 loops, best of 5: 15.6 usec per loop
# 4 function calls in 0.000 seconds
    
# "les04_01_2.main('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')"
# 1000 loops, best of 5: 29.6 usec per loop
# 4 function calls in 0.000 seconds