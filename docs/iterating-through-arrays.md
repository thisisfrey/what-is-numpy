# Iterating through Arrays

## Iterate through 1-D Array

A 1D Numpy array np1 is created containing integers from 1 to 9. The script iterates through the elements of the 1D
array np1 and prints each element on a separate line.

````python
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
for x in np1:
    print(x)
````

## Iterate through 2-D Array

A 2D Numpy array np2 is created with two rows and four columns.

### Iterate through Rows of the 2D Array

The code iterates through the rows of the 2D array np2
and prints each row on a separate line.

````python
np2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np2:
    print(x)
````

### Print Elements of the 2D Array Using Nested Loops

````python
np2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np2:
    for y in x:
        print(y)
````

## Iterate through N-D Array

Create a 3D Numpy Array:

````python
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
````

### Iterate through Matrices (2D Arrays) of the 3D Array

````python
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np3:
    print(x)
````

### Print Elements of the 3D Array Using Triple Nested Loops

````python
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np3:
    for y in x:
        for z in y:
            print(z)

````

## The `np.nditer()`-function

The `np.nditer()`-function is used to efficiently iterate through all the elements of the 3D array np3, regardless of
its
shape. It flattens the array and allows us to iterate through all elements seamlessly.

````python
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for z in np.nditer(np3):
    print(z)
````