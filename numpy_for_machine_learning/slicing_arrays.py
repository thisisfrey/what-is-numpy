import numpy as np

# Slicing Numpy Arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

np2 = np1[1:5]
# np2 is [2 3 4 5]
# starts at item at position 1 and ends before item at position 5

np3 = np1[3:]
# np3 is [4 5 6 7 8 9]
# return from starting position till the end

np4 = np1[-3]
# np4 is 7

np5 = np1[-3:-1]
# np5 is [7 8]
# 9 is item at position -1, not including -1-element!

np6 = np1[1:5:2]
# np6 is [2 4]
# step is 2

np7 = np1[::2]
# np7 is [1 3 5 7 9]

# Slice a 2d-array
np8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
el = np8[1][2]
# el is 8

# 0:1 is row, 1:3 is column
# np8 = np.array( [[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10]] )
np9 = np8[0:1, 1:3]
# np9 is [[2 3]]

np10 = np8[0:2, 1:3]
# np10 is array([[2, 3],
#                [7, 8]])
