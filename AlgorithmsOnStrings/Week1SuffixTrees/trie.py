#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    numNodes = 0
    tree = dict({0:{}}) #a graph consisting of a single node root

    # write your code here
    for pat in patterns :
        currentNode = 0
        for i in range(len(pat)) :
            currentSymbol = pat[i]
            if currentSymbol in tree[currentNode] :
                currentNode = tree[currentNode][currentSymbol]
            else :
                numNodes += 1
                tree[currentNode][currentSymbol] = numNodes
                tree[numNodes] = {}
                currentNode = numNodes
    return tree


if __name__ == '__main__':
    n = int(input())
    patterns = []
    for i in range(n) :
        patterns.append(input())
    # patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))