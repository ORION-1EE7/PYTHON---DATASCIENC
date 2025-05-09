# 1- SETS IN PYTHON

### 1. **Definition**

- **Sets** are **unordered collections** of **unique elements**. They are **mutable**, but **do not allow duplicates**. Sets are useful for membership testing and removing duplicates.

### 2. **Creating a Set**

You can create a set using **curly braces `{}`** or the `set()` function.

### Syntax:

```python
# SYNTAX: my_set = {element1, element2, element3}
fruits = {"apple", "banana", "cherry"}

# OR using set() constructor
numbers = set([1, 2, 3, 3])
print(numbers)  # Output: {1, 2, 3}

```

### 3. **Accessing Elements**

- Sets do **not support indexing** because they are unordered.
- You can loop over them.

```python
for fruit in fruits:
    print(fruit)

```

### 4. **Set Length**

```python
print(len(fruits))  # Output: 3

```
