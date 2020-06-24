#uses python3

import sys

def getData() :
    # lines = sys.stdin.read().splitlines()
    # [k, t] = [int(i) for i in lines[0].split()]
    # r = lines[1:]
    [k, t] = [int(i) for i in input().split()]
    r = []
    while True :
        read = input()
        if read != "":
            r.append(read)
        else:
            break
    return k, t, r

def getDBGraph(k, rs) :
    lenRead = len(rs[0])

    # dictIndToValue : Mapping from indexVertex to valueVertex
    # dictValueToInd : Mapping from valueVertex to indexVertex
    dictIndToValue = {} # Initialize
    dictValueToInd = {}
    # gr :  De Bruijn Graph
    # degrees :  [inDegree, outDegree] for each Vertex
    gr = []
    degr=[]
    counter = 0
    for i in range(len(rs)) :
        for j in range(lenRead - (k - 1)) :
            prefix = rs[i][j:j + (k-1)]
            suffix = rs[i][j + 1: j + 1 + (k - 1)]

            if prefix not in dictValueToInd :
                dictValueToInd[prefix] = counter
                dictIndToValue[counter] = prefix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if suffix not in dictValueToInd :
                dictValueToInd[suffix] = counter
                dictIndToValue[counter] = suffix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if dictValueToInd[suffix] not in gr[dictValueToInd[prefix]] :
                gr[dictValueToInd[prefix]].append(dictValueToInd[suffix])
                degr[dictValueToInd[prefix]][0] += 1
                degr[dictValueToInd[suffix]][1] += 1
    return gr, degr

def getBubbles(gr, degs) :
    for i in range(len(gr)) :
        selfLoops = gr[i].count(i)
        if degs[1] <= 1 + selfLoops : continue
        

if __name__ == "__main__" :
    k, t, reads = getData()
    lengthOfRead = len(reads[0])
    graph, degrees = getDBGraph(k, reads)
    getBubbles(graph, degrees)
