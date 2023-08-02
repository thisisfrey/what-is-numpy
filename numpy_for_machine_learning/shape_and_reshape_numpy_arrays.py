import numpy as np

# Create 1D Numpy Array and Get Shapes
np1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
s1 = np1.shape
# s1 is (12,)

# Create 2D Array and get Shape (rows, columns)
np2 = np.array([[1,2,3], [4,5,6]])
s2 = np2.shape
# s2 is (2,3) => 2 rows, 3 columns => 2x3 Matrix

# Reshape 2D
np3 = np1.reshape(3,4) # => 3 rows, 4 columns

# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

s3 = np3.shape
# s3 is (3, 4)

# Reshape 3D
np4 = np1.reshape(3,2,2)
s4 = np4.shape
"""
array([[[ 1,  2],
        [ 3,  4]],

       [[ 5,  6],
        [ 7,  8]],

       [[ 9, 10],
        [11, 12]]])

shape is (3, 2, 2)
# 3D is x-y-z
"""

# Flatten to 1D
np5 = np4.reshape(-1)
# Why?? 3D => 1D
# np5 is [ 1  2  3  4  5  6  7  8  9 10 11 12]


