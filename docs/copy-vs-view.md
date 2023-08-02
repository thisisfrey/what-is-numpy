# Copy vs View

This [code](../numpy_for_machine_learning/copy_vs_view.py) demonstrates the difference between creating a view and
making a copy of a Numpy array. Understanding this
difference is crucial when working with large datasets or when you want to avoid unintended changes to your original
data.

## View

Creating a view of a Numpy array provides a memory-efficient way to work with data, especially when dealing with large
datasets, as it shares the same data buffer with the original array. However, keep in mind that changes made to the view
will affect the original array as well.

```python
np1 = np.array([0,1,2,3,4,5])
np2 = np1.view()
```

## Copy

Creating a copy of a Numpy array ensures that the new array is independent and not linked to the
original array. Any modifications to the copied array will not impact the original data.

```python
np1 = np.array([0,1,2,3,4,5])
np3 = np1.copy()
```