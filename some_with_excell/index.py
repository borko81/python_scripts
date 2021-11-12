import pandas as pd

file = 'january.xlsx'

data = []
df = pd.read_excel(file, skiprows=1, usecols='A')

data.append(df)

d = pd.concat(data)
print(d)
