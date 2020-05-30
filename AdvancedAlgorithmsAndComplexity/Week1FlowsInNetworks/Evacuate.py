#Uses python3

import sys

class Graph :
    def __init__(self, n) :
        self.numOfVertices = n
        self.numOfEdges = 0
        self.graph = [[] for _ in range(self.numOfVertices)]
        self.capacity = {}
        self.prev = [-1] * self.numOfVertices

    # Import an Edge from Vertex u to Vertex v
    def importEdge(self, u, v, capacity) :
        if u != v :                                 # In case u = v
            if v in self.graph[u] :                 # In case u-v edge already exists
                self.capacity[(u, v)] += capacity
            else :
                self.capacity[(u, v)] = capacity
                self.graph[u].append(v)
                self.numOfEdges += 1


    def deleteEdge(self, u, v):
        self.numOfEdges -= 1
        self.graph[u].remove(v)
        del self.capacity[(u, v)]

def printGraph(self) :
        printList = []
        printList.append((self.numOfVertices, self.getNumOfEdges()))
        for v in range(self.numOfVertices) :
            for e in self.graph[v] :
                printList.append((v, e))
        return printList

    # Create BFS(u)
    def BFS(self, u) :
        self.S = u
        self.dist = [sys.maxsize] * self.numOfVertices
        self.prev = [-1] * self.numOfVertices
        self.dist[u] = 0
        queue = [self.S]
        while queue != [] :
            u = queue.pop(0)
            for v in self.graph[u] :
                if self.dist[v] == sys.maxsize :
                    queue.append(v)
                    self.dist[v] = self.dist[u] + 1
                    self.prev[v] = u

    def ReconstructPath(self, v) :
        result = []
        if self.dist[v] == sys.maxsize :
            return result
        while v != self.S:
            result.append(v)
            v = self.prev[v]
        return result

    def ComputeGf(self):
        # minFlow = self.getMinFlowInPath()
        # Compute minimum capacity in a path.
        minFlow = sys.maxsize
        u = self.numOfVertices - 1
        if self.prev[u] == -1:
            return 0
        while u != 0 :
            if self.capacity[(self.prev[u], u)] < minFlow :
                minFlow = self.capacity[(self.prev[u], u)]
            u = self.prev[u]

        # Update capacities in G and Gf(residual graph).
        u = self.numOfVertices - 1
        while u != 0 :
            if (u, self.prev[u]) in self.capacity.keys() :
                self.capacity[(u, self.prev[u])] += minFlow
            else :
                self.importEdge(u, self.prev[u], minFlow)

            self.capacity[(self.prev[u], u)] -= minFlow
            if self.capacity[(self.prev[u], u)] == 0 :
                self.deleteEdge(self.prev[u], u)

            u = self.prev[u]
        return minFlow

    def FordFulkerson(self):
        flow = 0
        self.BFS(0)
        while True :
            minFlow = self.ComputeGf()
            flow += minFlow
            self.BFS(0)
            if self.prev[self.numOfVertices - 1] == -1:
                return flow

if __name__ == '__main__':
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    myGraph = Graph(n)
    for i in range(m):
        inp = input().split()
        myGraph.importEdge(int(inp[0]) - 1, int(inp[1]) - 1, int(inp[2]))

    print(myGraph.FordFulkerson())


