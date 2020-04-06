#python3
import sys

class StackWithMax():
    def __init__(self):
        self.maximum = sys.maxsize * (-1)
        self.__stack = []

    def Push(self, a):
        self.maximum = max(a, self.maximum)
        self.__stack.append((a, self.maximum))

    def Pop(self):
        assert(len(self.__stack))
        m = self.__stack.pop()

    def Max(self):
        return self.__stack[len(self.__stack) - 1][1]

class naive():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        return max(self.__stack)

    def Max(self):
        return self.maximum
        # assert(len(self.__stack))
        # return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(input())
    for _ in range(num_queries):
        query = input().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
