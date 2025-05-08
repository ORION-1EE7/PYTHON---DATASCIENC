# 4- SLICING 1D ARRAYS

You can access and extract parts of a 1D NumPy array using slicing. A 1D array is like a simple list of elements.

- The basic syntax is: array\[start\:end]
- The slice includes start index but excludes end index.

```python
import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50, 60])

# Slice elements from index 1 to 3 (excludes index 4)
sub_arr = arr[1:4]
print(sub_arr)  # Output: [20 30 40]

```

### 2- INDEXING A SINGLE ELEMENT

You can access a specific element by its index.

```python
print(arr[2])  # Output: 30

```

### 3- SLICING FROM THE START OR TO THE END

You can omit the start or end index to slice from the beginning or to the end.

```python
# From start to index 3 (not included)
print(arr[:4])  # Output: [10 20 30 40]

# From index 3 to the end
print(arr[3:])  # Output: [40 50 60]

```

### 4- NEGATIVE INDICES

You can use negative indices to count from the end of the array.

```python
# Last element
print(arr[-1])  # Output: 60

# Last three elements
print(arr[-3:])  # Output: [40 50 60]

```

### 5- STEP VALUE IN SLICING

You can use a third value in slicing: array\[start\:end\:step]

```python
# Every second element
print(arr[::2])  # Output: [10 30 50]

# Reverse the array
print(arr[::-1])  # Output: [60 50 40 30 20 10]

```
