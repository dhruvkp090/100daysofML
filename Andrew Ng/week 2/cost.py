import numpy as np
import math
def j(X, y, theta):
    h = X.dot(theta)
    sum = 0
    for i in range(len(h)):
        diff = h[i] - y[i]
        diff = (diff)**2
        sum += diff
    out = 1/(2*len(h))*sum
    return out