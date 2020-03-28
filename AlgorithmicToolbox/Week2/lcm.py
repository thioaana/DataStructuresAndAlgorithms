# Uses python3
import sys

def gcd_better(a, b):
    if b == 0 : return a
    a1 = a % b
    return gcd_better(b, a1)

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def lcm_better(a, b):
    return (a * b) // gcd_better(a, b)

if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split())
    # print(lcm_naive(a, b))
    print(lcm_better(a, b))

