import numpy as np

a = np.arange(256).reshape(16, 16)

blocks = a.reshape(4, 4, 4, 4)

result = blocks.sum(axis=(1, 3))

print(result)
