import math
def sigmoid(x):
    out = []
    for i in range(len(x)):
        out.append(1/(1+ math.exp(-x[i])))
    return out