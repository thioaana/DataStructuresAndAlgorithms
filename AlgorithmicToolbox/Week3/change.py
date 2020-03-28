# Uses python3
import sys

def get_change(m) :
    #write your code here
    numCoins = 0
    while m>0 :
        for coin in coins :
            if m >= coin :
                numCoins += 1
                m -= coin
                break

    return numCoins

if __name__ == '__main__':
    coins = [10, 5, 1]
    m = int(input())
    print(get_change(m))
