# python3

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6) # max depth of recursion

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A function used by DFS

    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        # print(v, end=" ")
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

        # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

        # The main function that finds and prints all strongly

    # connected components
    def printSCCs(self):
        numSCC = 0
        stack = []
        # Mark all the vertices as not visited (For first DFS)

        visited = [False] * (self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

                # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                numSCC +=1
                # print()
        print(numSCC)
if __name__ == "__main__" :
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    # Create a graph given in the above diagram
    g = Graph(n)
    for i in range(m):
        g.addEdge(edges[i][0] - 1, edges[i][1] - 1)


    # g = Graph(5)
    # g.addEdge(1, 0)
    # g.addEdge(2, 1)
    # g.addEdge(2, 0)
    # g.addEdge(3, 2)
    # g.addEdge(3, 0)
    # g.addEdge(4, 1)
    # g.addEdge(4, 2)

    g.printSCCs()