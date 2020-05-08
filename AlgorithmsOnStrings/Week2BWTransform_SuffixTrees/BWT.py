# python3
import sys

# Input :   A string Text
# Output :  BWT(Text).
def BWT(text):
    BWTMatrix = [text[-1] + text[:-1]]
    for i in range(1, len(text)) :
        BWTMatrix.append(BWTMatrix[i-1][-1] + BWTMatrix[i-1][:-1])
    BWTMatrix.sort()
    BWTString = "".join([str(x[-1]) for x in BWTMatrix])
    return BWTString

if __name__ == '__main__':
    text = input()

    print(BWT(text))