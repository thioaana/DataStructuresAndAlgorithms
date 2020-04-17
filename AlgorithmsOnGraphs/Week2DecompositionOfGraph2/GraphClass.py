import sys

class Graph :
    def __init__(self, n) :
        self.numOfVertices = n
        self.graph = [[] for _ in range(self.numOfVertices)]

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
    def importEdge(self, v, e) :
       self.graph[v].append(e)

    # Return Topological Ordering
    def toposort(self) :
        def dfs(visited, order, x):
            visited[x] = True
            for i in self.graph[x]:
                if not visited[i]:
                    dfs(visited, order, i)
                    order.append(i)

        order = []
        visited = self.numOfVertices * [False]
        for v in range(self.numOfVertices):
            if not visited[v]:
                dfs(visited, order, v)
                order.append(v)
        order.reverse()
        return order

    def hasCycle(self):
        def isCyclic(v, visited, stack):

            # Mark current node as visited and
            # adds to recursion stack
            visited[v] = True
            stack[v] = True

            # Recur for all neighbours
            # if any neighbour is visited and in
            # recStack then graph is cyclic
            for neighbour in self.graph[v]:
                if not visited[neighbour]:
                    if isCyclic(neighbour, visited, stack):
                        return True
                elif stack[neighbour]:
                    return True

            # The node needs to be poped from
            # recursion stack before function ends
            stack[v] = False
            return False

        # Returns true if graph is cyclic else false
        visited = [False] * self.numOfVertices
        myStack = [False] * self.numOfVertices
        for node in range(self.numOfVertices):
            if not visited[node]:
                if isCyclic(node, visited, myStack):
                    return True
        return False

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
        edges.append((int(inp[0]), int(inp[1])))

    myGraph = Graph(n)
    for (a, b) in edges:
        myGraph.importEdge(a-1, b-1)

    print(myGraph.printGraph())
    print(myGraph.toposort())
    print(myGraph.hasCycle())