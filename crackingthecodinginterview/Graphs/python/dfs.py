# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(set)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].add(v)

    # A function used by DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)

        for next in self.graph[start] - visited:
            self.dfs(next, visited)
        return visited

# Driver code


# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(0)

# This code is contributed by Neelam Yadav
