# 5- LOGICAL OPERATORS

### LOGICAL OPERATORS:

Used to combine two or more conditions.

- `[and]` Checks if both conditions are true.
- `[or]` Checks if at least one of the conditions is true.
- `[not]` Checks if a condition is false.

### EXAMPLES:

```python
A = 5
B = 5
C = 10

# 1- AND (and)
result = (A == B) and (C > B)
print("(A == B) and (C > B):", result)  # True
result = (A == B) and (C < B)
print("(A == B) and (C < B):", result)  # False

# 2- OR (or)
result = (A == B) or (C > B)
print("(A == B) or (C > B):", result)  # True
result = (A != B) or (C > B)
print("(A != B) or (C > B):", result)  # True
result = (A != B) or (C < B)
print("(A != B) or (C < B):", result)  # False

# 3- NOT (not)
result = not (A == B)  # (A == B) = True => not(True) = False
print("not (A == B):", result)  # False
result = not (A != B)
print("not (A != B):", result)  # True

```
