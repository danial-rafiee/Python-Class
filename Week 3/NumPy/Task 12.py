import numpy as np

a = np.array([
    [5, 2, 8],
    [1, 7, 3],
    [4, 1, 6]
])

indices = np.argsort(a[:, 1])

sorted_a = a[indices]

print(sorted_a)
