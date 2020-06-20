# uses python3

import sys
import copy
from itertools import permutations

def createEdges(k, str, e):
    if len(str) == k :
        e.append(str)
        return
    for digit in "01":
        createEdges(k, str + digit, e)

def getDBGraph(e) :
    k = len(e[0])

    # dictIndToValue : Mapping from indexVertex to valueVertex
    # dictValueToInd : Mapping from valueVertex to indexVertex
    dictIndToValue = {i:[] for i in range(2**(k -1))} # Initialize
    dictValueToInd = {}
    # gr :  De Bruijn Graph
    gr = [[] for i in range(2**(k - 1))]
    counter = 0
    for i in range(len(e)) :
        prefix = e[i][:k-1]
        suffix = e[i][1:]

        if prefix not in dictValueToInd :
            dictValueToInd[prefix] = counter
            dictIndToValue[counter] = prefix
            counter += 1
        if suffix not in dictValueToInd :
            dictValueToInd[suffix] = counter
            dictIndToValue[counter] = suffix
            counter += 1
        gr[dictValueToInd[prefix]].append(dictValueToInd[suffix])
    return gr, dictIndToValue, dictValueToInd

def getEulerianPath(gr):
    # gr = copy.deepcopy(gr1)
    stack = []
    circuit = []
    current = 0 # Initial Node
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
    k = int(input())
    edges = []
    createEdges(k, "", edges)
    graph, mapIndToValue, mapValueToInd = getDBGraph(edges)
    path = getEulerianPath(copy.deepcopy(graph))
    universal = mapIndToValue[path[0]]
    for i in range(1, len(path)):
        universal += mapIndToValue[path[i]][-1]
    # print(path)
    print(universal)