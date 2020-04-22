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

    def isNegativeCycle(self, s):
        self.S = s
        self.dist = [sys.maxsize] * self.numOfVertices
        self.prev = [-1] * self.numOfVertices
        self.dist[self.S] = 0

        for V in range(self.numOfVertices - 1) :
            oldDist = [d for d in self.dist]
            visited = [False] * self.numOfVertices
            queue = [self.S]
            while queue != []:
            # for V2 in range(self.numOfVertices) :
                u = queue.pop(0)
                visited[u] = True
                for v in self.graph[u] :
                    if not visited[v] :
                        queue.append(v)
                    if self.dist[v] > self.dist[u] + self.weights[u][self.graph[u].index(v)] :
                        self.dist[v] = self.dist[u] + self.weights[u][self.graph[u].index(v)]
                        self.prev[v] = u
        for i in range(self.numOfVertices - 1) :
            if self.dist[i] != oldDist[i] :
                return True
        return False

    def hasNegativeCycle(self):
        # write your code here
        checked = [i for i in range(self.numOfVertices)]
        while checked != []
            result = self.isNegativeCycle(checked[0])
            if result : return 1
            for v in self.prev :
                del checked
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
