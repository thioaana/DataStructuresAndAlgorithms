#uses python3

import sys

def getData(numOfReads) :
    r = []
    for i in range(numOfReads) :
        r.append(input())
    return r

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

#    Conditions of a graph to have Euler Path
#    1. There is no Euler Path if the number of edges is odd.
#    2. There is an Euler Path if (a) or (b) is satisfied
#    (a) If all vertices have same out-degrees as in-degrees or
#    (b) If all but 2 vertices have same out-degree as in-degree,
#      and one of those 2 vertices has out-degree with one greater than its in-degree,
#      and the other has in-degree with one greater than its out-degree.
#      Otherwise no Euler Path exists.
def checkEulerPath(gr, deg):
    # Check Condition 1
    # edgesCounter = 0
    # for v in gr : edgesCounter += len(v)
    # if edgesCounter % 2 >0 : return False

    # Check Condition 2
    notEqualInOutVertices = []
    for v in deg :
        if v[0] != v[1] : return False
    #     if v[0] == v[1] : continue # No problem
    #     if abs(v[0] - v[1]) >1 : return False # |in-out| > 1, meaning no Euler Path
    #     notEqualInOutVertices.append(v[0] - v[1])
    #     if len(notEqualInOutVertices) > 2 : return False # More than 2 vertices have |in-out| =1, meaning no Euler Path
    # # if len(notEqualInOutVertices) == 1 : return False # Onl
    # # At this point all vertices but 2 have in = out
    # if len(notEqualInOutVertices) > 0 :
    #     if notEqualInOutVertices[0] * notEqualInOutVertices[1] > 0 : return False
    return True

if __name__ == "__main__" :
    reads = getData(5)
    lengthOfRead = len(reads[0])
    print(40)
    # for k in range(lengthOfRead - 1,2, -1) :
    #     graph, degrees = getDBGraph(k, reads)
    #     result = checkEulerPath(graph, degrees)
    #     if result : print(k)