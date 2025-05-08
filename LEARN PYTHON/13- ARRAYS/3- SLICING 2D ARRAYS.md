# 3- SLICING 2D ARRAYS

You can access and extract specific parts of a NumPy 2D array using slicing. Slicing lets you select subregions of arrays using row and column indices.

- A 2D array is structured like a matrix: rows × columns.
- The basic syntax is: array\[row\_start\:row\_end, col\_start\:col\_end]

```python
import numpy as np

# Create a 2D array (3 rows × 4 columns)
arr = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

# Slice the top-left 2x2 part
sub_arr = arr[0:2, 0:2]
print(sub_arr)
# Output:
# [[10 20]
#  [50 60]]

# Slice the last two columns of all rows
last_cols = arr[:, 2:4]
print(last_cols)
# Output:
# [[ 30  40]
#  [ 70  80]
#  [110 120]]

```

### 2- INDEXING A SINGLE ELEMENT

You can access a single element by specifying its row and column index.

```python
print(arr[1, 2])  # Output: 70

```

### 3- SLICING ENTIRE ROWS OR COLUMNS

- Use `:` to mean "all" rows or columns.

```python
# Get the first row
print(arr[0, :])  # Output: [10 20 30 40]

# Get the third column
print(arr[:, 2])  # Output: [30 70 110]

```

### 4- NEGATIVE INDICES

You can use negative indices to count from the end of the array.

```python
# Last row
print(arr[-1, :])  # Output: [90 100 110 120]

# Last column
print(arr[:, -1])  # Output: [40 80 120]

```
