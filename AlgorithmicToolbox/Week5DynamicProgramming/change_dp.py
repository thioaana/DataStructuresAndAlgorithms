# Uses python3
import sys

def get_change(money):
    #write your code here
    MinNumCoins = (money + 1) * [0]
    for m in range(1, money + 1) :
        MinNumCoins[m] = sys.maxsize
        for coin in [1, 3, 4] :
            if m >= coin :
                NumCoins = MinNumCoins[m - coin] + 1
                if NumCoins < MinNumCoins[m] :
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(input())
    a = get_change(m)
    print(a)