from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited, queue = [], []
        visited.append(start)
        queue.append(start)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        
g = Graph(4)
g.add_edge(0, 1); 
g.add_edge(0, 2); 
g.add_edge(1, 2); 
g.add_edge(2, 0); 
g.add_edge(2, 3); 
g.add_edge(3, 3); 

print(g.graph)
visited, queue = [], []

print("Hello")
g.bfs(2)