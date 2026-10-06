import numpy as np

a = np.random.random(5) * 10

print("Original array:")
print(a)

# Method 1
print("Method 1:", a.astype(int))

# Method 2
print("Method 2:", np.floor(a))

# Method 3
print("Method 3:", np.trunc(a))

# Method 4
print("Method 4:", a - a % 1)

# Method 5
fractional_part, integer_part = np.modf(a)
print("Method 5:", integer_part)