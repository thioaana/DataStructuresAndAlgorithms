#Uses python3

import sys

def dfs(adj, visited, order, x):
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            dfs(adj, visited, order, i)
            order.append(i)

def toposort(adj):
    order = []
    visited = len(adj) * [False]
    for v in range(len(adj)):
        if not visited[v]:
            dfs(adj, visited, order, v)
            order.append(v)
    order.reverse()
    return order

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

    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

