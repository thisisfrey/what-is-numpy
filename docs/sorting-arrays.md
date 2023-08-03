# Sorting Arrays

## Numerical Sorting

NumPy provides the numpy.sort() function to sort arrays in ascending order. Numerical sorting is used to sort arrays
containing numeric data. By default, NumPy sorts the array in ascending order.
Here's an example:

```python
import numpy as np

# Numerical sorting
numeric_array = np.array([5, 2, 9, 1, 7])
sorted_numeric_array = np.sort(numeric_array)
print(sorted_numeric_array)  # Output: [1 2 5 7 9]
```

Sorting multi-dimensional arrays along specific axes:

```python
# Multi-dimensional numerical sorting
multi_dim_array = np.array([[5, 2], [9, 1], [7, 3]])
sorted_multi_dim_array = np.sort(multi_dim_array, axis=0)
print(sorted_multi_dim_array)
# Output: [[5 1]
#          [7 2]
#          [9 3]]
```

## Alphabetical Sorting:

Alphabetical sorting is used for arrays containing strings. By default, it sorts strings lexicographically:

```python
# Alphabetical sorting
string_array = np.array(['apple', 'banana', 'orange', 'grape'])
sorted_string_array = np.sort(string_array)
print(sorted_string_array)  # Output: ['apple' 'banana' 'grape' 'orange']

```

## Boolean Sorting

Boolean sorting is useful when you want to sort based on a mask or a condition. You can use the numpy.argsort() function
to get the indices that would sort the array, which can then be used to rearrange the elements:

```python
# Boolean sorting
boolean_array = np.array([True, False, True, False])
sorted_indices = np.argsort(boolean_array)
sorted_boolean_array = boolean_array[sorted_indices]
print(sorted_boolean_array)  # Output: [False False True True]
```

You can also use boolean sorting with numeric or string data. For instance, sorting an array based on a specific
condition.

NumPy's sorting functions are efficient and versatile, making them essential tools for data manipulation and analysis in
scientific computing and data science tasks.