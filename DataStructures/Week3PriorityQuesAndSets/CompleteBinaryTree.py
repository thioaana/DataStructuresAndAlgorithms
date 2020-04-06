import sys

class CBT() :
    def __init__(self) :
        self.__heap = [0]

    def Insert(self, value) :
        self.__heap[0] += 1
        self.__heap.append(value)
        self.__ShiftUp(self.__heap[0])

    def ExtractMax(self) :
        result = self.__heap[1]
        self.__heap[1] = self.__heap[self.__heap[0]]
        self.__heap[0] -= 1
        self.__ShiftDown(1)
        return result

    def Remove(self, i) :
        self.__heap[i] = sys.maxsize
        self.__ShiftUp(i)
        m = self.ExtractMax()

    def ChangePriority(self, i, newValue) :
        oldValue = self.__heap[i]
        self.__heap[i] = newValue

        if oldValue < newValue :
            self.__ShiftUp(i)
        else :
            self.__ShiftDown(i)

    def GetMax(self) :
        return self.__heap[1]

    def __ShiftUp(self, i) :
        while i > 1 and self.__heap[i] > self.__heap[self.__Parent(i)]:
            temp = self.__heap[i]
            self.__heap[i] = self.__heap[self.__Parent(i)]
            self.__heap[self.__Parent(i)] = temp
            i = self.__Parent(i)

    def __ShiftDown(self, i):
        size = self.__heap[0]
        maxIndex = i
        l = self.__LeftChild(i)
        r = self.__RightChild(i)
        if l <= size and self.__heap[l] > self.__heap[maxIndex] :
            maxIndex = l
        if r <= size and self.__heap[r] > self.__heap[maxIndex] :
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

if __name__ == "__main__":
    myCBT = CBT()

    a = [18, 7, 12, 13, 29, 11, 42, 14, 18]
    for x in a:
        myCBT.Insert(x)
    print(myCBT.GetMax())
    print("ppp")

