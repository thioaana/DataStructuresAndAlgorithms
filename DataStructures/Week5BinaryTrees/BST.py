class Node :
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1

    def getKey(self):   return self.key
    def getValue(self): return self.value
    def getParent(self):return self.parent
    def getLeft(self):  return self.left
    def getRight(self): return self.right
    def getHeight(self): return self.height
    def setParent(self, n):  self.parent = n
    def setLeft(self, n):  self.left = n
    def setRight(self, n):  self.right = n
    def setKey(self, k): self.key = k
    def setValue(self, v): self.value = v
    def setHeight(self, h): self.height = h

class Tree:
    def __init__(self):
        self.root = None

    # Helper function to find minimum key node in subtree rooted on currNode
    def _getSuccessor(self, currNode):
        while currNode.getLeft() :
            currNode = currNode.getLeft()
        return currNode

    # Input : A node of the Tree and a key
    # Output: True if key exist in the Tree and the node with node.key = key.
    #         False if key does not exist in the Tree and the parent node of the key if the key is going to be inserted in the Tree.
    def _Find(self, curNode, k):
        if curNode.getKey() == k :
            return True, curNode
        if curNode.getKey() < k :
            if curNode.getRight() is not None : return self._Find(curNode.getRight(), k)
            else :                              return False, curNode
        else :
            if curNode.getLeft() is not None :   return self._Find(curNode.getLeft(), k)
            else :                              return False, curNode

    # Input : key and value of a new Node
    # Output: Inserts a new Node in the Tree and updates all the pointers
    #         In case the key of the new node exists in the Tree, inserts nothing.
    def insert(self, k, v):
        newNode = Node(k, v)
        if self.root is None:
            self.root = newNode
            return
        (found, parent) = self._Find(self.root, newNode.getKey())
        if not found :
            newNode.setParent(parent)
            if parent.getKey() < newNode.getKey() : parent.setRight(newNode)
            else : parent.setLeft(newNode)

    # Input : Key of the node to be deleted
    # Output: True if the node is found in the Tree and deleted and the parent node of the deleted node
    #         False if the node is not found in the Tree, and None
    def delete(self, key):
        # pointer to the parent node of current node
        parent = None

        # Start with root node
        currNode = self.root

        # search key in BST
        while currNode and currNode.getKey() != key :
            parent = currNode   #update parent
            if key < currNode.getKey() :
                currNode = currNode.getLeft()
            else :
                currNode = currNode.getRight()

        # if key is not in the Tree just return
        if currNode is None :
            return False, None

        # Case 1: Node to be deleted has no children. It is a leaf
        if currNode.getLeft() is None and currNode.getRight() is None :
            if currNode == self.root :  # if the node is the root of the Tree
                self.root = None
            else :
                if parent.getLeft() == currNode :
                    parent.setLeft(None)
                else :
                    parent.setRight(None)


        # Case 2: Node to be deleted has two children.
        elif currNode.getLeft() and currNode.getRight() :
            # Find the successor node
            successor = self._getSuccessor(currNode.getRight())
            succKey, succValue = successor.getKey(), successor.getValue()
            # Recursively delete successor. The successor has most only right-child.
            result = self.delete(succKey) # Returns True because val exists in the Tree
            currNode.setKey(succKey)
            currNode.setValue(succValue)

        # Case 3: Node to be deleted has only one child.
        else :
            if currNode.getLeft() :
                child = currNode.getLeft()
            else :
                child = currNode.getRight()
            if currNode == self.root :
                self.root = child
                self.root.setParent(None)
            else :
                if parent.getLeft() == currNode :
                    parent.setLeft(child)
                else :
                    parent.setRight(child)
                child.setParent(parent)

        return True, currNode.getParent()

# if __name__ == "__main__" :
#     myTree = Tree()
#
#     # keys = [15, 10, 20, 8, 12, 16]
#     # for k in keys:
#     #     myTree.insert(k, k)
#     # myTree.delete(15)
#     # myTree.delete(10)
#     myTree.insert(4, 4)
#     myTree.insert(6, 6)
#     myTree.insert(8, 8)
#     myTree.insert(5, 5)
#     myTree.insert(4, 4)
#     myTree.insert(6, 6)
#     myTree.insert(1, 1)
#     myTree.insert(2, 2)
#     myTree.delete(4)
#     myTree.delete(1)
#     myTree.delete(5)
#     myTree.delete(6)
#     myTree.delete(8)
#     myTree.delete(2)
#     print(5)