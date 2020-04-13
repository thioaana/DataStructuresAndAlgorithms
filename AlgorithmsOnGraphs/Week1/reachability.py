#Uses python3

import sys

def reach(adj, x, y):
    def Explore(a) :
        visited[a] = True
        for i in adj[a] :
            if not visited[i] :
                Explore(i)

    visited = len(adj) * [False]
    Explore(x)
    if visited[y] : return 1
    else : return 0

if __name__ == '__main__':
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    edges = []
    for i in range(m) :
        inp = input().split()
        edges.append((int(inp[0]), int(inp[1])))

    if m > 0 :
        inp = input().split()
        x = int(inp[0])
        y = int(inp[1])
        x, y = x - 1, y - 1
        adj = [[] for _ in range(n)]

        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        print(reach(adj, x, y))
    else : print(0)