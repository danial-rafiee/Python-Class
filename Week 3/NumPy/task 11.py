import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

mean = np.mean(a, axis=1, keepdims=True)

result = a - mean

print(result)
