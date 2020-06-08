# python3

import os
import itertools
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

finalEdges = [[] for _ in range(n + 1)]
for e in edges :
    finalEdges[e[0]].append(e[1])
    finalEdges[e[1]].append(e[0])

positions = [i for i in range(1, n + 1)]
clauses = []

def varnum(v, p) :
    return (v -1) * n + p

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    # Each node j must appear in the path
    # X(i, 1)vX(i, 2)v...X(i, n) for each node i
    for v in range(1, n + 1) :
        clause = []
        for p in positions :
            clause.append(varnum(v, p))
        clauses.append(clause)

    # No node i appears in path twice
    # -X(i, j)v - X(i, k) for all i, j, k where j != k
    for v in range(1, n + 1) :
        for j in positions :
            for k in positions:
                if  k > j :
                    clauses.append([-varnum(v, j), -varnum(v, k)])

    # No two nodes i & k occupy same position
    # -X(i, j)v - X(k, j) for all i, j, k where i != k
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if v > u :
                for p in positions:
                    clauses.append([-varnum(u, p), -varnum(v, p)])
    # # OLD ALGO
    # # Non adjacent nodes i & j cannot be adjacent in path
    # # -X(j, k)v - X(i, k + 1) for all(i, j) !E G and k = 1, 2, ...n-1
    # for u in range(1, n + 1):
    #     for v in range(1, n + 1):
    #         if u == v: continue
    #         if v in finalEdges[u] : continue
    #         for p in range(1, len(positions)):
    #             clauses.append([-varnum(u, p), -varnum(v, p + 1)])

    # REPLACED WITH THIS ALGO
    # For every vertex i. For every vertex j connected with i. Fo every ever n-1 positions.
    # -X(i,n) v X(j1,n+1) ....... X(jm, n+1) for all (i = 1..k, n = 1..k-1)
    for u in range(1, n + 1):
        for p in range(1, len(positions)): # Meaning 1 -> Positions -1
            clause = [-varnum(u, p)]
            for v in finalEdges[u] :
                clause.append(varnum(v, p + 1)) # That's why p is running up Positions -1
            clauses.append(clause)

    # Print Header - number of Clauses and Variables
    print(" ".join(map(str, [len(clauses), n * n])))
    # Print Clauses with 0 in the end of each clause
    for cl in clauses :
        cl.append(0)
        print(" ".join(map(str, cl)))

def Testing():
    with open("tmp.cnf", "w") as f :
        f.write("p cnf {} {}\n".format(n * 3, len(clauses)))
        for cl in clauses :
            f.write(" ".join(map(str, cl)) + "\n")
    f.close()
    os.system("minisat tmp.cnf tmp.sat")

    with open("tmp.sat", "r") as satfile:
        for line in satfile :
            if line.split()[0] == "UNSAT" :
                print("There is no solution")
            elif line.split()[0] == "SAT" :
                pass
            else :
                assignment = [int(x) for x in line.split()]
                for v in range(1, n + 1):
                    for p in positions:
                        if [v, p] in assignment :
                            print(p, end = "")
                            break


printEquisatisfiableSatFormula()
# Testing()


