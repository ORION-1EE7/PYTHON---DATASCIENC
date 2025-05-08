# 1- TUPLES IN PYTHON

### 1. **Definition**

- **Tuples** are **ordered, immutable collections** of elements. Once a tuple is created, its contents **cannot be changed**. They can contain elements of different types.

### 2. **Creating a Tuple**

You can create a tuple by enclosing elements in **parentheses `()`**.

### Syntax:

```python
# SYNTAX: my_tuple = (element1, element2, element3)
coordinates = (10, 20, 30)

```

### 3. **Accessing Elements**

- Elements are accessed using **indexing**, starting from `0`. Negative indexing also works.

```python
# SYNTAX:
my_tuple[index]

# EXAMPLES:
print(coordinates[0])  # Output: 10
print(coordinates[-1])  # Output: 30

```

### 4. **Tuple Length**

Use `len()` to find how many elements are in the tuple.

```python
print(len(coordinates))  # Output: 3

```
