# Introduction to NumPy

This document provides an overview of NumPy, a powerful library in Python for numerical computing. NumPy stands for "
Numeric Python" and is used extensively in scientific and data analysis applications due to its efficient handling of
multi-dimensional arrays and various mathematical functions.

## Table of Contents

1. [Introduction](#introduction)
2. [Basic NumPy Arrays](#basic-numpy-arrays)
    1. [Creating Arrays](#creating-arrays)
    2. [Array Shape](#array-shape)
    3. [Array Indexing](#array-indexing)
3. [Common NumPy Functions](#common-numpy-functions)
    1. [np.arange()](#arange)
    2. [np.zeros()](#zeros)
    3. [np.ones()](#ones)
    4. [np.full()](#full)
    5. [Multi-dimensional Arrays](#multi-dimensional-arrays)

## Introduction

NumPy is a foundational library for numerical computations in Python. It introduces a new data type called `ndarray` (
short for "N-dimensional array"), which is highly efficient and versatile for numerical operations. Importing NumPy is
typically done using the following convention:

```python
import numpy as np
```

## Basic NumPy Arrays

### Creating Arrays

NumPy arrays can be created using the np.array() function, which takes a Python list or tuple as input and returns a
NumPy array. For example:

```python
import numpy as np

# Create a NumPy array from a Python list
list1 = [1, 2, 3, 4, 5]
np1 = np.array(list1)
```

### Array Shape

NumPy arrays have a property called "shape," which represents the dimensions of the array. For a 1-dimensional array,
the shape is given as (length,). For example:

```python
import numpy as np

np1 = np.array([1, 2, 3, 4, 5])
length = np1.shape
# length is (5,)
```

### Array Indexing

Elements of a NumPy array can be accessed using indexing, similar to Python lists. The indexing is zero-based. For
example:

```python
import numpy as np

np9 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
el = np9[0]
# el is 1
```

## Common NumPy Functions

### np.arange()

The np.arange() function generates a sequence of numbers in a specified range. It is similar to the Python range()
function but returns a NumPy array.

```python
import numpy as np

np2 = np.arange(10)
# np2 is [0 1 2 3 4 5 6 7 8 9]

np3 = np.arange(0, 10, 2)
# np3 is [0 2 4 6 8]
```

### np.zeros()

The np.zeros() function creates an array filled with zeros.

```python
import numpy as np

np4 = np.zeros(10)
# np4 is [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

### np.ones()

The np.ones() function creates an array filled with ones.

```python
import numpy as np

np5 = np.ones(10)
# np5 is [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

### np.full()

The np.full() function creates an array with a specified shape, filled with a specified value.

```python
import numpy as np

np6 = np.full((10), 8)
# np6 is [8 8 8 8 8 8 8 8 8 8]
```

### Multi-dimensional Arrays

NumPy supports multi-dimensional arrays, commonly referred to as matrices. They can be created using the same functions
we've seen before, but with a tuple specifying the shape

```python
import numpy as np

# 2 dimensions, 5 items per dimension
np7 = np.ones((2, 5))
# np7 is [[1. 1. 1. 1. 1.]
#        [1. 1. 1. 1. 1.]]

# 2 dimensions, 10 elements per dimension, filled with 6s
np8 = np.full((2, 10), 6)
# np8 is [[6 6 6 6 6 6 6 6 6 6]
#        [6 6 6 6 6 6 6 6 6 6]]
```