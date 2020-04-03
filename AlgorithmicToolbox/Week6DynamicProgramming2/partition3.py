# Uses python3
import sys
import itertools
import numpy as np

# ------------ DOES NOT WORK -------------------

def optimal_weight(bars):
    a = sum(bars)
    if a % 3 != 0 : return 0
    if len(bars) < 3 : return 0
    W = a // 3
    bars.insert(0, 0)

    for times in range(3):
        n = len(bars)
        value = np.zeros([n, W + 1], dtype = int)
        for i in range(1, n) :
            for w in range(1, W + 1) :
                value[i, w] = value[i - 1, w]
                if bars[i] <= w :
                    val = value[i - 1, w - bars[i]] + bars[i]
                    if value[i, w] < val :
                        value[i, w] = val

        if value[n-1, W] != W : return 0

        # Reconstruction - Find the used bars-cells-numbers
        construct = []
        init = value[n-1, W]
        w = W
        for i in range(n-1, 0, -1) :
            if value[i - 1, w] == value[i, w] :
                construct.append(0)
            else :
                construct.append(1)
                w = w - bars[i]

        construct.reverse()
        for i in range(len(construct)-1, -1, -1) :
            if construct[i] == 1 :
                del bars[i + 1]

    return 1

def naive(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

if __name__ == '__main__':
    # Hint : Run Knapsack with W as sum/3
    n = int(input())
    A = [int(x) for x in input().split()]

    # Stress test code
    # while(True) :
    #     n = random.randint(1, 20)
    #     A = [random.randint(1,30) for i in range(n)]
    #     nav = naive(A)
    #     A.sort(reverse=True)
    #     opt = optimal_weight(A)
    #     if nav != opt :
    #         print(A)
    #         print("nav = ", nav, "opt = ", opt)
    #         break
    print(naive(A))
    A.sort(reverse=True)
    print(optimal_weight(A))
