from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)

        for next in self.graph[start] - visited:
            self.dfs(next, visited)
        return visited

    def printKCores(self, k):
        # self.dfs(0)
        deleted_items = []
        for node, vertices in self.graph.items():
            if len(vertices) < k:
                for vertex in vertices:
                    self.graph[vertex].remove(node)
                deleted_items.append(node)
                del self.graph[node]


if __name__ == "__main__":
    k = 3
    g1 = Graph()
    g1.addEdge(0, 1)
    g1.addEdge(0, 2)
    g1.addEdge(1, 2)
    g1.addEdge(1, 5)
    g1.addEdge(2, 3)
    g1.addEdge(2, 4)
    g1.addEdge(2, 5)
    g1.addEdge(2, 6)
    g1.addEdge(3, 4)
    g1.addEdge(3, 6)
    g1.addEdge(3, 7)
    g1.addEdge(4, 6)
    g1.addEdge(4, 7)
    g1.addEdge(5, 6)
    g1.addEdge(5, 8)
    g1.addEdge(6, 7)
    g1.addEdge(6, 8)
    g1.printKCores(k)
