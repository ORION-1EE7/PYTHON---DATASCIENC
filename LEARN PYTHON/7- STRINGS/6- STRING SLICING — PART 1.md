# 6- STRING SLICING — PART 1

### I- STRING SLICING

- A technique used to access a substring of a string.

### Example:

```python
S = "I AM MTALEB"
print("S[0:8] =", S[0:8])  # 'I AM MTA'

```

### II- SLICING WITH THE THIRD PARAMETER

- Also called the step value (by default, it is 1).
- The step value specifies the number of elements to skip when slicing the string.

### Example:

```python
S = "HELLO WORLD"
print("S[0:10:2] =", S[0:10:2])  # 'HLOWRD'

```

### III- ELIMINATING PARAMETERS IN SLICING

- Eliminating the first and/or second parameters is allowed.

### Example:

```python
S = "PYTHON"
print("S[:4] =", S[:4])  # 'PYTH'
print("S[2:] =", S[2:])  # 'THON'
print("S[:] =", S[:])    # 'PYTHON'
print("S[::2] =", S[::2])  # 'PTO'
print("S[::-1] =", S[::-1])  # 'NOHTYP'

```
