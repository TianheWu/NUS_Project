import numpy as np
from scipy.optimize import leastsq
from pandas import read_csv, DataFrame
import matplotlib.pyplot as plt


def func(_x, _p):
    k1, c = _p
    return k1 / _x + c


def residuals(_p, _y, _x):
    return _y - func(_x, _p)


def power_fit(x, y):
    x = np.array(x)
    y = np.array(y)

    x_fig1 = np.arange(np.min(x), np.max(x), 1)
    result_fit1 = leastsq(residuals, [0, 0], args=(y, x))
    plt.plot(x_fig1, func(x_fig1, result_fit1[0]), label="fit_line", c='r')
    font = {'family': 'Times New Roman',
            'weight': 'normal',
            'size': 13}
    plt.xlabel('Visitors number', font)
    plt.ylabel('Water quality', font)
    plt.title('Power fit')
    plt.legend()
    plt.show()