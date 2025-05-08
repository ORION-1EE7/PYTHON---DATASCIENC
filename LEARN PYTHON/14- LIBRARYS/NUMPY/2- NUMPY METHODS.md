# 2- NUMPY METHODS

### ARRAY CREATION:

You can create NumPy arrays using methods like np.array(), np.zeros(), np.ones(), np.arange(), and np.linspace().

- **`np.array()**` creates an array from a Python list or list of lists.
- **`np.zeros()`** creates an array filled with zeros.
- **`np.ones()`** creates an array filled with ones.
- **`np.arange()`** creates an array with evenly spaced values (like range()).
- **`np.linspace()**` creates an array with a specific number of evenly spaced values between two points.

```python
import numpy as np

a = np.array([1, 2, 3])
print(a)  # Output: [1 2 3]

b = np.zeros((2, 3))
print(b)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]

c = np.ones((2, 2))
print(c)
# Output:
# [[1. 1.]
#  [1. 1.]]

d = np.arange(0, 10, 2)
print(d)  # Output: [0 2 4 6 8]

e = np.linspace(0, 1, 5)
print(e)  # Output: [0.   0.25 0.5  0.75 1.  ]

```

### ARRAY SHAPE & RESHAPING

You can inspect or change the shape of an array using `.shape`, `.reshape()`, and `.ravel()`.

- **`.shape**` shows the current shape of the array.
- **`.reshape()`** returns a reshaped version of the array.
- **`.ravel()`** flattens a multi-dimensional array into 1D.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # Output: (2, 3)

reshaped = arr.reshape(3, 2)
print(reshaped)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

flattened = arr.ravel()
print(flattened)  # Output: [1 2 3 4 5 6]

```
