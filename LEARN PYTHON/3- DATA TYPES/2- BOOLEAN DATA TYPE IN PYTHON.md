# 2- BOOLEAN DATA TYPE IN PYTHON

**I - BOOLEAN**
The Boolean data type represents one of two values: True or False. It is used to represent logical values and is fundamental in conditional statements and loops.

**II - BOOLEAN IN PYTHON**
Python has a built-in `bool` type that represents Boolean values:

- **True** → Represents the logical value of truth.
- **False** → Represents the logical value of falsity.

A Boolean can be used in logical operations and conditional statements. It is typically the result of comparison operations, logical operations, or explicitly declared.

**III - BOOLEAN OPERATORS**
Common Boolean operations include:

- `and`: Returns True if both operands are True.
- `or`: Returns True if at least one operand is True.
- `not`: Reverses the Boolean value (True becomes False, False becomes True).

**EXAMPLE 1: Simple Boolean values**

```python
isTrue = True
isFalse = False

print(f"True: {isTrue}")
print(f"False: {isFalse}")

```

**EXAMPLE 2: Comparison operators that return Booleans**

```python
a = 10
b = 20

print(f"a == b: {a == b}")  # False
print(f"a < b: {a < b}")    # True
print(f"a > b: {a > b}")    # False

```

**EXAMPLE 3: Using Boolean operators**

```python
x = True
y = False

print(f"x and y: {x and y}")  # False
print(f"x or y: {x or y}")    # True
print(f"not x: {not x}")      # False

```

**EXAMPLE 4: Conditional statements using Booleans**

```python
if x:
    print("x is True")
else:
    print("x is False")

```

**EXAMPLE 5: Using Booleans in loops**

```python
while not isFalse:
    print("This will run once because isFalse is False.")
    break

```

**OUTPUT:**

```abap
True: True
False: False
a == b: False
a < b: True
a > b: False
x and y: False
x or y: True
not x: False
x is True
This will run once because isFalse is False.

```
