# Slicing NumPy Arrays

NumPy's array slicing functionality allows for efficient manipulation and extraction of data from arrays. By
understanding how to use slicing with different indices and step values, you can easily extract the data you
need from arrays.

## 1D Array Slicing

### Basic Slicing

```python
import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

np2 = np1[1:5]
# np2 is [2 3 4 5]
# Starts at item at position 1 and ends before item at position 5

np3 = np1[3:]
# np3 is [4 5 6 7 8 9]
# Returns elements from the starting position till the end

np4 = np1[-3]
# np4 is 7
# Negative indices count from the end of the array

np5 = np1[-3:-1]
# np5 is [7 8]
# The element at position -1 is 9, but not included in the slice

np6 = np1[1:5:2]
# np6 is [2 4]
# Step is 2, meaning it skips every second element

np7 = np1[::2]
# np7 is [1 3 5 7 9]
# Starts from the beginning, goes to the end, and takes every second element
```

## 2D Array Slicing

### Basic Slicing

```python
import numpy as np

np8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

el = np8[1][2]
# el is 8
# Accessing a single element in a 2D array

# 0:1 is row, 1:3 is column
# np8 = np.array( [[1, 2, 3, 4, 5],
#                 [6, 7, 8, 9, 10]] )

np9 = np8[0:1, 1:3]
# np9 is [[2 3]]
# Slice rows 0 to 1 (exclusive), and columns 1 to 3 (exclusive)

np10 = np8[0:2, 1:3]
# np10 is array([[2, 3],
#                [7, 8]])
# Slice rows 0 to 2 (exclusive), and columns 1 to 3 (exclusive)
```
