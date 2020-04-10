# python3
import sys

if __name__ == '__main__':
    PhoneBook = [None for i in range(10000000)]
    n = int(input())
    for _ in range(n) :
        inp = input().split()
        if inp[0] == "add" :
            PhoneBook[int(inp[1])] = inp[2]
        elif inp[0] == "del" :
            PhoneBook[int(inp[1])] = None
        elif inp[0] == "find" :
            if PhoneBook[int(inp[1])] != None :
                print(PhoneBook[int(inp[1])])
            else :
                print("not found")
