import pandas as pd

df = pd.read_csv("Cars93_missing.csv")


def exchange_columns(dataframe, column1, column2):
    columns = list(dataframe.columns)

    index1 = columns.index(column1)
    index2 = columns.index(column2)

    columns[index1], columns[index2] = columns[index2], columns[index1]

    return dataframe[columns]


df = exchange_columns(df, "Manufacturer", "Model")

print("After exchanging columns:")
print(df.head())

df = df.reindex(sorted(df.columns), axis=1)

print("\nAfter sorting columns:")
print(df.head())
