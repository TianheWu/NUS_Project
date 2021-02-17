from ReadFile.read import func_read
from TransferData.transfer import func_transfer
from Fitting.fit import fitting


x, y = func_read()
table, name = func_transfer(x, y)
name_i = 0

for i in range(0, len(table) - 1, 2):
    table[i + 1].reverse()
    fitting(table[i], table[i + 1], name[name_i])
    name_i += 1
