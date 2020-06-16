#uses python3

def getCommonPrefixOrSuffix(r,g, l):#(r, k, l) :
    # Find common substring
    # From suffix of g and prefix of l
    c1 = min(len(g), len(r[l]))
    while c1 > 0 :
        if r[l].startswith(g[-c1:]) :
            break
        c1 -= 1

    # From prefix of g and suffix of l
    c2 = min(len(g), len(r[l]))
    while c2 > 0:
        if r[l].endswith(g[:c2]):
            break
        c2 -= 1

    return c1, c2

if __name__ == "__main__" :
    numReads = 1618
    reads = []
    for i in range(numReads) :
        reads.append(input().strip())

    visited = [False] * numReads
    visited[0]= True
    genome = reads[0]
    for i in range(numReads-2) :
        maxSP = [0, -1]
        maxPS = [0, -1]
        for j in range(numReads):
            if visited[j] : continue

            cSP, cPS = getCommonPrefixOrSuffix(reads, genome, j)
            if cSP > maxSP[0] :
                maxSP = [cSP, j]
            if cPS > maxPS[0] :
                maxPS = [cPS, j]

        if maxSP[0] >= maxPS[0] :
            genome = genome + reads[maxSP[1]][maxSP[0]:]
            visited[maxSP[1]] = True
        else :
            genome = reads[maxPS[1]][:maxPS[0]-1] + genome
            visited[maxPS[1]] = True
    falseIndex = visited.index(False)
    cSP, cPS = getCommonPrefixOrSuffix(reads, genome, falseIndex)
    genome = genome + reads[falseIndex][cSP:-cPS]


    print(genome)