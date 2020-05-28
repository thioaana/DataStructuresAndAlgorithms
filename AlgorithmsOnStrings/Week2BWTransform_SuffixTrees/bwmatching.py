# python3
import sys
import copy


def createCountArray(BWTtext):
    d = {0: {"$": 0, "A": 0, "C": 0, "G": 0, "T": 0}}
    for i in range(len(BWTtext)):
        d[i + 1] = {"$": d[i]["$"], "A": d[i]["A"], "C": d[i]["C"], "G": d[i]["G"], "T": d[i]["T"]}
        c = BWTtext[i]
        d[i + 1][c] = d[i][c] + 1
    return d

def getFirstOccurence(countA, s):  # Get the first position of symbol in FirstColumn which is sorted.
        chain = ["$", "A", "C", "G", "T"]
        ind = chain.index(s)
        sum = 0
        for i in range(ind):
            sum += countA[chain[i]]
        return sum

def BWMatching(firstCol, lastCol, pattern, countTable):
    top = 0
    bottom = len(lastCol) - 1
    while top <= bottom:
        for i in range(len(pattern)-1, -1, -1):
            symbol = pattern[i]
            a = countTable[bottom + 1][symbol]
            b = countTable[top][symbol]
            if countTable[bottom][symbol] - countTable[top][symbol] + 1 > 0:  # if positions from top to bottom in LastColumn contain an occurrence of symbol
                firstOccurence = getFirstOccurence(countTable[len(lastCol)], symbol)
                top = firstOccurence + countTable[top][symbol]
                bottom = firstOccurence + countTable[bottom + 1][symbol] - 1
            else:
                return 0
        return bottom - top + 1


if __name__ == '__main__':
    BWTtext = input()
    n = int(input())
    patterns = []
    patterns = input().split()
    # BWTtext = "AT$TCTATG"
    # patterns = ["TCT", "TATG"]
    countArray = createCountArray(BWTtext)
    BWTList = [BWTtext[i] for i in range(len(BWTtext))]
    firstCol = copy.deepcopy(BWTList)
    firstCol.sort()
    result = []
    for pat in patterns:
        result.append(BWMatching(firstCol, BWTtext, pat, countArray))

    print(' '.join(map(str, result)))
