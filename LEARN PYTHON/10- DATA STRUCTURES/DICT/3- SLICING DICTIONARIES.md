# 3- SLICING DICTIONARIES

❌ Not directly supported — you can use tools like `dict.items()` with slicing indirectly.

```python
info = {"a": 1, "b": 2, "c": 3}
partial = dict(list(info.items())[:2])
print(partial)  # Output: {'a': 1, 'b': 2}

```

### **NESTED DICTIONARIES**

Dictionaries can contain other dictionaries or lists.

```python
student = {
    "name": "Alice",
    "grades": {"math": 90, "science": 95}
}

print(student["grades"]["science"])  # Output: 95

```

### **DICTIONARY COMPREHENSION**

You can create dictionaries using comprehension.

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

```
