# -*- coding: utf-8 -*-
"""
6. В программе генерируется случайное целое число от 0 до 100. 
Пользователь должен его отгадать не более чем за 10 попыток. 
После каждой неудачной попытки должно сообщаться, больше или меньше 
введенное пользователем число, чем то, что загадано. 
Если за 10 попыток число не отгадано, вывести ответ.
"""
import random 

number = random.randint(1, 100)
for i in range(10):
    num = int(input('input your guess: '))
    if num > number:
        print(f'{num} is more than number')
    elif num < number:
        print(f'{num} is less than number')
    else:
        print(f'you win! {num} is the number')
        break
if num != number:
    print (f'The number is {number}')