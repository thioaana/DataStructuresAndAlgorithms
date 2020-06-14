#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.D = sys.maxsize

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

def FunParty(tree, vertex, parent) :
    if len(tree[vertex].children) == 1 and parent != -1:
        tree[vertex].D = tree[vertex].weight
    else :
        m1 = tree[vertex].weight
        for u in tree[vertex].children : # For all children
            if u != parent :
                for v in tree[u].children:   # For all grand children
                    if v != vertex :
                        m1 = m1 + tree[v].D
        m0 = 0
        for u in tree[vertex].children:  # For all children
            if u != parent:
                m0 = m0 + tree[u].D
        tree[vertex].D = max(m0, m1)

def dfs(tree, vertex, parent):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex)
        # else :
    FunParty(tree, vertex, parent)

def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    dfs(tree, 0, -1)
    return tree[0].D

def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
