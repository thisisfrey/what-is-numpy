import numpy as np

# 1d array
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

for x in np1:
    print(x)

# 2d array
np2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np2:
    print(x)
# prints array rows
# [1 2 3 4]
# [5 6 7 8]

# print elements in 2d arrays
# for embedded loops
for x in np2:
    for y in x:
        print(y)

# 3d array (x-,y-,z-dimension)
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np3:
    print(x)
# [[1 2 3]
#  [4 5 6]]

# [[ 7  8  9]
#  [10 11 12]]

for x in np3:
    for y in x:
        for z in y:
            print(z)


# Use np.nditer() to print elements of 3d array
for z in np.nditer(np3):
    print(z)
