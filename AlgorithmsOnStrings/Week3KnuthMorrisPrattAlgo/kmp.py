# python3
import sys


def ComputePrefix(P):
    s = [0 for i in range(len(P))]
    border = 0
    for i in range(1, len(P)):
        while border > 0 and P[i] != P[border]:
            border = s[border - 1]
        if P[i] == P[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def find_pattern(pattern, text):
    """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
    result = []
    # Implement this function yourself
    return result


if __name__ == '__main__':
    # pattern = input().strip()
    text = input().strip()
    print(ComputePrefix(text))
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
