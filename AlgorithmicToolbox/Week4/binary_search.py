# Uses python3
import sys

def binary_search(seq, key, left, right):
    # left, right = 0, len(a)
    # write your code here
    if right <left : return -1
    mid = int(left + (right - left) / 2)
    if key == seq[mid] : return mid
    elif key < seq[mid] :
        return binary_search(seq, key, left, mid - 1)
    else :
        return binary_search(seq, key, mid + 1, right)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    s = [int(i) for i in input().split()]
    ch= [int(i) for i in input().split()]
    del s[0]; del ch[0]
    for c in ch:
        print(binary_search(s, c, 0, len(s) - 1), end = ' ')
