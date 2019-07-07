import re
import matplotlib.pyplot as plt
import numpy as np
import cost
import gradient


x = []
y = []
file = open('ex1data1.txt', 'r')
for line in file:
    line = line.replace('\n', '')
    line_values = line.split(',')
    x.append(float(line_values[0])) #Population
    y.append(float(line_values[1])) #Profit

m = len(y)
plt.scatter(x, y, c='red', alpha=0.5)
plt.title('Scatter plot of training data')
plt.xlabel('Population of City in 10,000s')
plt.ylabel('Profit in $10,000s')

X = np.c_[np.ones((m,1)), x]
theta = np.zeros((2,1))
iterations = 1500
alpha = 0.01
J = cost.j(X, y, [-1 , 2])
theta = gradient.gradientD(X, y, theta, alpha, iterations)
J = cost.j(X, y, theta)
plt.plot(x, X.dot(theta), 'k-', lw=2)
plt.show()
predict1 = np.array([1,3.5]).dot(theta)
predict2 = np.array([1,7]).dot(theta)
print("*************PREDICTIONS***********************")
print("Population of 35,000: " + str(predict1))
print("Population of 70,000: " + str(predict2))
