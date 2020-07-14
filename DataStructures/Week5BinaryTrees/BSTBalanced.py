import BST

class Node(BST.Node) :
    def __init__(self, key, value):
        BST.Node.__init__(self, key, value)

class Tree(BST.Tree):
    def __init__(self):
        BST.Tree.__init__(self)

    # Helper function to find the Hight of a node, used in balancing the Balanced BST
    def _getNodeHeight(self,  n):
        if n.getLeft() is None and n.getRight() is None :
            return 1
        else :
            return 1 + max(self._nodeHeight(n.getLeft()), self._nodeHeight(n.getRight()))

    def _Rebalance(self, n):
        parent = n.getParent()
        leftBranchHeight  = self._getNodeHeight(n.getLeft())
        rightBranchHeight = self._getNodeHeight(n.getRight())
        if leftBranchHeight > rightBranchHeight + 1 :
            self._RebalanceRight(n)
        if rightBranchHeight > leftBranchHeight + 1 :
            self._RebalanceLeft(n)
        # self.AdjustHeight(n)
        if parent is not None :
            self._Rebalance(parent)

    def _RebalanceRight(self, n):
        m = n.getLeft()
        if self._getNodeHeight(m.getRight()) > self._getNodeHeight(m.getLeft()) :
            self._RotateLeft(m)
        self._RotateRight(n)

    def _RotateRight(self, n):
        return

    # def AdjustHeight(self, n):
    #
    # def _getParent(self, curNode, k):
    #     # Case 1: Searching for the parent of root node. ie parent is None.
    #     if k == self.root.getKey() :
    #         return True, None
    #
    #     parent = curNode
    #     if parent.getLeft().getKey() == k or parent.getRight().getKey() == k :
    #         return True, parent
    #     if curNode.getKey() < k :
    #         if curNode.getRight()  : return self._getParent(curNode.getRight(), k)
    #         else :                   return False, parent
    #     else :
    #         if curNode.getLeft() :   return self._getParent(curNode.getLeft(), k)
    #         else :                   return False, parent

    # Input : Key of the node to be deleted
    # Output: True if the node is found in the Tree and deleted
    #         False if the node is not found in the Tree

    def insert(self, k, v):
        BST.Tree.insert(self, k, v)
        found, newNode = self._Find(self.root, k)
        if found :
            self._Rebalance(newNode)


if __name__ == "__main__" :
    myTree = Tree()

    # keys = [15, 10, 20, 8, 12, 16]
    # for k in keys:
    #     myTree.insert(k, k)
    myTree.insert(22, 1)#AVLInsert(16, 8)
    print(myTree)
    myTree.delete(15)
    myTree.delete(10)
    # myTree.insert(4, 4)
    # myTree.insert(6, 6)
    # myTree.insert(8, 8)
    # myTree.insert(5, 5)
    # myTree.insert(4, 4)
    # myTree.insert(6, 6)
    # myTree.insert(1, 1)
    # myTree.insert(2, 2)
    # myTree.delete(4)
    # myTree.delete(1)
    # myTree.delete(5)
    # myTree.delete(6)
    # myTree.delete(8)
    # myTree.delete(2)
    print(5)