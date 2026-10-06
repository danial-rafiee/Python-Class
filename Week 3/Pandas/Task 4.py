import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

print("Column names:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())
