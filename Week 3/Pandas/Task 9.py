import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cars93_missing.csv")

df["Price"].hist()

plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Price Histogram")

plt.show()
