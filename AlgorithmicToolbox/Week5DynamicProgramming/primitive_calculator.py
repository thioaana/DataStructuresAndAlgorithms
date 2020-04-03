# Uses python3
import sys

def optimal_sequence(n):
    # for each number up to n find a tuple.
    # the first coord of the tuple is the count of actions to achive to the number
    # the second coord of the tuple i the index of a previous number.
    sequence = [(0, 0), (0, 0)]
    for i in range(2, n + 1) :
        n1 = (sequence [i - 1][0], i-1)
        if i%2 == 0 :
            if sequence[i // 2][0] < n1[0] :
                n1 = (sequence[i // 2][0], i // 2)
        if i%3 == 0 :
            if sequence[i // 3][0] < n1[0] :
                n1 = (sequence[i // 3][0], i // 3)
        sequence.append((n1[0] + 1, n1[1]))
    return sequence

if __name__ == '__main__':
    n = int(input())
    s = optimal_sequence(n)
    print(s[n][0])
    finalList = [n]
    k = s[n][1]
    while k >= 1 :
        finalList.append(k)
        k = s[k][1]
    for i in reversed(finalList) :
        print(i, end=" ")
