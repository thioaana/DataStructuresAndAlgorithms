# Uses python3
import sys
import numpy as np

def optimal_weight(W, bars):
    # write your code here
    n = len(bars)
    value = np.zeros([n, W + 1], dtype = int)
    for i in range(1, n) :
        for w in range(1, W + 1) :
            value[i, w] = value[i - 1, w]
            if bars[i] <= w :
                val = value[i - 1, w - bars[i]] + bars[i]
                if value[i, w] < val :
                    value[i, w] = val
    return value[n-1, W]

if __name__ == '__main__':
    inp = input().split()
    W = int(inp[0])
    n = int(inp[1])
    b = [int(x) for x in input().split()]
    b.insert(0, 0)
    print(optimal_weight(W, b))
