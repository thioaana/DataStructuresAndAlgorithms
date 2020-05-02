#Uses python3

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []
        self.count = 0

    def importEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # The function detects negative weight cycle
    def isNegativeCycle3(self, src):

        # Step 1: Initialization
        dist = [float("Inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            # if not sameValues : return False
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                self.count += 1
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return True

    def hasNegativeCycle(self):
        if self.isNegativeCycle(self.V - 1) :
            return 1
        return 0


if __name__ == '__main__':
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    edges = []
    for i in range(m):
        inp = input().split()
        edges.append((int(inp[0]), int(inp[1]), int(inp[2])))
    myGraph = Graph(n + 1)
    for (a, b, w) in edges:
        myGraph.importEdge(a - 1, b - 1, w)
    for i in range(n):
        myGraph.importEdge(n + 1 - 1, i, 0)
    print(myGraph.hasNegativeCycle())


    # # Testing ...........................
    # import random
    # import time
    # n = 1000
    # m = 10000
    # kkk = 0
    # # myGraph = Graph(n)
    # while kkk < n * m :
    #     start = time.time()
    #     myGraph = Graph(n+1)
    #     lList = []
    #     for i in range(1, m+1) :
    #         r1 = random.randint(1, n)
    #         r2 = random.randint(1, n)
    #         while (r1, r2) in lList or r1==r2:
    #             r1 = random.randint(1, n)
    #             r2 = random.randint(1, n)
    #         lList.append((r1, r2))
    #         myGraph.importEdge(r1 - 1, r2 - 1, random.randint(-1000, 1000))
    #     for i in range(n):
    #         myGraph.importEdge(n + 1 - 1, i, 0)
    #     # print(myGraph.hasNegativeCycle3())
    #     print(myGraph.hasNegativeCycle2()) # Additional node
    #     end = time.time()
    #     print(n, m, myGraph.count, end-start)
    #     kkk = myGraph.count
