# Uses python3
import sys

def MergeSort(seq) :
    l = len(seq)
    if l == 1 : return seq
    mid = int(l / 2)
    seqLeft = MergeSort(seq[:mid]) # without mid
    seqRight = MergeSort(seq[mid :]) # with mid
    seqResult = Merge(seqLeft, seqRight)
    return seqResult

def Merge(seqL, seqR) :
    global counter
    # seqL and seqR are already sorted
    sRes = []
    while len(seqL) != 0 and len(seqR) != 0 :
        if seqL[0] <= seqR[0] : sRes.append(seqL.pop(0))
        else :
            sRes.append(seqR.pop(0))
            counter += len(seqL)
    sRes.extend(seqL)
    sRes.extend(seqR)
    counter += len(seqL) * len(seqR)
    return sRes

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = n * [0]
    counter = 0
    c = MergeSort(a)
    print(counter)
