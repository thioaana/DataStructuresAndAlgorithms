# python3
import sys


def SortCharacters(text):
    order = [0 for i in text]
    alphabet = {"$": 0, "A": 1, "C": 2, "G": 3, "T": 4}
    count = [0, 0, 0, 0, 0]
    for i in range(len(text)):
        count[alphabet[text[i]]] += 1
    for j in range(1, len(count)):
        count[j] += count[j - 1]
    for k in range(len(text) - 1, -1, -1):
        c = text[k]
        count[alphabet[c]] -= 1
        order[count[alphabet[c]]] = k
    return order

def ComputeCharClasses(text, order) :
    classes = [0 for i in text]
    classes[order[0]] = 0
    for i in range(1, len(text)) :
        if text[order[i]] != text[order[i - 1]] :
            classes[order[i]] = classes[order[i - 1]] + 1
        else :
            classes[order[i]] = classes[order[i - 1]]
    return classes

def SortDouble(text, L, order, classes) :
    count = [0 for i in text]
    newOrder = [0 for i in text]
    for i in range(len(text)) :
        count[classes[i]] += 1
    for j in range(1, len(text)) :
        count[j] = count[j] + count[j - 1]
    for k in range(len(text) - 1, -1, -1) :
        start = (order[k] - L + len(text))%len(text)
        cl = classes[start]
        count[cl] -= 1
        newOrder[count[cl]] = start
    return newOrder

def UpdateClasses(order, classes, L) :
    newClasses = [0 for i in range(len(order))]
    for i in range(1, len(order)) :
        cur = order[i]
        prev = order[i - 1]
        mid = cur + L
        midPrev = (prev + L) % len(order)
        if classes[cur] != classes[prev] or classes[mid] != classes[midPrev] :
            newClasses[cur] = newClasses[prev] + 1
        else :
            newClasses[cur] = newClasses[prev]
    return newClasses

def BuildSuffixArray(text):
    order = SortCharacters(text)
    classes = ComputeCharClasses(text, order)
    L = 1
    while L < len(text):
        order = SortDouble(text, L, order, classes)
        classes = UpdateClasses(order, classes, L)
        L = 2 * L
    return order


if __name__ == '__main__':
    text = input().strip()
    # print(BuildSuffixArray(text))
    print(" ".join(map(str, BuildSuffixArray(text))))
