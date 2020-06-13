# python3
import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

# Reads Input Data
# n : Number of Variables
# m : Number of Clauses
# m lines with clauses. Each clause contains 2 literals (2-CNF)
def readInput() :
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split())) for i in range(m)]
    return (n, m, clauses)

# Creates the implication graph with 2*n vertices (x and not x) and 2*m edges
def createGraph(n, m, clauses) :
    # Initialize 1-based vertices. 1 to n (0 to n+1)
    edges = [[] for i in range(2 * n + 1)]

    # For each clause create 2 implication edges
    for cl in clauses :
        edges[VerPosToNeg(-cl[0], n)].append(VerPosToNeg(cl[1], n))
        edges[VerPosToNeg(-cl[1], n)].append(VerPosToNeg(cl[0], n))
    return edges

# Vertex x is edges[x]
# Vertex not x (input as -x) is edge[n+(-x)]
def VerPosToNeg(x, n):
    if x < 0 :
        return n + (-x)
    else :
        return x
# Get list of sub-lists.
# Each sub-list contains the vertices are SCC
def findSCCs(numV, graph):
    def fillOrder(v, visited, gr, stack):
        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in gr[v]:
            if visited[i] == False:
                fillOrder(i, visited, gr, stack)
        stack = stack.append(v)

    # Function that returns reverse (or transpose) of this graph
    def getReversedGraph(gr):
        edges = [[] for i in range(len(gr))]

        # For each clause create 2 implication edges
        for u in range(1, len(gr)):
            for v in gr[u]:
                edges[v].append(u)
        return edges

    def DFSUtil(v, visited, nScc, scc, gr):
        # Mark the current node as visited and print it
        visited[v] = True

        # Append SCC with v
        sccs[numSccs].append(v)
        # print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for i in gr[v]:
            if visited[i] == False:
                DFSUtil(i, visited, nScc, scc, gr)

    sccs=[]
    numSccs = 0
    stack = []

    # Mark all the vertices as not visited (For first DFS)
    visited = [False] * (numV + 1)

    # Fill vertices in stack according to their finishing times
    for i in range(1, numV + 1):
        if visited[i] == False:
            fillOrder(i, visited, graph, stack)

    # Create a reversed graph
    reversedGraph = getReversedGraph(graph)

    # Mark all the vertices as not visited (For second DFS)
    visited = [False] * (numV + 1)

    # Now process all vertices in order defined by Stack
    while stack:
        i = stack.pop()
        if visited[i] == False:
            sccs.append([])
            DFSUtil(i, visited, numSccs, sccs, reversedGraph)
            numSccs += 1
    return sccs

def createVertexIndex(gr, sccs) :
    d = {}
    for indScc in range(len(sccs)):
        for v in sccs[indScc]:
            d[v] = [indScc]
    return d

def getSatisfuction(numV, indScc):
    for v in range(1, numV + 1) :
        if indScc[v][0] == indScc[numV + v][0] :
            return False
    return True

def computeSolution(n, indScc, Sccs) :
    for scc in range(len(Sccs)-1, -1, -1) :
        for v in Sccs[scc]:
            if len(indScc[v]) == 1 :
                indScc[v].append(1)
                if v <= n : indScc[n + v].append(0)
                else :      indScc[v - n].append(0)

def printSolution(numV, indScc) :
    result = []
    for i in range(1, numV + 1):
        if indScc[i][1] > 0 :result.append(i)
        else : result.append(-i)
    print("SATISFIABLE")
    print(" ".join(str(i) for i in result))

def main():
    (numVertices, numClauses, clauses) = readInput()
    graph = createGraph(numVertices, numClauses, clauses)
    # graph=[[], [], [1], [2, 1], [3, 1], [2, 3]] # For checking SCCs
    # graph=[[], [2, 4], [3], [1], [5], []] # For checking SCCs
    # graph=[[], [2], [3], [1], [], []] # For checking SCCs
    # SCCs = findSCCs(5, graph) #For checking SCCs
    SCCs = findSCCs(2 * numVertices, graph)
    indexSCC = createVertexIndex(graph, SCCs)
    isSat = getSatisfuction(numVertices, indexSCC)
    if not isSat :
        print("UNSATISFIABLE")
        sys.exit()

    computeSolution(numVertices, indexSCC, SCCs)
    printSolution(numVertices, indexSCC)

# This is to avoid stack overflow issues
threading.Thread(target=main).start()