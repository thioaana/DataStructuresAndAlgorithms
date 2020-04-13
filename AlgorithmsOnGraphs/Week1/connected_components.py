#Uses python3

import sys

def number_of_components(adj):
    def Explore(a) :
        visited[a] = True
        for i in adj[a] :
            if not visited[i] :
                Explore(i)

    visited = len(adj) * [False]
    cc = 0
    for v in range(len(adj)) :
        if not visited[v] :
            Explore(v)
            cc += 1

    return cc

if __name__ == '__main__':
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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))