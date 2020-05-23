# -*- coding: utf-8 -*-
"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n = int(input(f'How many friends? '))
graph = []

for i in range (1, n+1):
    for j in range (i+1, n+1):
        graph.append((i, j))

print(f'{n} friends made {len(graph)} handshakes')