# -*- coding: utf-8 -*-
"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 
32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: 
по десять пар «код-символ» в каждой строке.
"""

string = ''
for i in range(32, 128):
    if i % 10 == 1:
        unit = str(i) + '-' + chr(i) + ' ' + '\n'
    else:
        unit = str(i) + '-' + chr(i) + ' '
    string = string + unit
print(string)