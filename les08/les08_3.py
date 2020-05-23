# -*- coding: utf-8 -*-
"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random

def random_graph(n):
    g = []

    for i in range(n):
        edges = random.sample(range(0, n), random.randint(1, n-1))
        for el in edges:
            if el == i:
                edges.remove(el) #remove loops
        g.append(edges)
    
    return(g)

# graph = [[2, 4, 6],
#             [9],
#             [0, 3],
#             [2, 4],
#             [0, 3],
#             [],
#             [0, 7, 8],
#             [6],
#             [6],
#             [1]]


def dfs(v, g):
    visited[v] = True
    for w in g[v]:
        if not visited[w]:  
            dfs(w, g)
    
    return(visited)

vert = 7
graph = random_graph(vert)

visited = [False] * len(graph)  

s = int(input('start vertex: '))
print(dfs(s, graph))


