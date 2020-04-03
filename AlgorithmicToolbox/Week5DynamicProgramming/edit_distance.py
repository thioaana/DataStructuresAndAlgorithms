# Uses python3
import numpy as np
import sys

def edit_distance(s, t):
    d = np.zeros([len(s) + 1, len(t) + 1], dtype = int)
    for i in range(d.shape[0]):
        d[i, 0] = i
    for j in range(d.shape[1]):
        d[0, j] = j
    for j in range(1, d.shape[1]):
        for i in range(1, d.shape[0]) :
            insertion = d[i, j -1] + 1
            deletion  = d[i - 1, j] + 1
            mismatch  = d[i - 1, j - 1] + 1
            match = d[i - 1, j - 1]
            # print(s[i - 1], t[j - 1])
            if s[i-1] != t[j - 1] :
                match  = sys.maxsize
            d[i, j] = min(insertion, deletion, mismatch, match)
    # print(d)
    #write your code here
    return d[len(s), len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
