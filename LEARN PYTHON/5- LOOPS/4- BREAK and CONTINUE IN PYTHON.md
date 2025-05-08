# 4- BREAK and CONTINUE in Python

### `break` Statement

Use `break` to exit a loop immediately when a condition is met.

### Example 1: Stop loop when `i` is 3

```python
for i in range(6):
    if i == 3:
        break
    print(i)

```

**Output:**

```
0
1
2
```

### Example 2: Stop `while` loop at 3

```python
i = 0
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
```

### `continue` Statement

Use `continue` to skip the current iteration and move to the next one.

### Example 3: Skip printing when `i` is 3

```python
for i in range(6):
    if i == 3:
        continue
    print(i)

```

**Output:**

```
0
1
2
4
5
```

### Example 4: Skip in `while` loop

```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

```
