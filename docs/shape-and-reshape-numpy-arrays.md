# Shape and Reshape NumPy Arrays

This [code](../numpy_for_machine_learning/shape_and_reshape_numpy_arrays.py) demonstrates the creation of 1D and 2D
Numpy arrays and explores various reshaping techniques available in
Numpy. Understanding the concept of shapes and reshaping is essential for working with multi-dimensional arrays and
manipulating data efficiently.

## Shape of an Array

In this example, we create a 2D Numpy array arr with 2 rows and 3 columns. The shape of this array is (2, 3), indicating
that it has 2 rows and 3 columns.

```python
import numpy as np

# Create a 2D Numpy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Get the shape of the array
shape = arr.shape

# Output
# shape is (2, 3)
```

## Reshape of an Array

Reshaping an array allows us to change its dimensions while maintaining the total number of elements. The .reshape()
method in Numpy enables us to modify the shape of an array.

```python
import numpy as np

# Create a 1D Numpy array
arr1d = np.array([1, 2, 3, 4, 5, 6])

# Reshape the 1D array to a 2D array
arr2d = arr1d.reshape(2, 3)

# Output
# arr2d is
# array([[1, 2, 3],
#        [4, 5, 6]])
```

### Example: Reshape a 1D Array to 3D Array

```
import numpy as np

# Create a 1D Numpy array
arr1d = np.array([1, 2, 3, 4, 5, 6])

# Reshape the 1D array to a 3D array
arr3d = arr1d.reshape(2, 1, 3)

# Output
# arr3d is
# array([[[1, 2, 3]],
#        [[4, 5, 6]]])
```

## Flattening a Multi-Dimensional Array

We can also flatten a multi-dimensional array back to a 1D array using the .reshape(-1) method.

```python
import numpy as np

# Create a 2D Numpy array
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

# Flatten the 2D array to a 1D array
arr1d = arr2d.reshape(-1)

# Output
# arr1d is [1 2 3 4 5 6]
```

In this example, we start with a 2D Numpy array arr2d with 2 rows and 3 columns. We then use the .reshape(-1) method to
flatten it back to a 1D array arr1d with all the elements in a single row. The order of elements remains the same as in
the original 2D array.