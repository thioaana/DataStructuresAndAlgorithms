# uses python3

import sys
import copy
from itertools import permutations

def getData() :
    r = []
    for i in range(5396) :
        r.append(input())
    return r

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
    dictIndToValue = {} # i:[] for i in range(2**(k -1))} # Initialize
    dictValueToInd = {}
    # gr :  De Bruijn Graph
    gr = []# for i in range(2**(k - 1))]
    counter = 0
    for i in range(len(e)) :
        prefix = e[i][:k-1]
        suffix = e[i][1:]

        if prefix not in dictValueToInd :
            dictValueToInd[prefix] = counter
            dictIndToValue[counter] = prefix
            gr.append([])
            counter += 1
        if suffix not in dictValueToInd :
            dictValueToInd[suffix] = counter
            dictIndToValue[counter] = suffix
            gr.append([])
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

def getCommonSP(r, stK,stL, exLap) :
    # Find common substring
    # From suffix of g and prefix of l
    m = min(len(stK), len(stL))
    c1 = m
    while c1 > 0 :
        if c1 <= exLap : return 0
        if stL[:c1] == stK[-c1:] : break
        c1 -= 1
    return c1

if __name__ == "__main__" :
    reads = getData()
    k = len(reads[0])
    numReads = len(reads)

    path = getEulerianPath(copy.deepcopy(graph))
    universal = mapIndToValue[path[0]]
    for i in range(1, len(path)):# - (k-1)): An alternative, without the last 2 lines
        universal += mapIndToValue[path[i]][-1]

    cPS = getCommonSP(reads, mapIndToValue[path[len(path) - 1]], universal, 0)
    universal = universal[:-cPS]

    print(universal)