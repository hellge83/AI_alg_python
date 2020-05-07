# -*- coding: utf-8 -*-
"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""
import cProfile

def main(num):
    even, odd = 0, 0
    for i in num:
        if i in {'0', '2', '4', '6', '8'}:
            even += 1
        else:
            odd += 1
    return even, odd         

# print(main('1234567890')) 
    
cProfile.run("main('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')")

#  "les04_01_3.main('1234567890')"
# 1000 loops, best of 5: 683 nsec per loop    
# 4 function calls in 0.000 seconds 
    
# "les04_01_3.main('12345678901234567890123456789012345678901234567890')"
# 1000 loops, best of 5: 2.85 usec per loop
#  4 function calls in 0.000 seconds
    
# "les04_01_3.main('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')"
# 1000 loops, best of 5: 5.95 usec per loop
# 4 function calls in 0.000 seconds