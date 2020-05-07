# python3
import sys

# Build a Trie where a pattern may be a prefix of another pattern. Uses a $ as a flag
def BuildTrie(patterns):
    numNodes = 0
    tree = dict({0: {}})  # a graph consisting of a single node root

    for pat in patterns:
        currentNode = 0
        for i in range(len(pat)):
            currentSymbol = pat[i]
            if currentSymbol in tree[currentNode]:
                if i == len(pat) - 1:  # Reached the end of the pattern.
                    t = tree[currentNode][currentSymbol]
                    tree[currentNode][t] = "$"  # The $ sign is added as a flag indicating that a pattern i reached to the end.
                currentNode = tree[currentNode][currentSymbol]
            else:
                numNodes += 1
                tree[currentNode][currentSymbol] = numNodes
                if i == len(pat) - 1:  # Reached the end of the pattern.
                    t = tree[currentNode][currentSymbol]
                    tree[currentNode][t] = "$"  # The $ sign is added as a flag indicating that a pattern i reached to the end.
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
                if trie[v][text[indexSymbol]] in trie[v] : # Found sign $, which means reached to the end of a pattern without reaching a leaf.
                    return True
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

def naive(text, n, patterns) :
    result = []
    for pat in patterns :
        for i in range(len(text) - len(pat) + 1) :
            if pat == text[i:i + len(pat)]:
                if i not in result : result.append(i)
    return result

# Stress Test Function
def createRandomSample() :
    import random
    numTextChars = random.randint(1, 10000)
    numPatterns = random.randint(1, 5000)
    chars = ["A", "C", "G", "T"]
    text = ''.join(str(x) for x in random.choices(["A", "C", "G", "T"], k = min(100, numTextChars)))
    patterns = []
    for i in range(numPatterns):
        pat = ''.join(str(x) for x in random.choices(["A", "C", "G", "T"], k=random.randint(1, 3)))
        patterns.append(pat)
    return (text, numTextChars, patterns)

if __name__ == '__main__':
    text = input()
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input().strip())
    ans = solve(text, n, patterns)
    sys.stdout.write(' '.join(map(str, ans)) + '\n')

    # This part of the code is used for Stressing the Code.
    # s = 0
    # while True :
    #     s += 1
    #     text, n, patterns = createRandomSample()
    #
    #     ans = solve(text, n, patterns)
    #     ansNaive = naive(text, n, patterns)
    #
    #     if len(ans) == len(ansNaive) :
    #         for i in ans :
    #             if  i not in ansNaive :
    #                 break
    #     else :
    #         break
    #     print(s)
    # print(ans, "\n", ansNaive)