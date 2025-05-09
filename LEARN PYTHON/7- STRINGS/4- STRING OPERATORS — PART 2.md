# 4- STRING OPERATORS — PART 2

### I- STRING COMPARISON OPERATORS

String comparison operators are used to compare two strings.

### 1- POINTS TO REMEMBER:

- Comparisons are case-sensitive.
  - Example: `'A'` is not the same as `'a'`.
- Each character has an ASCII value, and characters are compared by their ASCII values.
  - Example: ASCII of `'A' = 65`, ASCII of `'a' = 97` → `'A' < 'a'`.

### 2- THE `<` OPERATOR

- Returns `True` if the first string is smaller than the second string; otherwise, it returns `False`.

### 3- THE `<=` OPERATOR

- Returns `True` if the first string is smaller than or equal to the second string; otherwise, it returns `False`.

### 4- THE `>` OPERATOR

- Returns `True` if the first string is greater than the second string; otherwise, it returns `False`.

### 5- THE `>=` OPERATOR

- Returns `True` if the first string is greater than or equal to the second string; otherwise, it returns `False`.

### STRING COMPARISON EXAMPLES:

```python
a = "Apple"
b = "Banana"
c = "cat"
d = "dog"
e = "Goat"
f = "goat"

# POINT: ASCII of first characters
print("ASCII of 'A':", ord('A'))  # 65
print("ASCII of 'a':", ord('a'))  # 97
print()

# < Operator
print("Apple < Banana:", a < b)     # True

# <= Operator
print("cat <= dog:", c <= d)        # True
print("dog <= cat:", d <= c)        # False

# > Operator
print("dog > cat:", d > c)          # True
print("Apple > Banana:", a > b)     # False

# >= Operator
print("Goat >= goat:", e >= f)      # False
print("Goat >= Goat:", e >= e)      # True

```
