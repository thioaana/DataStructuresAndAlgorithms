# Uses python3
import sys
import random

def get_majority_element(a) :
    seq = MergeSort(a)
    l = len(seq)
    for i in range(int(l / 2) + l%2) :
        if seq[i] == seq[i + int(l / 2)] :
            return 1
    return 0

def MergeSort(seq) :
    l = len(seq)
    if l == 1 : return seq
    mid = int(l / 2)
    seqLeft = MergeSort(seq[:mid]) # without mid
    seqRight = MergeSort(seq[mid :]) # with mid
    seqResult = Merge(seqLeft, seqRight)
    return seqResult

def Merge(seqL, seqR) :
    # seqL and seqR are already sorted
    sRes = []
    while len(seqL) != 0 and len(seqR) != 0 :
        if seqL[0] <= seqR[0] : sRes.append(seqL.pop(0))
        else : sRes.append(seqR.pop(0))
    sRes.extend(seqL)
    sRes.extend(seqR)
    return sRes

def naive(a):
    dic = {}
    for i in a:
        if (i in dic): dic[i] += 1
        else:          dic[i] = 1
    maxValue = 0
    maxKey = 0
    for k, v in dic.items() :
        if v > maxValue :
            maxValue = v
            maxKey = k
    return (maxKey, maxValue)

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    print(get_majority_element(a))
    # Stress test code
    # while(True) :
    #     n = random.randint(0, 10)
    #     a = [random.randint(2,3) for i in range(5)]
    #     maj = get_majority_element(a)
    #     nav = naive(a)
    #     # print(a, naive(a), get_majority_element(a))
    #     if maj == 1 and naive(a)[1] <=int(len(a)/2) : print(a, maj, nav); break
    #     if maj == 0 and naive(a)[1] >int(len(a)/2) : print(a, maj, nav); break
    #     print(maj)
    #     # print(naive(a))