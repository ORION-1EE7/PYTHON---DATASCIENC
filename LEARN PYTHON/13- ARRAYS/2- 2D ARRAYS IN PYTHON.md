# 2- 2D ARRAYS IN PYTHON

## 2D ARRAYS IN PYTHON

### WHAT IS A 2D ARRAY?

A 2D array is an array of arrays
It is organized as a matrix with rows and columns
Each element is accessed using two indices: the row index and the column index

### SYNTAX AND INITIALIZATION

```python
# 2D list with 2 rows and 4 columns
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

# Another 2D list with 3 rows and 4 columns
arr1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Sparse-style: pre-allocate with zeroes and assign row 5 manually
arr2 = [[0]*4 for _ in range(6)]
arr2[0] = [1, 2, 3, 4]
arr2[5] = [9, 10, 11, 12]

```

### EXAMPLE CODE

```python
def main():
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]

    print("Values from arr:")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(f"arr[{i}][{j}] = {arr[i][j]}")

    arr1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print("\nValues from arr1:")
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            print(f"arr1[{i}][{j}] = {arr1[i][j]}")

    arr2 = [[0]*4 for _ in range(6)]
    arr2[0] = [1, 2, 3, 4]
    arr2[5] = [9, 10, 11, 12]

    print("\nValues from arr2:")
    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            print(f"arr2[{i}][{j}] = {arr2[i][j]}")

if __name__ == "__main__":
    main()

```

---

Let me know if you'd like the **NumPy version** or how to render this in Markdown for GitHub.
