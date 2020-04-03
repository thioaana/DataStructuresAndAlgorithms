import numpy as np
import sys

# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    def MinAndMax(i, j):
        myMin = sys.maxsize
        myMax = sys.maxsize * (-1)
        for k in range(i, j):
            a = evalt(M[i, k], M[k + 1, j], operate[k])
            b = evalt(M[i, k], m[k + 1, j], operate[k])
            c = evalt(m[i, k], M[k + 1, j], operate[k])
            d = evalt(m[i, k], m[k + 1, j], operate[k])
            myMin = min(myMin, a, b, c, d)
            myMax = max(myMax, a, b, c, d)
        return (myMin, myMax)

    values  = [int(dataset[i]) for i in range(0, len(dataset), 2)]
    operate = [dataset[i] for i in range(1, len(dataset) - 1, 2)]
    n = len(values)
    m = np.zeros([n, n], dtype = np.int64)
    M = np.zeros([n, n], dtype = np.int64)
    for i in range(n) :
        m[i, i] = values[i]
        M[i, i] = values[i]
    for s in range(1, n) :
        for i in range(n-s) :
            j = i + s
            (m[i, j], M[i, j]) = MinAndMax(i, j)
    return M[0, n-1]


if __name__ == "__main__":
    dataset =input()
    print(get_maximum_value(dataset))
