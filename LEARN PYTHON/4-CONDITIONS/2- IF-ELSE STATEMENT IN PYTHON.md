# 2- IF-ELSE STATEMENT in Python

### Example 1: Basic `if-else` statement

```python
x = 10

if x > 5:  # Condition is true
    print("x is greater than 5")  # This block runs
else:  # Condition is false (won't run in this case)
    print("x is less than or equal to 5")

```

### Example 2: Condition is false

```python
y = 3

if y > 5:  # Condition is false
    print("y is greater than 5")  # This block will not run
else:  # Condition is false, so this block runs
    print("y is less than or equal to 5")

```

### Example 3: Nested `if-else` statement

```python
z = 10

if z > 5:
    if z < 15:  # Nested condition
        print("z is between 5 and 15")  # This block runs
    else:
        print("z is greater than or equal to 15")  # This won't run

```
