# uses python3

import sys


# Check if the graph is not Eulerian ie outDegree != inDegree for every vertex
# In this case print 0 and exit program
def isEulerian(nV, dV):
    for u in range(1, nV + 1):
        if dV[u][0] != dV[u][1] :
            return False
    return True

# 1. Start with an empty stack and an empty circuit (eulerian path).
#    - If all vertices have same out-degrees as in-degrees - choose any of them.
#    - If all but 2 vertices have same out-degree as in-degree, and one of those 2 vertices has out-degree with one greater than its in-degree, and the other has in-degree with one greater than its out-degree - then choose the vertex that has its out-degree with one greater than its in-degree.
#    - Otherwise no euler circuit or path exists.
# 2. If current vertex has no out-going edges (i.e. neighbors) - add it to circuit,
#    remove the last vertex from the stack and set it as the current one.
#    Otherwise (in case it has out-going edges, i.e. neighbors) - add the vertex to the stack,
#    take any of its neighbors, remove the edge between that vertex and selected neighbor,
#    and set that neighbor as the current vertex.
# 3. Repeat step 2 until the current vertex has no more out-going edges (neighbors) and the stack is empty.
def getEulerianPath(gr):
    stack = []
    circuit = []
    current = 1
    while len(gr[current]) > 0 or len(stack) > 0 : # Step 3, repeat until ...
        if len(gr[current]) == 0 :
            circuit.append(current)
            current = stack.pop()
        else :
            stack.append(current)
            neighbor = gr[current].pop(0)
            current = neighbor
    circuit.append(current)
    circuit.reverse()
    return circuit

if __name__ == "__main__" :
    [numV, numE] = [int(i) for i in input().split()]

    # Initialize graph and dictV
    graph = [[]]
    dictV = {}
    for i in range(1, numV + 1) :
        graph.append([])
        dictV[i]=[0, 0] # [outDegree, inDegree]

    # Input edges
    for i in range(numE):
        [u, v] = [int(i) for i in input().split()]
        graph[u].append(v)
        dictV[u][0] += 1
        dictV[v][1] += 1

    if not isEulerian(numV, dictV) :
        print(0)
        sys.exit()

    path = getEulerianPath(graph)
    print(1)
    print(" ".join(str(path[i]) for i in range(len(path)-1)))