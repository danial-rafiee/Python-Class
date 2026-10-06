import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

series = df["Manufacturer"]

df.index = series

print(df)
