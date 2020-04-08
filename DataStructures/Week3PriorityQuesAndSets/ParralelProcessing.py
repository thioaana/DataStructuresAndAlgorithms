# python3
# Turn an Array into a Heap IN PLACE.
import sys

class CBT() :
    def __init__(self, n) :
        self.__heap = (n + 1) * [0]

    def Insert(self, tuple) :
        self.__heap[0] += 1
        self.__heap[self.__heap[0]] = tuple
        self.__ShiftUp(self.__heap[0])

    def ExtractMin(self) :
        result = self.__heap[1]
        self.__heap[1] = self.__heap[self.__heap[0]]
        self.__heap[0] -= 1
        self.__ShiftDown(1)
        return result

    def GetMin(self):
        return self.__heap[1]

    def __ShiftUp(self, i) :
        while i > 1 and self.__heap[i] < self.__heap[self.__Parent(i)]: #self.__heap[i][0] < self.__heap[self.__Parent(i)][0]:
            temp = self.__heap[i]
            self.__heap[i] = self.__heap[self.__Parent(i)]
            self.__heap[self.__Parent(i)] = temp
            i = self.__Parent(i)

    def __ShiftDown(self, i):
        size = self.__heap[0]
        maxIndex = i
        l = self.__LeftChild(i)
        r = self.__RightChild(i)
        if l <= size and self.__heap[l] < self.__heap[maxIndex] : #self.__heap[l][0] < self.__heap[maxIndex][0] :
            maxIndex = l
        if r <= size and self.__heap[r] < self.__heap[maxIndex] : #self.__heap[r][0] < self.__heap[maxIndex][0] :
            maxIndex = r
        if i != maxIndex :
            temp = self.__heap[i]
            self.__heap[i] = self.__heap[maxIndex]
            self.__heap[maxIndex] = temp
            self.__ShiftDown(maxIndex)

    @staticmethod
    def __Parent(i):
        return int(i / 2)

    @staticmethod
    def __LeftChild(i):
        return i * 2

    @staticmethod
    def __RightChild(i):
        return i * 2 + 1

    def PrintThreads(self) :
        print(self.__heap)

if __name__ == "__main__" :
    inp = input().split()
    NumThreads = int(inp[0])
    NumJobs = int(inp[1])
    TimePerJob = list(map(int, input().split()))

    myThreads = CBT(NumThreads)
    for i in range(NumThreads) :
        myThreads.Insert((TimePerJob[i] + 0, i)) # Inserts with the index and the EndTime
        print(i, 0)

    for i in range(NumThreads, NumJobs) :
        extracted =myThreads.ExtractMin()

        # Prints the next element which inserts in the heap
        # The element  has the index of the previous and StartTime the EndTime of the previous
        print(extracted[1], extracted[0])
        myThreads.Insert((TimePerJob[i] + extracted[0], extracted[1]))