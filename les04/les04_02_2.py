# -*- coding: utf-8 -*-
"""
n-e простое число - перебор делителей
"""
import cProfile

from math import sqrt
 
 
def is_sieve(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def main(n):
    # n = 20
    tmp = n
    sieve = [i for i in range(n)]
    result = [i for i in sieve if is_sieve(i)]
    
    while len(result) < n:
        if is_sieve(tmp):
            result.append(tmp)
        tmp +=1
    
    res = result[len(result)-1]
    return res


# print(main(15))

cProfile.run("main(1000)")    

    
# "les04_02_2.main(10)"
# 1000 loops, best of 5: 16.1 usec per loop
# 91 function calls in 0.000 seconds
    
# "les04_02_2.main(100)"
# 1000 loops, best of 5: 466 usec per loop
# 1606 function calls in 0.001 seconds
    
#  "les04_02_2.main(200)"
# 1000 loops, best of 5: 1.24 msec per loop
# 3631 function calls in 0.002 seconds

# "les04_02_2.main(1000)"
# 1000 loops, best of 5: 12.6 msec per loop
# 23597 function calls in 0.016 seconds
    

    
    