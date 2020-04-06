# python3
# Turn an Array into a Heap IN PLACE.
import sys

class CBT() :
    def __init__(self, arr) :
        self.__heap = [len(arr)]
        self.__heap.extend(arr)

    def ShiftDown(self, i):
        swaps = []
        size = self.__heap[0]
        minIndex = i
        l = self.__LeftChild(i)
        r = self.__RightChild(i)
        if l <= size and self.__heap[l] < self.__heap[minIndex] :
            minIndex = l
        if r <= size and self.__heap[r] < self.__heap[minIndex] :
            minIndex = r
        if i != minIndex :
            swaps.append((i - 1, minIndex - 1))
            temp = self.__heap[i]
            self.__heap[i] = self.__heap[minIndex]
            self.__heap[minIndex] = temp
            s = self.ShiftDown(minIndex)
            if len(s) != 0 :
                swaps.extend(s)
        return swaps

    @staticmethod
    def __Parent(i):
        return int(i / 2)

    @staticmethod
    def __LeftChild(i):
        return i * 2

    @staticmethod
    def __RightChild(i):
        return i * 2 + 1

if __name__ == "__main__" :
    n = int(input())
    data = list(map(int, input().split()))

    myHeap = CBT(data)
    permut = []
    for i in range(int(n/2), 0, -1) :
        permut.extend(myHeap.ShiftDown(i))
    print(len(permut))
    for t in permut :
        print(t[0], t[1])
