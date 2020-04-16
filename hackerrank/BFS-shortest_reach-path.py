import collections 
import queue 
from collections import deque
import random as rand
import math as math
import time

class Graph:
    def __init__(self, n):
        self.List = {} #store graph u -> (v, w)
        self.n = n
    
    def connect(self, u, v, w = 6):
        if (u in self.List.keys()):
            self.List[u].append([w, v])
        else: 
            self.List[u] = [[w, v]]

        #because is an undirect graph
        if (v in self.List.keys()):
            self.List[v].append([w, u])
        else:
            self.List[v] = [[w, u]]

def find_all_distances(n, start):
    dist = [-1] * n
    visited = [False]* n
    
    q = queue.Queue()
    q.put(s)
    visited[s] = True
    dist[s] = 0

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                dist[v] = dist[u] + 1
    
    for i in range(n):
        if i == start:
            continue
        print(dist[i]*6 if dist[i] != -1 else '-1', end = ' ')
    print()


t = int(input())
for i in range(t):
    # n,m = [int(value) for value in input().split()]
    n,  m = map(int, input().split())

    graph = [[] for i in range(n)]
    # graph = Graph(n)

    for i in range(m):
        x,y = map(lambda x: int(x) - 1, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
        # graph.connect(x-1,y-1)
        
    s = int(input()) - 1
    find_all_distances(n, s)
