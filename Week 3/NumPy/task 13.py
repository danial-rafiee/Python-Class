import numpy as np

a = np.array([
    [1, 2],
    [2, 4]
])

rank = np.linalg.matrix_rank(a)

print("Rank:", rank)
