# 1

## DICTIONARIES IN PYTHON

### 1. **Definition**

- **Dictionaries** are **unordered collections** of **key-value pairs**. Each key is **unique**. Dictionaries are **mutable**.

### 2. **Creating a Dictionary**

Use **curly braces `{}`** with key-value pairs separated by colons `:`.

### Syntax:

```python
# SYNTAX: my_dict = {key1: value1, key2: value2}
person = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}
```

### 3. **Accessing Elements**

Access values using the key.

```python
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 25
```

### 4. **Dictionary Length**

```python
print(len(person))  # Output: 3
```