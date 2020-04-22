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

    # Compute distance from s to t with Dijkstra Algorithm
    def distance(self, s, t):
        self.S = s
        self.dist = [sys.maxsize] * self.numOfVertices
        self.prev = [-1] * self.numOfVertices
        self.dist[self.S] = 0

        H = PriorityQueue()
        for v in range(self.numOfVertices) :
            H.put((self.dist[v], v))
        nodesToProcess = self.numOfVertices
        processed = [False] * self.numOfVertices
        while nodesToProcess > 0 :
            u = H.get()[1]
            while processed[u] :
                u = H.get()[1]
            nodesToProcess -=1
            processed[u] = True
            for v in self.graph[u] :
                if self.dist[v] > self.dist[u] + self.weights[u][self.graph[u].index(v)] :
                    self.dist[v] = self.dist[u] + self.weights[u][self.graph[u].index(v)]
                    self.prev[v] = u
                    H.put((self.dist[v], v)) # ChangePriority

        if self.dist[t] == sys.maxsize :
            return -1
        else :
            return self.dist[t]

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
        myGraph.importEdge(a-1, b-1, w)

    inp = input().split()
    s = int(inp[0]) - 1
    t = int(inp[1]) - 1
    print(myGraph.distance(s, t))
    # print(myGraph.printGraph())
