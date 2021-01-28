# Big Wave Bay

import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x_num = [128722, 123297, 134047, 139017, 120068, 141320, 149270, 138610, 127750, 131590, 125730, 124260, 107760, 69900]
y_coil = [50, 17, 31, 46, 149, 17, 31, 21, 40, 21, 78, 36, 34, 103]

X = np.array(x_num, dtype=int)
Y = np.array(y_coil, dtype=int)

X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

reg = LinearRegression()
reg.fit(X, Y)
predictions = reg.predict(X)
plt.scatter(X, Y, c='black')
plt.plot(X, predictions, c='blue', linewidth=2)

X2 = sm.add_constant(X)
est = sm.OLS(Y, X2)
est2 = est.fit()
print(est2.summary())
plt.show()
