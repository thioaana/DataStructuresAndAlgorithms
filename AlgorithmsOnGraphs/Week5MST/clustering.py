#Uses python3
import sys
import math
from queue import PriorityQueue

class MST:
    def __init__(self):
        self.nodes = [] # includes tuples of coords.
        self.T = []     # includes the root of the set, for every node
        self.V = 0      # the number of nodes
        self.priorityEdges = PriorityQueue()    # includes tuples in form (distance, (x, y))
        self.X = [] # the final set. elements of priorityEdges in the same form

    def importPoint(self, newNode):
        self.nodes.append(newNode)
        self.V += 1
        self.T.append(self.V - 1)
        for i in range(self.V - 1) :
            self.priorityEdges.put((self.getDistance(i, self.V - 1), (i, self.V - 1)))

    def getDistance(self, indV1, indV2):
        v1 = self.nodes[indV1]
        v2 = self.nodes[indV2]
        return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

    def findRootSet(self, i):
        return self.T[i]

    def union(self, indexV1, indexV2):
        tV1 = self.T[indexV1]
        tV2 = self.T[indexV2]
        m = min(tV1, tV2)
        for k in range(self.V) :
            if self.T[k] in [tV1, tV2] :
                self.T[k] = m

    def Kruskal(self) : #, x, y):
        while not self.priorityEdges.empty() :
            p = self.priorityEdges.get()
            if self.findRootSet(p[1][0]) != self.findRootSet(p[1][1]) :
                self.X.append(p)
                self.union(p[1][0], p[1][1])

    # def clustering(self, k):


if __name__ == '__main__':
    myPoints = MST()
    n = int(input())
    for _ in range(n) :
        inp = input().split()
        x, y = int(inp[0]), int(inp[1])
        myPoints.importPoint((x, y))
    k = int(input())
    myPoints.Kruskal()
    print("{0:.12f}".format(myPoints.X[-k + 1][0]))
    # print("{0:.9f}".format(myPoints.Kruskal()))
