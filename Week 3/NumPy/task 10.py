import numpy as np

a = np.random.random((100, 2))

difference = a[1:] - a[:-1]

distances = np.sqrt(np.sum(difference**2, axis=1))

print(distances)
