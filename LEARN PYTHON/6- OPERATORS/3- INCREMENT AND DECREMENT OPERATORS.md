# 3- INCREMENT AND DECREMENT OPERATORS

### 1. INCREMENT OPERATORS

Used to increase the value of the variable by 1. Python does not have `++` or `--` operators. Instead, we use `+= 1` to increment and `-= 1` to decrement. You can simulate pre- and post-increment behavior manually.

### 2. DECREMENT OPERATORS

Used to decrease the value of the variable by 1. Similarly, Python uses `-= 1` instead of `--`.

### EXAMPLES:

```python
# INCREMENT OPERATORS
x = 5
y = 5
X = 10.5

# 1- PRE-INCREMENT (simulated)
x += 1
print("pre-increment:", x)  # 5 + 1 = 6

X += 1
print("pre-increment float:", X)  # 10.5 + 1 = 11.5

# 2- POST-INCREMENT (simulated)
print("post-increment:", y)  # prints before incrementing
y += 1
print("new y =", y)  # 6 after post-increment
res = y - x  # 6 - 6 = 0
print("y - x =", res)

# The same steps with float
X = 10.5
print("post-increment float:", X)  # prints before incrementing
X += 1
print("new X =", X)  # 11.5 after post-increment

# DECREMENT OPERATORS
a = 8
b = 11
v = 2
A = 4.5

# 1- PRE-DECREMENT (simulated)
a -= 1
print("pre-decrement:", a)  # 8 - 1 = 7

A -= 1
print("pre-decrement float:", A)  # 4.5 - 1 = 3.5

# 2- POST-DECREMENT (simulated)
print("post-decrement:", b)  # prints before decrementing
b -= 1
print("new b =", b)  # 10
print("b - v =", b - v)  # 10 - 2 = 8

# The same steps with float
A = 4.5
print("post-decrement float:", A)  # prints before decrementing
A -= 1
print("new A =", A)  # 3.5 after post-decrement

```
