# 3- DATA TYPE CASTING IN PYTHON

In Python, data type casting means converting a variable from one data type to another. This can be done **implicitly** or **explicitly**, but Python is less strict than C++ and handles many conversions automatically.

**I - IMPLICIT CASTING (Automatic Type Conversion)**

- Performed automatically by Python.
- Happens when doing operations that mix types (e.g., int + float).
- Python will promote types to avoid data loss.

```python
a = 10         # int
b = 3.5        # float
c = a + b      # int + float → float

print("a (int):", a)
print("b (float):", b)
print("c (a + b):", c)  # Result is float

```

**II - EXPLICIT CASTING (Manual Type Conversion)**

- Done by the programmer using built-in functions.
- Used when you want to control how data is converted between types.

```python
x = 10.75
y = int(x)     # float → int (decimal part is removed)

print("x (float):", x)
print("y (int from x):", y)

s = "123"
n = int(s)     # str → int

print("s (string):", s)
print("n (int from s):", n)

f = float("9.81")  # str → float
print("f (float from string):", f)

```

You can also cast to:

- `str()`: Convert any value to string
- `int()`: Convert to integer
- `float()`: Convert to float
- `bool()`: Convert to boolean

**Example:**

```python
value = 0
truth = bool(value)  # 0 is False, non-zero is True
print("bool(0):", truth)

```
