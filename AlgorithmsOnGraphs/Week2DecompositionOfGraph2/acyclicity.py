#Uses python3

import sys

def acyclic(adj):
    def isCyclic(v, visited, stack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        stack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for i in adj[v]:
            if not visited[i] :
                if isCyclic(i, visited, stack) :
                    return True
            elif stack[i] :
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        stack[v] = False
        return False

    # Returns true if graph is cyclic else false
    visited = [False] * len(adj)
    myStack = [False] * len(adj)
    for v in range(len(adj)) :
        if not visited[v] :
            if isCyclic(v, visited, myStack) :
                return 1
    return 0


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
    print(acyclic(adj))

