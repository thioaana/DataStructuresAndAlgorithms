# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # value = 0.
    # valPerWeight = [int(v) / int(w) for v, w in zip(values, weights)]
    # valPerWeight.sort(reverse = True)
    # return capacity * valPerWeight[0]
    valPerWeight = [[int(v) / int(w), w, v] for v, w in zip(values, weights)]
    valPerWeight.sort(reverse=True)
    A = [0 for i in range(len(values))]
    V = 0
    for i in range(len(values)) :
        if capacity == 0 : return V
        for vPW in range(len(valPerWeight)) :
            if valPerWeight[vPW][1] > 0 :
                key = vPW
                break
        a = min(valPerWeight[key][1], capacity)
        V += a * valPerWeight[key][2] / valPerWeight[key][1]
        valPerWeight[key][1] -= a
        capacity -= a
    return V

if __name__ == "__main__":
    l1 = input().split()
    n = int(l1[0])
    capacity  = int(l1[1])
    values = []
    weights = []
    for i in range(n) :
        l = input().split()
        values.append(int(l[0]))
        weights.append(int(l[1]))
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
