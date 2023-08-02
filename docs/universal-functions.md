# Universal Functions

In this code, we demonstrate various mathematical operations that can be performed on Numpy arrays. Numpy is a powerful
library for numerical computing, and it provides a wide range of mathematical functions to operate on arrays
efficiently.

## Square Root

``` python

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np2 = np.sqrt(np1)
```

In this example, we calculate the square root of each element in the Numpy array np1 using np.sqrt(). The result is
stored in np2.

## Absolute Value

``` python

np3 = np.array([-3, -5, 4, 6])
np4 = np.absolute(np3)
```

Here, we compute the absolute value of each element in the Numpy array np3 using np.absolute(). The result is stored in
np4.

## Exponents

``` python
np5 = np.exp(np1)
```

This code calculates the exponential value of each element in the Numpy array np1 using np.exp(). The result is stored
in np5.

## Min / Max

``` python
min_val = np.min(np1) # returns 0
max_val = np.max(np1) # returns 9
```

In this part of the code, we find the minimum and maximum values in the Numpy array np1 using np.min() and np.max()
functions, respectively.

## Sign

``` python
signs = np.sign(np3)
```

This line of code calculates the sign of each element in the Numpy array np3 using np.sign(). The result is stored in
signs, where each element will be -1 if negative, 0 if zero, and 1 if positive.

## Trigonometric Functions and Logarithm

``` python
a = np.sin(np3)
b = np.log(np3)
```

These lines demonstrate trigonometric functions and logarithms. We compute the sine of each element in the Numpy array
`np3` using `np.sin()` and store the result in `a`. The logarithm of each element in `np3` is computed using `np.log()`
and stored
in `b`.

Note that the `np.log()` function returns `nan` (Not a Number) for negative values since the logarithm of negative
numbers
is undefined.

## Conclusion

Numpy's mathematical functions enable efficient and vectorized operations on arrays, making it an essential tool for
numerical computation and data processing. With Numpy, you can perform complex mathematical operations on arrays
effortlessly and leverage the speed and performance optimizations provided by the library.