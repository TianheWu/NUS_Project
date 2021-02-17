from ReadFile.read import func_read
from TransferData.transfer import func_transfer
from Fitting.linearFit import fitting
import matplotlib.pyplot as plt
from Draw.draw import func_draw
from Fitting.powerFit import power_fit


x, y = func_read()
table, name = func_transfer(x, y)
X = []
Y = []
name_i = 0
del_i = 0

for i in range(0, len(table) - 1, 2):
    table[i + 1].reverse()

    # del three abnormal point
    while name_i == 0 and del_i < 3:
        maxIndex = table[i + 1].index(max(table[i + 1]))
        table[i].remove(table[i][maxIndex])
        table[i + 1].remove(max(table[i + 1]))
        del_i += 1

    func_draw(table[i], table[i + 1], name[name_i])
    name_i += 1

    X.extend(table[i])
    Y.extend(table[i + 1])

fitting(X, Y)
# power_fit(X, Y)
plt.show()
