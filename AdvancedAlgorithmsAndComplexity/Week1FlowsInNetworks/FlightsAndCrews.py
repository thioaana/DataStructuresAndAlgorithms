#Uses python3

def bipartiteMatch(graph):
    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break

    while 1:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = dict([(u, unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)

        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v, []).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)

        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching, list(pred), list(unlayered))

        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)

inp = input().split()
flights = int(inp[0])
crews = int(inp[1])
bpGraph = {}
for i in range(1, flights + 1):
    cr = []
    inp = [int(x) for x in input().split()]
    for j in range(len(inp)) :
        if inp[j] == 1 :
            cr.append(j + 1)
    bpGraph[i] = cr
    # for j in range(len(inp)) :
    #     bpGraph.append(inp)
# print(bipartiteMatch({1:[3, 4], 2:[3]}))
# print(bipartiteMatch({1:[1, 2, 4], 2:[2], 3:[]}))
# print(bipartiteMatch({1:[1, 2], 2:[1]}))
res1 = bipartiteMatch(bpGraph)[0]
# print(result)
listRes1 = [(res1[t], t) for t in res1]
i = 0; res2 = {}
for i in range(1, flights + 1):
    res2[i] = -1

i = 0
for i in listRes1:
    res2[i[0]] = i[1]
listRes2 = [(k, v) for k, v in res2.items()]
listRes2.sort()
listRes3 = [str(t[1]) for t in listRes2]
print(" ".join(listRes3))
