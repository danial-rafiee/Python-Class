import pandas as pd

dict1 = {
    "ID": [1, 2, 3],
    "Name": ["Ali", "Sara", "John"]
}

dict2 = {
    "ID": [1, 2, 3],
    "Age": [25, 30, 22]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

merged_df = pd.merge(df1, df2, on="ID")

print("\nMerged DataFrame:")
print(merged_df)

df1["Age"] = df2["Age"]

print("\nDataFrame with new column:")
print(df1)
