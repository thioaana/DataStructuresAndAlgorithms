# python3
import sys
import copy


def naive(BWTtext):
    BWTList = [BWTtext[i] for i in range(len(BWTtext))]
    firstCol = copy.deepcopy(BWTList)
    firstCol.sort()
    for k in range(len(BWTList) - 1):
        firstCol = [BWTtext[i] + firstCol[i] for i in range(len(BWTtext))]
        firstCol.sort()
    return firstCol[0][1:] + firstCol[0][0]


def createCountArray(BWTtext) :
    d = {0:{"$" : 0, "A": 0, "C" : 0, "G" : 0, "T" : 0}}
    for i in range(len(BWTtext)) :
        d[i+1] = {"$" : d[i]["$"], "A": d[i]["A"], "C" : d[i]["C"], "G" : d[i]["G"], "T" : d[i]["T"]}
        c = BWTtext[i]
        d[i + 1][c] = d[i][c] + 1
    return d

def getNumCharsBeforeSymbol(countA, s):
    chain = ["$", "A", "C", "G", "T"]
    ind = chain.index(s)
    sum = 0
    for i in range(ind) :
        sum += countA[chain[i]]
    return sum

def InverseBWT(BWTtext):
    # Create first column
    BWTList = [BWTtext[i] for i in range(len(BWTtext))]
    firstCol = copy.deepcopy(BWTList)
    firstCol.sort()

    # Create Count Array. Sets the pointer to 0
    countArray = createCountArray(BWTtext)
    p = 0
    text = [firstCol[0]]

    # Execute len(BWTtext) times
    for i in range(len(BWTtext) - 1) :
        symbol = BWTtext[p]
        text.append(symbol)
        p = countArray[p][symbol] + getNumCharsBeforeSymbol(countArray[len(BWTtext)], symbol)
    text.reverse()
    return "".join([c for c in text])


if __name__ == '__main__':
    BWTtext = input()
    print(InverseBWT(BWTtext))
