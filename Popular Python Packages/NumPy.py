import numpy as np

# array = np.zeroes((3, 4), dtype=int)
# array = np.ones((3, 4), dtype=int)
# array = np.full((3, 4), dtype=int)
# array = np.random.random((3, 4))
# print(array[0, 0])
# print(array > 0.2)
# print(array[array > 0.2])
# print(np.round(array))

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)

dimensions_inch = [1, 2, 3]
dimensions_cm = [x * 2.54 for x in dimensions_inch]
