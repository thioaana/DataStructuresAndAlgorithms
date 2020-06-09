# python3
# n, m = map(int, input().split())
# clauses = [ list(map(int, input().split())) for i in range(m) ]

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable():
    for mask in range(1<<n):
        result = [ (mask >> i) & 1 for i in range(n) ]
        formulaIsSatisfied = True
        for clause in clauses:
            clauseIsSatisfied = False
            if result[abs(clause[0]) - 1] == (clause[0] < 0):
                clauseIsSatisfied = True
            if result[abs(clause[1]) - 1] == (clause[1] < 0):
                clauseIsSatisfied = True
            if not clauseIsSatisfied:
                formulaIsSatisfied = False
                break
        if formulaIsSatisfied:
            return result
    return None

def ReadInput() :
    n, m = map(int, input().split())
    clauses = [list(map(int, input().split())) for i in range(m)]
    return (n, m, clauses)

def CreateGraph(n, m, clauses) :
    # Initialize 1-based edges
    edges = [[] for i in range(2 * n + 2)]

    # For each clause create 2 implication edges
    for cl in clauses :
        edges[Vertex(-cl[0])].append(Vertex(cl[1]))
        edges[Vertex(-cl[1])].append(Vertex(cl[0]))
    return edges

def Vertex(x):
    if x < 0 :
        return n + (-x)
    else :
        return x

(n, m, clauses) = ReadInput()
myEdges = CreateGraph(n, m, clauses)

result = isSatisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE");
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))

