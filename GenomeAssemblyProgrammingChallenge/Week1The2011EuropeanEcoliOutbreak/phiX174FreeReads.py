# pytthon 3

def countPrefix(r, k, l) :
    # Find common suffix of k and prefix of l
    for i =
    while count < min(len(r[k]), len(r[l])) :
        if r[k][len(r[k]) - count - 1] != r[l][count] :
            return count
        count += 1
    return count

def countSuffix(r, k, l) :
    return 0

r = ["abcdef", "def1"]
c = countPrefix(r, 0, 1)
numReads = 1618
reads = []
for i in range(numReads) :
    reads.append(input().strip())

visited = [False] * numReads
for i in range(numReads - 1) :
    maxPrefix = maxSuffix = 0
    for j in range(i + 1, numReads) :
        if visited[j] : continue
        cP = countPrefix(reads, i, j)
        cS = countSuffix(reads, i, j)