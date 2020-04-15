#Uses python3

import sys

def acyclic(adj):
    def Explore(a, flag):
        visited[a] = True
        visited2[a] = True
        for i in adj[a]:
            if not visited2[i] :
                if not visited[i] and flag[0]:
                    Explore(i, flag)
            else :
                 flag[0] = False


        # if adj[a] == [] :
        #     for vertexIndex in range(len(adj)):  # delete all the edges from the Graph that ends to A
        #         if a in adj[vertexIndex]:
        #             adj[vertexIndex].remove(a)
        #     sinksList.append(a)


    # def ExploreAndDelSink(a):
    #     visited[a] = True
    #     if len(adj[a]) > 0 :    # a is not a Sink
    #         for i in adj[a]:
    #             if not visited[i]:
    #                 ExploreAndDelSink(i)
    #     else :                  # a IS a Sink
    #         for vertexIndex in range(len(adj)):  # delete all the edges from the Graph that ends to A
    #             if a in adj[vertexIndex]:
    #                 adj[vertexIndex].remove(a)
    #         sinksList.append(a)

    # def ExploreAndDelSink(adj, a):
    #     visited[a] = True
    #     if len(adj[a]) > 0 :    # a is not a Sink
    #         for i in adj[a]:
    #             if not visited[i]:
    #                 ExploreAndDelSink(adj, i)
    #     else :                  # a IS a Sink
    #         for vertexIndex in range(len(adj)):  # delete all the edges from the Graph that ends to A
    #             if a in adj[vertexIndex]:
    #                 adj[vertexIndex].remove(a)
    #         # del adj[a]  # delete vertex A.

    visited = len(adj) * [False]
    acyclicFlag = [True]
    for v in range(len(adj)):
        if not visited[v] and acyclicFlag[0]:
            visited2 = len(adj) * [False]
            Explore(v, acyclicFlag)


    if acyclicFlag[0] :
        return 0 # Acyclic Graph
    else :
        return 1 # Cycle Graph

if __name__ == '__main__':

    # if m > 0:
    #     for (a, b) in edges:
    #         adj[a - 1].append(b - 1)
    #         adj[b - 1].append(a - 1)
    #     print(reach(adj, x, y))
    # else:
    #     print(0)

    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    edges = []
    for i in range(m):
        inp = input().split()
        edges.append((int(inp[0]), int(inp[1])))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

