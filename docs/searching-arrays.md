# Searching arrays

NumPy's numpy.where() function is a powerful tool for conditionally selecting elements from an array or creating a new
array based on a given condition. It is used to perform element-wise conditional operations and is a fundamental part of
array masking and filtering.

The basic syntax of numpy.where() is as follows:

```python
numpy.where(condition, x, y)
```

- condition: The condition that acts as a filter for selecting elements from the input arrays x and y. It can be a
  boolean array or an expression that evaluates to a boolean array. When the condition is True, the corresponding
  elements from x are selected; otherwise, the elements from y are selected.
- x: The array-like object that provides the values to be chosen when the condition is True.
- y: The array-like object that provides the values to be chosen when the condition is False.

```python
import numpy as np

# Example 1: Element-wise conditional selection
arr = np.array([1, 5, 3, 8, 2, 7])
condition = arr > 3
result = np.where(condition, arr, 0)
print(result)
# Output: [0 5 0 8 0 7]

# Example 2: Creating a new array based on conditions
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])
condition = arr1 > 15
result = np.where(condition, arr1, arr2)
print(result)
# Output: [ 1  2 30 40]

# Example 3: Using numpy.where() for filtering
arr = np.array([1, 2, 3, 4, 5])
filtered_arr = arr[np.where(arr % 2 == 0)]
print(filtered_arr)
# Output: [2 4]
```







