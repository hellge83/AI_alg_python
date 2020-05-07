"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) 
и 2 нечетные (3 и 5).
"""
import cProfile

def main(num):
    even = [itm for itm in num if not int(itm) % 2]
    odd = [itm for itm in num if int(itm) % 2]
    return(len(even), len(odd))

# print(main('1234567890')) 
    
cProfile.run("main('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')")
    
# "les04_01_1.main('1234567890')"
# 1000 loops, best of 5: 6.95 usec per loop
#  8 function calls in 0.000 seconds
    
# "les04_01_1.main('12345678901234567890123456789012345678901234567890')"
# 1000 loops, best of 5: 21.7 usec per loop
# 8 function calls in 0.000 seconds
    
# "les04_01_1.main('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')"
# 1000 loops, best of 5: 44.3 usec per loop
# 8 function calls in 0.000 seconds