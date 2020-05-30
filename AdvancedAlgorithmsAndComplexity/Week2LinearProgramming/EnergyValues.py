# python3
import random
import numpy as np

EPS = 1e-6
PRECISION = 20

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return (a, b)

def ReadEquationTesting():
    size = 15#random.randint(1, 5)
    a = []; b = []
    for row in range(size):
        temp = [random.randint(-3,3) for i in range(size + 1)]
        a.append([float(t) for t in temp[:size]])
        b.append(float(temp[size]))
    return (a, b)


def SelectPivotElement(a, b, index):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    for i in range(index, len(a)) :
        if a[i][index] != 0 :
            if i != index :
                SwapLines(a, b, i, index)
            break

def SwapLines(a, b, row1, row2):
    tempA = a[row1]
    a[row1] = a[row2]
    a[row2] = tempA
    tempB = b[row1]
    b[row1] = b[row2]
    b[row2] = tempB

def SolveEquation(equ):
    a = equ[0]
    b = equ[1]
    size = len(a)

    # used_columns = [False] * size
    # used_rows = [False] * size
    for diag in range(size):
        SelectPivotElement(a, b, diag)
        # Main Equation : divide every coef by the coef of the diagonal variable
        subtractor = a[diag][diag]
        for i in range(diag, size):
            a[diag][i] /= subtractor
        b[diag] /= subtractor

        # All other Equations
        for j1 in range(diag + 1, size):
            subtractor = a[j1][diag] / a[diag][diag]
            b[j1] -= subtractor * b[diag]
            for j2 in range(diag, size):
                a[j1][j2] -= subtractor * a[diag][j2]

    for i in range(size -1, 0, -1) :
        for row in range(i - 1, -1, -1):
            Coef = a[row][i] / a[i][i]
            b[row] -= Coef * b[i]
            for j in range(size) :
                a[row][j] -= Coef * a[i][j]

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    # while True : # Used for testing
    equation = ReadEquation()
    # equation = ReadEquationTesting() # Used for testing
    # print(equation) # Used for testing
    solution = SolveEquation(equation)
    PrintColumn(solution)

    # Used for testing
    # naive = np.linalg.solve(equation[0], equation[1])
    # for i in range(len(solution)):
    #     problem = False
    #     if abs(solution[i]-naive[i]) >0.01 :
    #         problem = True
    #     if problem :
    #         print("problem")
    #         # print(equation[0], equation[1])
    #         print(solution)
    #         print(naive)
    #         break
