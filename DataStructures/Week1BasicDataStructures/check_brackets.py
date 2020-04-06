# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            result = are_matching(opening_brackets_stack[len(opening_brackets_stack) - 1][1], next)
            if not(result) :
                return i + 1
            else :
                a = opening_brackets_stack.pop()
    if len(opening_brackets_stack) > 0 :
        return opening_brackets_stack[len(opening_brackets_stack) - 1][0] + 1
    else :
        return "Success"

if __name__ == "__main__":
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
