# -*- coding: utf-8 -*-
"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""


bit_and = 5 & 6
bit_or = 5 | 6
mv_left = 5 >> 2
mv_right = 5 << 2
print(f'5 and 6: {bit_and}')
print(f'5 or 6: {bit_or}')
print(f'move 5 >> 2: {mv_left}')
print(f'move 5 << 2: {mv_right}')