from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdges(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self, v):
        visited = [False] * (max(self.graph)+1)
        self.DFSUtil(v, visited)



n = int(input())

vertices = []
for i in range(n):
    vertices.append(int(input()))