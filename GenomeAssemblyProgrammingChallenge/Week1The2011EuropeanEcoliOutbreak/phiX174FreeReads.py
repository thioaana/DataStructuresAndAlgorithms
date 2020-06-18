#uses python3

def getCommonSP(r, k, l, exLap) :
    # Find common substring
    # From suffix of g and prefix of l
    m = min(len(r[k]), len(r[l]))
    c1 = m
    while c1 > 0 :
        if c1 <= exLap : return 0
        if r[l][:c1] == r[k][-c1:] : break
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
    while numForSearch > 0 :
        maxSP = [0, -1]
        for j in range(numReads):
            if visited[j] : continue

            cSP = getCommonSP(reads, i, j, maxSP[0])
            if cSP > maxSP[0] :
                maxSP = [cSP, j]

        genome = genome + reads[maxSP[1]][maxSP[0]:]
        visited[maxSP[1]] = True
        i = maxSP[1]
        numForSearch -= 1

    cPS = getCommonSP(reads, maxSP[1], 0, 0)
    genome = genome[:-cPS]
    print(genome)