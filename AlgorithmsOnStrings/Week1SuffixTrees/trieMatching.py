# python3
import sys

def BuildTrie(patterns):
    numNodes = 0
    tree = dict({0: {}})  # a graph consisting of a single node root

    for pat in patterns:
        currentNode = 0
        for i in range(len(pat)):
            currentSymbol = pat[i]
            if currentSymbol in tree[currentNode]:
                currentNode = tree[currentNode][currentSymbol]
            else:
                numNodes += 1
                tree[currentNode][currentSymbol] = numNodes
                tree[numNodes] = {}
                currentNode = numNodes
    return tree


def PrefixTrieMatching(text, trie, result):
    indexSymbol = 0             # first letter of 	Text
    v = 0                       # root of Trie
    while True :
        if not bool(trie[v]):   # if 𝑣 is a leaf in Trie
            return True         # the pattern found
        elif indexSymbol < len(text):           # checking if the text is not exhausted
            if text[indexSymbol] in trie[v] :   # if there is an edge (𝑣, 𝑤) in Trie labeled by symbol:
                v = trie[v][text[indexSymbol]]
                indexSymbol += 1
            else:
                return False
        else :
            return False
def solve(text, n, patterns):
    result = []
    trie = BuildTrie(patterns)
    for i in range(len(text)):
        if PrefixTrieMatching(text[i:], trie, result):
            result.append(i)
    return result

if __name__ == '__main__':
    text = input()
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input().strip())
    ans = solve(text, n, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')
