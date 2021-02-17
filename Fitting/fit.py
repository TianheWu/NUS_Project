import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression


def fitting(x_num, y_coil, name):

    X = np.array(x_num, dtype=int)
    Y = np.array(y_coil, dtype=int)

    X = X.reshape(-1, 1)
    Y = Y.reshape(-1, 1)

    reg = LinearRegression()
    reg.fit(X, Y)
    predictions = reg.predict(X)
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 13}
    plt.scatter(X, Y, c='orange')
    plt.plot(X, predictions, c='r', linewidth=2, label='fit_line')
    plt.xlabel('Visitors number', font)
    plt.ylabel('Water quality', font)
    plt.title(name, font)
    X2 = sm.add_constant(X)
    est = sm.OLS(Y, X2)
    est2 = est.fit()
    print(est2.summary())
    plt.legend()
    plt.show()
