import BST

class Node(BST.Node) :
    def __init__(self, key, value):
        BST.Node.__init__(self, key, value)

class Tree(BST.Tree):
    def __init__(self):
        BST.Tree.__init__(self)

    # Helper function to find the Hight of a node, used in balancing the Balanced BST
    def _getNodeHeight(self,  n):
        if n is None : return 0
        if n.getLeft() is None and n.getRight() is None :
            return 1
        else :
            return 1 + max(self._getNodeHeight(n.getLeft()), self._getNodeHeight(n.getRight()))

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
            self._AdjustHeight(parent)
            self._Rebalance(parent)

    def _AdjustHeight(self, n) :
        leftBranch = n.getLeft()
        rightBranch = n.getRight()
        if leftBranch and rightBranch :
            n.setHeight(1 + max(leftBranch.getHeight(), rightBranch.getHeight()))
        elif leftBranch is None and rightBranch :
            n.setHeight(1 + rightBranch.getHeight())
        elif leftBranch  and rightBranch is None:
            n.setHeight(1 + leftBranch.getHeight())
        else :
            n.setHeight(1)

    def _RebalanceRight(self, n):
        m = n.getLeft()
        if self._getNodeHeight(m.getRight()) > self._getNodeHeight(m.getLeft()) :
            self._RotateLeft(m)
        self._RotateRight(n)

    def _RebalanceLeft(self, n):
        m = n.getRight()
        if self._getNodeHeight(m.getLeft()) > self._getNodeHeight(m.getRight()) :
            self._RotateRight(m)
        self._RotateLeft(n)

    def _RotateRight(self, n):
        # Saves in memory
        nParent = n.getParent()
        y = n.getLeft()
        yRight = y.getRight()
        # Rotate
        y.setRight(n)
        n.setLeft(yRight)
        # Define new parents
        if n.getLeft()  : n.getLeft().setParent(n)
        if n.getParent(): y.setParent(n.getParent())
        n.setParent(y)
        if nParent :
            if nParent.getLeft() == n :
                nParent.setLeft(y)
            else :
                nParent.setRight(y)
        else :
            self.root = y
        # Update heights
        self._AdjustHeight(n)
        self._AdjustHeight(y)
        if nParent : self._AdjustHeight(nParent)

    def _RotateLeft(self, n):
        # Saves in memory
        nParent = n.getParent()
        y = n.getRight()
        yLeft = y.getLeft()
        # Rotate
        y.setLeft(n)
        n.setRight(yLeft)
        # Define new parents
        if n.getRight()  : n.getRight().setParent(n)
        if n.getParent() : y.setParent(n.getParent())
        n.setParent(y)
        if nParent :
            if nParent.getLeft() == n:
                nParent.setLeft(y)
            else:
                nParent.setRight(y)
        else :
            self.root = y
        # Update heights
        self._AdjustHeight(n)
        self._AdjustHeight(y)
        if nParent : self._AdjustHeight(nParent)

    # Input : Key of the node to be deleted
    # Output: True if the node is found in the Tree and deleted
    #         False if the node is not found in the Tree
    def insert(self, k, v):
        BST.Tree.insert(self, k, v)
        found, newNode = self._Find(self.root, k)
        if found :
            self._Rebalance(newNode)

    def delete(self, key):
        (deleted, parent) = BST.Tree.delete(self, key)
        if deleted :
            self._Rebalance(parent)

if __name__ == "__main__" :
    myTree = Tree()
    # keys = [13, 10, 15, 5, 11, 16, 4, 6] # insert(7, 7)
    # keys = [30, 5, 35, 32, 40]
    # keys = [5, 2, 7, 1, 4, 6, 9, 3, 16] #insert(15, 15)
    keys = [44, 17, 62, 32, 50, 78, 48, 54, 88] # delete(15, 15)
    for k in keys:
        myTree.insert(k, k)
    myTree.insert(15, 15)
    print(5)