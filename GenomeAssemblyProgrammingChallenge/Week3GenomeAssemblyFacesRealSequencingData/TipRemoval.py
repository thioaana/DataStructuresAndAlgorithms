# uses python3

import sys

def getData():
    r = sys.stdin.read().splitlines()
    return 15, r
    # The code below is for temporary use.
    # r = []
    # while True:
    #     read = input()
    #     if read != "":
    #         r.append(read)
    #     else:
    #         break
    # return 3, r

def getDBGraph(k, rs):
    lenRead = len(rs[0])

    # dictIndToValue : Mapping from indexVertex to valueVertex
    # dictValueToInd : Mapping from valueVertex to indexVertex
    dictIndToValue = {}  # Initialize
    dictValueToInd = {}
    # gr :  De Bruijn Graph
    # degrees :  [inDegree, outDegree] for each Vertex
    gr = []
    degr = []
    counter = 0
    for i in range(len(rs)):
        for j in range(lenRead - (k - 1)):
            prefix = rs[i][j:j + (k - 1)]
            suffix = rs[i][j + 1: j + 1 + (k - 1)]

            if prefix not in dictValueToInd:
                dictValueToInd[prefix] = counter
                dictIndToValue[counter] = prefix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if suffix not in dictValueToInd:
                dictValueToInd[suffix] = counter
                dictIndToValue[counter] = suffix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if dictValueToInd[suffix] not in gr[dictValueToInd[prefix]]:
                gr[dictValueToInd[prefix]].append(dictValueToInd[suffix])
                degr[dictValueToInd[prefix]][1] += 1
                degr[dictValueToInd[suffix]][0] += 1
    return gr, degr, dictValueToInd, dictIndToValue

def getReverseDBGraph(k, rs):
    lenRead = len(rs[0])

    # dictIndToValue : Mapping from indexVertex to valueVertex
    # dictValueToInd : Mapping from valueVertex to indexVertex
    dictIndToValue = {}  # Initialize
    dictValueToInd = {}
    # gr :  De Bruijn Graph
    # degrees :  [inDegree, outDegree] for each Vertex
    gr = []
    degr = []
    counter = 0
    for i in range(len(rs)):
        for j in range(lenRead - (k - 1)):
            prefix = rs[i][j:j + (k - 1)]
            suffix = rs[i][j + 1: j + 1 + (k - 1)]

            if prefix not in dictValueToInd:
                dictValueToInd[prefix] = counter
                dictIndToValue[counter] = prefix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if suffix not in dictValueToInd:
                dictValueToInd[suffix] = counter
                dictIndToValue[counter] = suffix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            #Reverse
            if dictValueToInd[prefix] not in gr[dictValueToInd[suffix]]:
                gr[dictValueToInd[suffix]].append(dictValueToInd[prefix])
                degr[dictValueToInd[suffix]][1] += 1
                degr[dictValueToInd[prefix]][0] += 1
    return gr, degr, dictValueToInd, dictIndToValue

def getNodesNoInDegree(graph, degrees) :
    noIn = []
    for u in range(len(graph)):
        if degrees[u][0] == 0 :
            noIn.append(u)
    return noIn

if __name__ == "__main__":
    k, reads = getData()
    numOfReads = len(reads)
    lengthOfRead = len(reads[0])

    # Create two graphs. a)De Bruijn graph bb)De Bruijn Reverse graph
    graph, degrees, dVtoI, dItoV = getDBGraph(k, reads)


    # Find nodes with zero in-degree on (a) graph
    noInDegree = getNodesNoInDegree(graph, degrees)

    tipEdgesCounter = 0
    # For each node u (= noInDegree.pop()) in noInDegree perform :
    # - Increase Counter with len(u)
    # - For each adjacent node v, if v has in-degree = 1 (meaning from u), add v in noInDegree.
    # - Cut the edges going out of u (no need)
    # - Cut u from graph (no need).

    for mode in range(2):
        if mode == 0:
            # Create De Bruijn graph
            graph, degrees, dVtoI, dItoV = getDBGraph(k, reads)
        else :
            # Create De Bruijn Reverse graph
            graph, degrees, dVtoI, dItoV = getReverseDBGraph(k, reads)

        # Find nodes with zero in-degree on (a) graph
        noInDegree = getNodesNoInDegree(graph, degrees)

        while noInDegree :
            u = noInDegree.pop()
            tipEdgesCounter += len(graph[u])
            for v in graph[u]:
                if degrees[v][0] > 1 : continue
                noInDegree.append(v)
    print(tipEdgesCounter)

