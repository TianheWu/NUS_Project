from ReadFile.read import func_read
import pandas as pd


def func_transfer(x_F, y_F):
    table = []
    name = []
    xTable = x_F.drop('Year', 1)
    yTable = y_F.drop('Year', 1)
    for index, j in xTable.iteritems():
        table.append(list(xTable[index]))
        table.append(list(yTable[index]))
        name.append(index)

    return table, name


