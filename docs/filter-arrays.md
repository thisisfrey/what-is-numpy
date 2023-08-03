# Filter arrays

In NumPy, you can filter arrays using boolean indexing or conditional statements. Here are a few common ways to filter
NumPy arrays:

## Boolean Indexing

Boolean indexing allows you to filter elements in an array based on a given condition, resulting in a new array
containing only the elements that satisfy the condition.

```python
import numpy as np

# Sample array
arr = np.array([1, 5, 10, 15, 20])

# Filter elements greater than 10
filtered_arr = arr[arr > 10]

print(filtered_arr)  # Output: [15, 20]
```

## Conditional Statements

You can use conditional statements to create a mask that will be used to filter the array.

```python
import numpy as np

# Sample array
arr = np.array([1, 5, 10, 15, 20])

# Create a mask for elements greater than 10
mask = arr > 10

# Apply the mask to the array
filtered_arr = arr[mask]

print(filtered_arr)  # Output: [15, 20]
```

## Multiple Conditions

You can use logical operators (like & for AND, | for OR) to apply multiple conditions.

```python
import numpy as np

# Sample array
arr = np.array([1, 5, 10, 15, 20])

# Create a mask for elements greater than 5 and less than 20
mask = (arr > 5) & (arr < 20)

# Apply the mask to the array
filtered_arr = arr[mask]

print(filtered_arr)  # Output: [10, 15]
```

These methods can be applied to NumPy arrays of any dimensions. Remember that the result will be a new array containing
the filtered elements, and the original array remains unchanged.