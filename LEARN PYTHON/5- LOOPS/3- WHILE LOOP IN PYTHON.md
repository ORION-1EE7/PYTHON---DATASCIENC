# 3- WHILE LOOP in Python

### Example 1: count from 0 to 5 using while loop

```python
i = 0  # Initialization
while i <= 5:  # Condition
    print(i)
    i += 1  # Update

```

### Example 2: loop variable declared outside and used after loop

```python
x = 0
while x <= 5:
    print(x)
    x += 1
print("OUT OF BLOCK:", x)

```

### Example 3: user input to repeat a loop up to entered number

```python
n = int(input("ENTER A NUMBER: "))

A = 0
while A <= n:
    print(f"{A}\\\\", end="")  # Print without newline
    A += 1

```
