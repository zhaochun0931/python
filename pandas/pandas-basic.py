import pandas as pd


# A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

xx = [1,2,3]

zz = pd.Series(xx)

print(zz)




xx = range(100)

zz = pd.Series(xx)

print(zz)



# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "duration22": [500, 400, 450]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
