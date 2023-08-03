import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

x = np.where(np1 == 3)
# x is (array([2], dtype=int64),)
# 3 is at index 2 in np3

np2 = np.array([1, 5, 3, 6, 3])
y = np.where(np2 == 3)
# y is array([2, 4], dtype=int64),)
np3 = np2[y[0]]
# np3 is array([3, 3])

# Return even items
even = np.where(np1 % 2 == 0)
# even[0] is [1 3 5 7 9]

# Return odd items
odd = np.where(np1 % 2 == 1)
# odd[0] is [0 2 4 6 8]
