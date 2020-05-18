# -*- coding: utf-8 -*-
"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""
import random

def heapify(array, n, i):
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i] 

        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]  
        heapify(array, i, 0)

m = 5
lst = [random.randint(0, 50) for _ in range(m * 2 + 1)]
print(f'list: {lst}')
n = len(lst)
heap_sort(lst)
print(f'sorted: {lst}')
print(f'median: {lst[n // 2]}')