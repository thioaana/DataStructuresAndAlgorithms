#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):

    def myUtility(node, lower, upper):
      if node == -1:
        return True

      if not myUtility(tree[node][1], lower, tree[node][0]):
        return False

      if tree[node][0] <= lower or tree[node][0] >= upper:
        return False


      if not myUtility(tree[node][2], tree[node][0], upper):
        return False

      return True

    h = myUtility(0, sys.maxsize * (-1), sys.maxsize)
    return h


  # def isBSTUtil(root, prev):
  #
  #   # traverse the tree in inorder fashion and
  #   # keep track of prev node
  #   if root != -1 :
  #     if not isBSTUtil(tree[root][1], prev) :
  #       return False
  #
  #     # Allows only distinct valued nodes
  #     if tree[root][0] <= prev:
  #       return False
  #
  #     # Initialize prev to current
  #     prev = tree[root][0]
  #
  #     return isBSTUtil(tree[root][2], prev)
  #
  #   return True
  #
  # return isBSTUtil(0, sys.maxsize * (-1))
  # def inOrder(node, lowerBound, upperBound):
  #   if node != -1 and TF:
  #
  #     inOrder(tree[node][1], lowerBound, tree[node][0])
  #     if TF :
  #       if not (tree[node][0] > lowerBound and tree[node][0] < upperBound) :
  #         TF = False
  #
  #       inOrder(tree[node][2], tree[node][0], upperBound)
  #       if not (tree[node][0] > lowerBound and tree[node][0] < upperBound) :
  #         TF =  False
  #
  # TF= True
  # inOrder(0, sys.maxsize * (-1), sys.maxsize, TF)
  # Implement correct algorithm here


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
