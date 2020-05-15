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
        order[count[alphabet[c]]] = i
    return order


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
    print(SortCharacters(text))
    # print(" ".join(map(str, build_suffix_array(text))))
