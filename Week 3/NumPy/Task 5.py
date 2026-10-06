import numpy as np

today = np.datetime64('today', 'D')

yesterday = today - np.timedelta64(1, 'D')
tomorrow = today + np.timedelta64(1, 'D')

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

