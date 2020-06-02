# python3
from sys import stdin
import sys
import itertools

def ReadData() :
  n, m = list(map(int, stdin.readline().split()))
  A = []
  for i in range(n):
    A += [list(map(int, stdin.readline().split()))]

  b = list(map(int, stdin.readline().split()))

  # Append with constraints Xi>=0 ==> -Xi<=0
  for i2 in range(m):
    A += [[0 for i3 in range(m)]]
    A[n + i2][i2] = -1
    b += [0]

  # Append with infinity condition
  A += [[1 for i3 in range(m)]]
  b += [1000000000]
  n += 1

  c = list(map(int, stdin.readline().split()))
  return (n, m, A, b, c)

def SelectPivotElement(a, b, index):
  # Selects the first free element.
  for i in range(index, len(a)):
    if a[i][index] != 0:
      if i != index:
        SwapLines(a, b, i, index)
      return True
  return False

def SwapLines(a, b, row1, row2):
  tempA = a[row1]
  a[row1] = a[row2]
  a[row2] = tempA
  tempB = b[row1]
  b[row1] = b[row2]
  b[row2] = tempB

def SolveEquations(equ):
  a = equ[0]
  b = equ[1]
  size = len(a)

  # used_columns = [False] * size
  # used_rows = [False] * size
  for diag in range(size):
    pivotFound = SelectPivotElement(a, b, diag)
    # Check if the system of equations is Impossible or Infinity
    if not pivotFound :
      return (False, 0)
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

  for i in range(size - 1, 0, -1):
    for row in range(i - 1, -1, -1):
      Coef = a[row][i] / a[i][i]
      b[row] -= Coef * b[i]
      for j in range(size):
        a[row][j] -= Coef * a[i][j]

  return (True, b)

def CreateSystemEquations(S, A, b) :
  eqA = []
  eqB = []
  for si in S :
    eqA.append(A[si][:])
    eqB.append(b[si])
  return (eqA, eqB)

def GetVertices(n, m, A, b):
  vertices = []
  infSolutions = []
  fullSet = set()
  for i in range(n + m):
    fullSet.add(i)
  subsets = list(itertools.combinations(fullSet, m))
  for subset in subsets :
    equations = CreateSystemEquations(subset, A, b)
    eqSolution = SolveEquations(equations)

    if not eqSolution[0] :
      continue     # The system of equations is Impossible or Infinity. Go to the next one

    else :
      if eqSolution[1] not in vertices :
        vertices += [eqSolution[1]]
        if subset[-1] == n + m - 1: # Save solutions with infinity condition
          infSolutions.append(eqSolution[1])
  return vertices, infSolutions

def CheckValidation(v, A, B):
  v2 = []
  for i in range(len(v)):
    checked = True
    for j in range(len(A)) :
      leftPart = 0
      for k in range(len(A[j])) :
        leftPart += A[j][k] * v[i][k]
      if leftPart > B[j] + 0.001:
        checked = False
        break
    if checked :
      v2.append(v[i][:])
  return v2

def FindMax(v, c, infVer) :
  index = -1
  count = 0
  maximum = sys.maxsize * (-1)
  lstMax = []
  for i in range(len(v)):
    leftPart = 0
    for j in range(len(c)) :
      leftPart += c[j] * v[i][j]
    if leftPart > maximum :
      maximum = leftPart
      count = 1
      index = i
      lstMax = [v[i]]
    elif leftPart == maximum :
      count += 1
      index = i
      lstMax.append((v[i]))
  finalSol = []
  for k in lstMax:
    if k not in infVer :
      finalSol.append(k)
  return finalSol #(count, v[index])

def solve_diet_problem(n, m, A, b, c):
  vertices, infSol = GetVertices(n, m, A, b)
  vertices = CheckValidation(vertices, A, b)
  if len(vertices) == 0 :
    return -1, [0]
  bounded = FindMax(vertices, c, infSol)
  if len(bounded) == 1 :
    return 0, bounded[0]
  else :
    return 1, [0]

if __name__ == '__main__':
  (n ,m , A, b, c) = ReadData()

  anst, ansx = solve_diet_problem(n, m, A, b, c)

  if anst == -1:
    print("No solution")
  if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
  if anst == 1:
    print("Infinity")
    
