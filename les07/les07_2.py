# -*- coding: utf-8 -*-
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

def merge(left, right):
    result = []
    i, j = 0, 0
    for _ in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    
        elif i == len(left):
            result.append(left[j])
            j += 1
        elif j == len(right):
            result.append(right[i])
            i += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return(array)
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)



lst = [random.randint(0, 50) for _ in range(10)]    
print(f'array: {lst}')

print(f'sorted: {merge_sort(lst)}')