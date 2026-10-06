import numpy as np

a = np.random.random((5, 5))

min_value = a.min()
max_value = a.max()

normalized_a = (a - min_value) / (max_value - min_value)

print(normalized_a)
