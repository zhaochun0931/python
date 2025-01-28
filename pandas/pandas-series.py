import pandas as pd


# A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

xx = [1,2,3]

zz = pd.Series(xx)

print(zz)




xx = range(100)

zz = pd.Series(xx)

print(zz)
