# python3
import sys


def compute_min_refills(stops, tank,):
    # write your code here
    n = len(stops) - 2
    numRefils = 0
    currentStop = 0
    while currentStop <= n :
        lastStop = currentStop
        while currentStop <= n and stops[currentStop + 1] - stops[lastStop] <= tank :
            currentStop += 1
        if currentStop == lastStop :
            return -1
        if currentStop <= n :
            numRefils += 1
    return numRefils

if __name__ == '__main__':
    # Travel d (distance) miles away
    # Can travel m miles with a ull tank
    # There are stop (list var) for fuel stops.
    d = int(input())
    m = int(input())
    n = int(input())
    # inp = input().split()
    st = [int(x) for x in input().split()]
    st.insert(0, 0)
    st.append(d)
    print(compute_min_refills(st, m))
