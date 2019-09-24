import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt


dates = []
prices = []

def get_data(filename):
    with open(filename , 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            date = row[0].split('-')
            dates.append(int(date[0] + date[1]))
            prices.append(float(row[1]))
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel="rbf", C=1e3, gamma = 0.1)

    svr_lin.fit(dates, prices)
    print('svr_lin fit done')
    svr_poly.fit(dates, prices)
    print('svr_poly fit done')
    svr_rbf.fit(dates, prices)
    print('svr_rbf fit done')

    plt.scatter(dates, prices, color = 'black', label='Data')
    plt.plot(dates, svr_lin.predict(dates), color = 'Red', label='Linear Model')
    print('svr_lin prediction done')
    plt.plot(dates, svr_poly.predict(dates), color = 'Green', label='Polynomial Model')
    print('svr_poly prediction done')
    plt.plot(dates, svr_rbf.predict(dates), color = 'Blue', label='RBF Model')
    print('svr_poly prediction done')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('SENSEX Prediction with SVRs')
    plt.legend()
    plt.show()

    return svr_lin.predict(x)[0], svr_poly.predict(x)[0], svr_rbf.predict(x)[0]


get_data('BSESN.csv')
print(dates)
print(prices)
predicted_price = predict_price(dates, prices, 2409)

print(predicted_price)
