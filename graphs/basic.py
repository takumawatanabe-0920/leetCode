
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def setEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
      stack = []
      visited = set()
      stack.append(s)
      while len(stack):
        cur = stack[-1]
        stack.pop()

        if cur not in visited:
          print(cur, 'dfs')
          visited.add(cur)
        for vertex in self.graph[cur]:
          if(vertex not in visited):
            stack.append(vertex)
      
    def bfs(self, s):
      queue = []
      queue.append(s)
      visited = set()

      while queue:
        cur = queue.pop(0)
        print(cur, 'bfs')

        for v in self.graph[cur]:
          if v not in visited:
                queue.append(v)
                visited.add(v)



g = Graph()
g.setEdge(2, 1)
g.setEdge(2, 5)
g.setEdge(5, 6)
g.setEdge(5, 8)
g.setEdge(6, 9)

g.dfs(2)
g.bfs(2)