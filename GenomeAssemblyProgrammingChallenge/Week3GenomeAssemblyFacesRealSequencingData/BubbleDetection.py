# uses python3

import sys

def getData():
    lines = sys.stdin.read().splitlines()
    [k, t] = [int(i) for i in lines[0].split()]
    r = lines[1:]
    return k, t, r
    # The code below is for temporary use.
    # [k, t] = [int(i) for i in input().split()]
    # r = []
    # while True:
    #     read = input()
    #     if read != "":
    #         r.append(read)
    #     else:
    #         break
    # return k, t, r

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

def isBubble(path1, path2):
    for v in path1[1:-1]:
        if v in path2: return False
    return True

def getCandidatesV(gr, v, cands, degs, t, path, visited):
    visited[v] = True
    path.append(v)
    selfLoops = gr[v].count(v)
    if degs[v][0] > (1 + selfLoops):
        if v not in cands : cands.append(v)
    for i in gr[v]:
        if len(path) <= t:
            if v == i : continue
            if visited[i] == False:
                getCandidatesV(gr, i, cands, degs, t, path, visited)
    path.pop()
    visited[v] = False
    if not path: return cands

# The function to do DFS traversal.
def getPaths(gr, v, cand, visited, path, fullPaths, t):
    visited[v] = True
    path.append(v)
    if v == cand:
        fullPaths.append(path[:])
    for i in gr[v]:
        if len(path) <= t:
            if v == i : continue
            if visited[i] == False:
                getPaths(gr, i, cand, visited, path, fullPaths, t)
    path.pop()
    visited[v] = False
    if not path: return fullPaths

def getBubbles(gr, candidates, t):
    paths = {}
    numBubbles = 0
    # For each pair u (from start), w (from end) get all paths
    for u in candidates:
        for w in candidates[u]:
            if u == w: continue
            paths[u] = getPaths(gr, u, w, [False] * len(gr), [], [], t)
            for indPath1 in range(len(paths[u])):
                for indPath2 in range(indPath1 + 1, len(paths[u])):
                    if indPath1 == indPath2: continue
                    if isBubble(paths[u][indPath1], paths[u][indPath2]): numBubbles += 1
    print(numBubbles)

if __name__ == "__main__":
    k, t, reads = getData()
    lengthOfRead = len(reads[0])

    # Create De Bruijn graph
    graph, degrees, dVtoI, dItoV = getDBGraph(k, reads)

    # For each node u with out-degree >1 (without selfloops) run DFS
    # and find all the nodes v with distance (edge) <= t and in-degree >1
    # Save in dictionary candidates
    candidates={}
    for u in range(len(graph)):
        selfLoops = graph[u].count(u)
        if degrees[u][1] > (1 + selfLoops):
            candidates[u] = getCandidatesV(graph, u, [], degrees, t, [], [False]*len(graph))

    # 1. For each pair u v run DFS and find all the paths that connect them with distance <= t
    #    Save then in dictionary paths
    # 2. For each pair of paths check if there is a bubble.
    getBubbles(graph, candidates, t)
