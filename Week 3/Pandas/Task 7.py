import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

average = df["Price"].mean()

df["Price"] = df["Price"].fillna(average)

print(df["Price"])
