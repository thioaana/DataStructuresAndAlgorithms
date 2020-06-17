#uses python3

def getCommonSP(r, k, l) :
    # Find common substring
    # From suffix of g and prefix of l
    c1 = min(len(r[k]), len(r[l]))
    while c1 > 0 :
        if r[l].startswith(r[k][-c1:]) :
            break
        c1 -= 1
    return c1

if __name__ == "__main__" :
    numReads = 1618
    reads = []
    for i in range(numReads) :
        reads.append(input().strip())

    visited = [False] * numReads
    visited[0]= True
    genome = reads[0]
    i =0
    numForSearch = numReads - 1
    while numForSearch > 1 :
        maxSP = [0, -1]
        for j in range(numReads):
            if visited[j] : continue

            cSP = getCommonSP(reads, i, j)
            if cSP > maxSP[0] :
                maxSP = [cSP, j]

        genome = genome + reads[maxSP[1]][maxSP[0]:]
        visited[maxSP[1]] = True
        i = maxSP[1]
        numForSearch -= 1

    falseIndex = visited.index(False)
    cSP = getCommonSP(reads, maxSP[1], falseIndex)  # Suffix of last inserted with Prefix of FalseIndex
    cPS = getCommonSP(reads, falseIndex, 0)         # Suffix of FalseIndex with Prefix of 0 index (first inserted in genome)
    genome = genome + reads[falseIndex][cSP:-cPS]
    print(genome)