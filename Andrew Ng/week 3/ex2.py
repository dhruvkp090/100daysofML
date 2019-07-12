import re
import matplotlib.pyplot as plt
import numpy as np
import sigmoid
import cost


x1 = []
x2 = []
y = []
file = open('ex2data1.txt', 'r')
for line in file:
    line = line.replace('\n', '')
    line_values = line.split(',')
    x1.append(float(line_values[0])) #Score 1
    x2.append(float(line_values[1])) #Score 2
    y.append(int(line_values[2])) #Got in or not

pos1 = []
neg1 = []
pos2 = []
neg2 = []
m = len(y)
for i in range(m):
    if y[i] == 1:
        pos1.append(x1[i])
        pos2.append(x2[i])
    elif y[i] == 0:
        neg1.append(x1[i])
        neg2.append(x2[i])

plt.scatter(pos1, pos2, c='red', alpha=0.5)
plt.scatter(neg1, neg2, c='blue', alpha=0.5)
plt.title('Scatter plot of training data')
plt.xlabel('Exam 1 Score')
plt.ylabel('Exam 2 Score')
#plt.show()
#print(sigmoid.sigmoid(np.array([[1,2],[3,4]])))
X = np.c_[np.ones((m,1)),x1, x2]
y = np.array(y)
theta = np.zeros((3,1))
J = cost.cost(X, y, theta)
theta1 = cost.gradient(theta,X,y)
theta = [-25.16131856, 0.20623159, 0.20147149]
x_values = [np.min(X[:, 1] - 5), np.max(X[:, 2] + 5)]
y_values = - (theta[0] + np.dot(theta[1], x_values)) / theta[2]

plt.plot(x_values, y_values, label='Decision Boundary')
plt.xlabel('Marks in 1st Exam')
plt.ylabel('Marks in 2nd Exam')
plt.legend()
plt.show()
#plt.show()
