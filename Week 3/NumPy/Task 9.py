import numpy as np

A = np.random.random(5)
B = np.random.random(5)

print("A:", A)
print("B:", B)

result = np.array_equal(A, B)

print("Are A and B equal?", result)
