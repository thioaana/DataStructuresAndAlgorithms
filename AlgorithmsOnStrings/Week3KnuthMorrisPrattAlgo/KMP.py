# python3
import sys


def ComputePrefix(P):
    s = [0 for i in range(len(P))]
    border = 0
    for i in range(1, len(P)):
        while border > 0 and P[i] != P[border]:
            border = s[border - 1]
        if P[i] == P[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s

def FindOccurKMP(pattern, text):
    result = []
    S = pattern + "$" + text
    patternLength = len(pattern)
    s = ComputePrefix(S)
    for i in range(patternLength + 1, len(S)) :
        if s[i] == patternLength :
            result.append(i - 2 * patternLength)
    return result

if __name__ == '__main__':
    pattern = input().strip()
    text = input().strip()
    result = FindOccurKMP(pattern, text)
    print(" ".join(map(str, result)))
