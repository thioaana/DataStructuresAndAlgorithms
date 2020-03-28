# Uses python3

def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib_better(n) :
    F = []
    F.append(0)
    F.append(1)

    for i in range(2, n+1) :
        F.append(F[i - 2] + F[i - 1])
    return F[n]

if __name__ == '__main__':
    n = int(input())
    # print(calc_fib(n))
    print(calc_fib_better(n))
