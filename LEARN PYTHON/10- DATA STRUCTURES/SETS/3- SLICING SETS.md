# 3- SLICING SETS

❌ Not supported — sets are **unordered**, so slicing is **not possible**.

### **NESTED SETS**

Sets cannot contain other sets because they are unhashable, but they can contain **frozensets**.

```python
a = frozenset([1, 2])
b = {a, 3}
print(b)  # Output: {frozenset({1, 2}), 3}

```

### **SET COMPREHENSION**

Set comprehension is supported and useful for filtering/transforming data.

```python
squares = {x**2 for x in range(5)}
print(squares)  # Output: {0, 1, 4, 9, 16}

```
