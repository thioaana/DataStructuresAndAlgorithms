#Uses python3

import sys

from queue import PriorityQueue

class Graph :
    def __init__(self, n) :
        self.numOfVertices = n
        self.graph = [[] for _ in range(self.numOfVertices)]
        self.weights = [[] for _ in range(self.numOfVertices)]

    # Return the number of Vertices
    def getNumOfVertices(self) :
        return self.numOfVertices

    # Return the number of Edges
    def getNumOfEdges(self) :
        edges = 0
        for v in self.graph :
            for e in v :
                edges += 1
        return edges

    # Import an Edge e from Vertex v to Vertex e
    def importEdge(self, u, v, w) :
       self.graph[u].append(v)
       self.weights[u].append(w)

    def isNegativeCycle(self, s, checked):
        self.S = s
        self.dist = [sys.maxsize] * self.numOfVertices
        self.prev = [-1] * self.numOfVertices
        self.dist[self.S] = 0
        # visited = ["dummy", "dummy"] # In order to enter the for loop.
        # oldDist = [d for d in self.dist]
        # i = 0
        # while i < len(visited)+2 :
        for V in range(self.numOfVertices-1) :
            # if V > 0 and self.dist == oldDist :
            #     break
            # oldDist = [d for d in self.dist]
            queue = [self.S]
            visited = []
            while queue != []:
                u = queue.pop(0)
                visited.append(u)
                checked[u] = True
                for v in self.graph[u] :
                    if v not in visited :
                        queue.append(v)
                    if self.dist[v] > self.dist[u] + self.weights[u][self.graph[u].index(v)] :
                        self.dist[v] = self.dist[u] + self.weights[u][self.graph[u].index(v)]
                        self.prev[v] = u
            # i += 1
        # oldDist = [d for d in self.dist]
        for u in range(self.numOfVertices) :
            for v in self.graph[u] :
                if self.dist[u] != sys.maxsize and self.dist[v] > self.dist[u] + self.weights[u][self.graph[u].index(v)]: # if (dist[u] != Integer.MAX_VALUE & & dist[u] + weight < dist[v]) - From Java
                    return True
        # if self.dist != oldDist :
        #     return True
        return False

    def hasNegativeCycle(self):
        checked = [False] * self.numOfVertices # For every set of conected components the relevant indexes are turned into True
        for node in range(self.numOfVertices):
            if not checked[node] :
                if self.isNegativeCycle(node, checked) :
                     return 1
        return 0

    def printGraph(self) :
        printList = []
        printList.append((self.numOfVertices, self.getNumOfEdges()))
        for v in range(self.numOfVertices) :
            for e in self.graph[v] :
                printList.append((v, e))
        return printList


if __name__ == '__main__':

    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    edges = []
    for i in range(m):
        inp = input().split()
        edges.append((int(inp[0]), int(inp[1]), int(inp[2])))

    myGraph = Graph(n)
    for (a, b, w) in edges:
        myGraph.importEdge(a - 1, b - 1, w)
    print(myGraph.hasNegativeCycle())
    # print(myGraph.negative_cycle())

#  --------------- H E L P -----------------
# For instance, you can initialize all distances with zero, essentially adding a new vertex and 0-edges from it to all of the nodes.
# It does not affect the existence of a negative cycle.