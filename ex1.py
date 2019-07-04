import re
import matplotlib.pyplot as plt


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
plt.show()