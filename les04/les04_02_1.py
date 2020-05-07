# -*- coding: utf-8 -*-
"""
n-e простое число - решето Эратосфена
"""
import cProfile
from math import sqrt

def erato(a, b, lst):
    for i in range(a, b):
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return(lst)
    
def main(n):
    # n = 20
    tmp = n
    
    lst=[]
    erato(2, n+1, lst)
            
    while len(lst)<n:
        erato(tmp+1, tmp+2, lst)
        tmp +=1
    
    res = lst[len(lst)-1]
    return(res)

# print(main(15))
cProfile.run("main(1000)")    
    
#  "les04_02_1.main(10)"
# 1000 loops, best of 5: 30.5 usec per loop
# 107 function calls in 0.000 seconds
    
# "les04_02_1.main(100)"
# 1000 loops, best of 5: 900 usec per loop
# 2490 function calls in 0.001 seconds
    
# "les04_02_1.main(200)"
# 1000 loops, best of 5: 2.05 msec per loop
# 6067 function calls in 0.003 seconds
    
# "les04_02_1.main(1000)"
# 1000 loops, best of 5: 19.3 msec per loop
# 49139 function calls in 0.024 seconds