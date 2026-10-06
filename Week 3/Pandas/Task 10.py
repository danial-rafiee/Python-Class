import pandas as pd

df = pd.read_csv("Cars93_missing.csv")

columns = ["Price", "Horsepower", "MPG.city"]

correlation_matrix = df[columns].corr()

print(correlation_matrix)