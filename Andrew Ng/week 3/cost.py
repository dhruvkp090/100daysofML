import numpy as np
import math
import sigmoid

def j(X,y, theta):
    h = sigmoid.sigmoid(X.dot(theta))
    sum = 0
    for i in range(len(h)):
        element = (y[i]*math.log(h[i])) + ((1-y[i])*math.log(1-h[i]))
        sum += element
    out = -1/(len(h))*sum

    return out