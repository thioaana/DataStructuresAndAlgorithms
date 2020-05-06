# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def BuildTrie(patterns):
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


def PrefixTrieMatching(text, trie, result) :
# PrefixTrieMatching(Text, Trie)
# 	symbol ← first letter of 	Text
# 	𝑣 ← root of	Trie
# 	while forever:
# 		if 𝑣 is a leaf in Trie:
# 			return the		pattern	spelled	by the path	from the root to 𝑣
# 		else if there is an edge (𝑣, 𝑤) in Trie labeled by symbol:
# 			symbol ← next		letter		of		Text
# 			𝑣 ← 𝑤
# 		else:
# 			output “no	matches	found”
# 	return

def solve (text, n, patterns):
	result = []
	trie = BuildTrie(patterns)
	for i in range(len(text)) :
		PrefixTrieMatching(text, trie, result)
	# // write your code here
	return result

if __name__ == '__main__':
	text = input()
	n = int(input())
	patterns = []
	for i in range (n):
		patterns.append(input().strip())

	ans = solve (text, n, patterns)

	sys.stdout.write (' '.join (map (str, ans)) + '\n')
