# 1- ARRAYS IN PYTHON (LISTS)

### 💡 WHAT'S A LIST (PYTHON'S VERSION OF AN ARRAY)?

- In Python, **lists** are used as dynamic arrays.
- A **list** is an **ordered collection** of items that can store elements of different types (though typically the same type is used).
- Unlike C arrays, Python lists can **grow or shrink dynamically**, and indexing starts at `0`.

### SYNTAX:

```python
# Create a list with fixed elements
arr = [1, 2, 3, 4, 5]

# You can also initialize an empty list and append values later
arr = []

# Partial initialization (rest filled dynamically or set to None/0 as needed)
arr = [1, 2] + [0] * 3  # [1, 2, 0, 0, 0]

# Explicit size initialization (e.g., default to zero)
arr = [0] * 5  # [0, 0, 0, 0, 0]

# Setting a value at a specific index manually
arr = [1, 2, 0, 0, 3]  # manually set index 4 to 3

```

### WITHOUT LISTS (Verbose)

```python
note1 = 3
note2 = 10
note3 = 12
note4 = 33

print(f"note1: {note1} / note2: {note2} / note3: {note3} / note4: {note4}")

note1 += 1
note2 += 1
note3 += 1
note4 += 1

```

### ✅ WITH LISTS

```python
arr = [3, 10, 12, 33]

for i in range(len(arr)):
    print(f"arr{i+1}: {arr[i]}")
    arr[i] += 1  # increase each element by 1

```
