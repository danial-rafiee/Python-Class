import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

lower = df["Price"].quantile(0.05)
upper = df["Price"].quantile(0.95)

df = df[
    (df["Price"] >= lower) &
    (df["Price"] <= upper)
]

print(df)
