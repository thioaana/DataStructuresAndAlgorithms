#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):

    def myUtility(node, lower, upper):
        if node == -1:
            return True

        if not myUtility(tree[node][1], lower, tree[node][0]):
            return False

        if tree[node][0] < lower or tree[node][0] >= upper:
            return False

        if not myUtility(tree[node][2], tree[node][0], upper):
            return False

        return True

    if len(tree) == 0 :
        result = True
    else :
        result = myUtility(0, (sys.maxsize * 2 + 1) * (-1), sys.maxsize * 2 + 1)
    return result

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()