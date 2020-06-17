# pytthon 3

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


    # # Find common substring
    # # From suffix of k and prefix of l
    # c1 = min(len(r[k]), len(r[l]))
    # while c1 > 0 :
    #     if r[l].startswith(r[k][-c1:]) :
    #         break
    #     c1 -= 1
    # # c1 += 1
    #
    # # From prefix of k and suffix of l
    # c2 = min(len(r[k]), len(r[l]))
    # while c2 > 0:
    #     if r[l].endswith(r[k][:c2]):
    #         break
    #     c2 -= 1
    # # c2 += 1

    return c1, c2

class Node :
    def __init__(self, ind, s, p, n):
        self.index = ind
        self.value = s
        self.prev = p
        self.next = n

class Graph :
    def __init__(self, n):
        self.numReads = n
        self.gr = []

    def createNodes(self, r):
        visited = [False] * self.numReads
        for i in range(self.numReads - 1) :
            self.gr.append(Node(i, r[i], -1, -1))
            visited[i] = True
            maxSP = [0, -1]  # [maximum i Suffix].
            maxPS = [0, -1]  # [maximum i Prefix].
            for j in range(numReads):  # (i + 1, numReads) :
                if visited[j]: continue



if __name__ == "__main__" :
    # r = ["abcdef", "def1"]
    # c = getCommonPrefixOrSuffix(r, 0, 1)
    nR = 5#1618
    reads = []
    for i in range(nR) :
        reads.append(input().strip())

    graph = Graph(nR)
    graph.createNodes(r)

    visited = [False] * nR
    visited[0]= True
    genome = reads[0]
    for i in range(numReads-1) :
        # if visited[i]: continue
        # visited[i] = True
        maxSP = [0, -1] #[maximum S-P, index  of P].
        maxPS = [0, -1] #[maximum P-S, index  of S].
        for j in range(numReads):#(i + 1, numReads) :
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
    print(genome)