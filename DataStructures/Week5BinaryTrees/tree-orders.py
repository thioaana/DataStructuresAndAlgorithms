# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.parent = [0 for i in range(self.n)]
        for i in range(self.n):
            [k, l, r] = map(int, sys.stdin.readline().split())
            self.key[i] = k
            self.left[i] = l
            self.right[i] = r
            if self.left[i] != -1  : self.parent[self.left[i]] = i
            if self.right[i] != -1 : self.parent[self.right[i]] = i
        self.parent[0] = -1
        # self.result = []

    def inOrder(self, node):
        if node != -1 :
            self.inOrder(self.left[node])
            print(self.key[node], end=" ")
            self.inOrder(self.right[node])

    def preOrder(self, node):
        if node != -1 :
            print(self.key[node], end=" ")
            self.preOrder(self.left[node])
            self.preOrder(self.right[node])

    def postOrder(self, node):
        if node != -1 :
            self.postOrder(self.left[node])
            self.postOrder(self.right[node])
            print(self.key[node], end=" ")

    def Find(self, k, node):
        if self.key[node] == k :
            return node
        elif self.key[node] > k :
            if self.left[node] != -1 :
                return self.Find(k, self.left[node])
            else :
                return node
        else :
            if self.right[node] != -1:
                return self.Find(k, self.right[node])
            else :
                return node

    def Next(self, node):
        if self.right[node] != -1 :
            return self.LeftDescendant(self.right[node])
        else :
            return self.RightAncestor(node)

    def LeftDescendant(self, node):
        if self.left[node] == -1 :
            return node
        else :
            return self.LeftDescendant(self.left[node])

    def RightAncestor(self, node):
        if self.key[node] < self.key[self.parent[node]] :
            return self.parent[node]
        else :
            return self.RightAncestor(self.parent[node])

def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0);print()
    tree.preOrder(0);print()
    tree.postOrder(0)

threading.Thread(target=main).start()
