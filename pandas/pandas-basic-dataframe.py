# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "duration22": [500, 400, 450]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
