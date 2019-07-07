def gradientD(X, y, theta, alpha, iterations):
    sum = 0
    for i in range(iterations):
        sum = 0
        h = X.dot(theta)
        for i in range(len(h)):
            diff = (h[i] - y[i])*X[i][0]
            sum += diff
        temp1 = theta[0] - alpha*(1/len(h))*sum
        sum = 0
        h = X.dot(theta)
        for i in range(len(h)):
            diff = (h[i] - y[i])*X[i][1]
            sum += diff
        temp2 = theta[1] - alpha*(1/len(h))*sum
        theta[0] = temp1
        theta[1] = temp2
    return theta