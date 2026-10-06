import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

df.loc[df["Price"] < 10, "Price"] = 10

print(df["Price"])
