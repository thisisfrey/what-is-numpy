import numpy as np

# python list
list1 = [1, 2, 3, 4, 5]
# print(list1)
# print(list1[0])

# python lists can have different data types
list2 = ["John Elder", 123, list1, True]
# print(list2)

# NumPy - Numeric Python
np1 = np.array([1, 2, 3, 4, 5])
# np1 = [ [1, 2, 3, 4, 5] ]
# type(np1) is <class 'numpy.ndarray'>

# shape
length = np1.shape
# length is ((5,))

# arange
np2 = np.arange(10)
# np2 = [0 1 2 3 4 5 6 7 8 9]

# arange with step
np3 = np.arange(0, 10, 2)
# [0 2 4 6 8]

# zeros
np4 = np.zeros(10)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# ones
np5 = np.ones(10)
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# full
np6 = np.full((10), 8)
# [8 8 8 8 8 8 8 8 8 8]

# multidimensional ones
# 2 dimensions, 5 items per dimension
np7 = np.ones((2, 5))
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# multidimensional full
# 2 dimensions, 10 elements per dimension, filled with 6s
np8 = np.full((2, 10), 6)
# [[6 6 6 6 6 6 6 6 6 6]
#  [6 6 6 6 6 6 6 6 6 6]]

# convert python lists to numpy
py_list = [1, 2, 3, 4, 5, 6, 7, 8]
np9 = np.array(py_list)

# access specific elements
el = np9[0]
# el is 1
