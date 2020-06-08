# python3

import os
import itertools

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m) ]

finalEdges = [[] for _ in range(n + 1)]
for e in edges :
    finalEdges[e[0]].append(e[1])

colors = [1, 2, 3]
clauses = []

def varnum(v, c) :
    return v + n * (c - 1)

def ExactlyOneOf(literals) :
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def OnlyNegations(literals):
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():

    # Each Vertex contains exactly one Color
    for v in range(1, n + 1) :
        ExactlyOneOf([varnum(v, c) for c in colors])

    # Adjacent Vertices cannot have the same Color
    for edgeIndex in range(1, len(finalEdges)) :
        if len(finalEdges[edgeIndex]) == 0 :
            continue
        for e in finalEdges[edgeIndex]:
            for c in colors :
                literals = [varnum(edgeIndex, c)]
                literals.append(varnum(e, c))
                OnlyNegations(literals)

    # Print Header - number of Clauses and Variables
    print(" ".join(map(str, [len(clauses), n * 3])))
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
    os.system("minisat tmp.cnf")
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
                    for c in colors:
                        if [v, c] in assignment :
                            print(c, end = "")
                            break

printEquisatisfiableSatFormula()
# Testing()
