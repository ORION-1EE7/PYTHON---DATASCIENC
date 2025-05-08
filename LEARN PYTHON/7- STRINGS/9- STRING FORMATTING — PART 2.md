# 9- STRING FORMATTING — PART 2

### I - f-strings

- Used to format a string in a clean and readable way.
- **SYNTAX:** `f"string {expression}"`
- Allows embedding Python expressions inside string literals.
- Introduced in Python 3.6.

### Examples:

```python
# Example:
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

```

**Output:**

```
My name is Alice and I am 30 years old.

```

```python
print(f"Next year, I’ll be {age + 1}.")

```

**Output:**

```
Next year, I’ll be 31.

```

```python
print(f"My name in uppercase is {name.upper()}.")

```

**Output:**

```
My name in uppercase is ALICE.
```
