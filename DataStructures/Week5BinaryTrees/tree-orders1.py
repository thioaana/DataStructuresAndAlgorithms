# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node :
    def __init__(self, k, l, r):
        self.key = k
        self.left = l
        self.right = r
        # self.parent = -1

    def SetParent(self, p) :
        self.parent = p

class TreeOrders:
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(0, 0, 0) for i in range(self.n)]

        for i in range(self.n):
            [k, l, r] = map(int, sys.stdin.readline().split())
            self.nodes[i] = Node(k, l, r)
            if l != -1: self.nodes[l].SetParent(i)
            if r != -1: self.nodes[r].SetParent(i)
        self.nodes[0].SetParent(-1)
        for i in range(self.n):
            if self.left[i] != -1: self.nodes[l].SetParent(i)
            if r != -1: self.nodes[r].SetParent(i)


    # def read(self):
    #     self.n = int(sys.stdin.readline())
    #     self.key = [0 for i in range(self.n)]
    #     self.left = [0 for i in range(self.n)]
    #     self.right = [0 for i in range(self.n)]
    #     for i in range(self.n):
    #         [a, b, c] = map(int, sys.stdin.readline().split())
    #         self.key[i] = a
    #         self.left[i] = b
    #         self.right[i] = c

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def Find(self, k, node):
        if self.key[node] == k :
            return node
        elif self.key[node] > k :
            if self.left[node] != -1 :
                return Find(k, self.left[node])
            else :
                return node
        else :
            if self.right[node] != -1:
                return Find(k, self.right[node])
            else :
                return node

    def Next(self, node):
        if self.right[node] != -1 :
            return LeftDescedant(self.right[node])
        else :
            return RightAncestor(node)

    def LeftDescendant(self, node):
        if self.left[node] == -1 :
            return node
        else :
            return LeftDescendant(self.left[node])

    def RightAncestor(self, node):
        if self.key[node] < self.key[self.parent[node]] :
            return self.parent[node]
        else :
            return RightAncestor(self.parent[node])


def main():
    n = int(sys.stdin.readline())
    tree = TreeOrders(n)
    # tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
