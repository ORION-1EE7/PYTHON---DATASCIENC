# 7

## STRING SLICING — PART 2

### I- NEGATIVE THIRD PARAMETER

- A negative third parameter means the slicing moves backward (right to left).
- It is used to extract characters in reverse order.
- The start index should be greater than the end index.

### Example:

```python
S = "PYTHON"
print("S[5:1:-1] =", S[5:1:-1])  # 'NOHT'
print("S[4:0:-2] =", S[4:0:-2])  # 'TO'

```

### Diagram:

```
Index:   0   1   2   3   4   5
         P   Y   T   H   O   N
        -6  -5  -4  -3  -2  -1

S[5:1:-1] → from 'N' to after 'Y', step -1
S[4:0:-2] → 'O' (4), skip to 'T' (2)

```

### II- REVERSED STRING

- A common use of negative slicing is to reverse the entire string.
- This is done using \[::-1].

### Example:

```python
S = "HELLO"
print("S[::-1] =", S[::-1])  # 'OLLEH'

```

### Diagram:

```
Original:  H   E   L   L   O
Index:     0   1   2   3   4
           -5  -4  -3  -2  -1

S[::-1] → moves from -1 to -5 (right to left)

```