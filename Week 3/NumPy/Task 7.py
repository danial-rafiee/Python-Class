import numpy as np

dtype = [
    ('position', [('x', float), ('y', float)]),
    ('color', [('r', int), ('g', int), ('b', int)])
]

a = np.zeros(3, dtype=dtype)

a[0]['position']['x'] = 10
a[0]['position']['y'] = 20
a[0]['color']['r'] = 255
a[0]['color']['g'] = 100
a[0]['color']['b'] = 50

a[1]['position']['x'] = 30
a[1]['position']['y'] = 40
a[1]['color']['r'] = 100
a[1]['color']['g'] = 200
a[1]['color']['b'] = 50

a[2]['position']['x'] = 50
a[2]['position']['y'] = 60
a[2]['color']['r'] = 50
a[2]['color']['g'] = 100
a[2]['color']['b'] = 255

print(a)