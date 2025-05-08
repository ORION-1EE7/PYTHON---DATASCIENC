# 5- OVERFLOW IN PYTHON

**I - OVERFLOW DEFINITION**

- Overflow happens when a number exceeds the storage limit of its data type.
- In Python, integers have arbitrary precision, so they won't overflow like in C/C++.
- However, floating-point numbers in Python do have limits and can overflow to 'inf'.

**II - TYPES OF OVERFLOW**

1. Integer Overflow:

- In C/C++, fixed-size integers overflow when they exceed their max size.
- In Python, integers grow as needed, so there's no overflow.

```python
a = 2**63 - 1  # Simulates 64-bit signed int max
b = a + 1
print("Simulated 64-bit int max:", a)
print("a + 1 (no overflow in Python):", b)  # Python handles this fine

```

1. Floating-point Overflow:

- Python floats are based on C double (64-bit).
- If a float exceeds \~1.8e+308, it results in 'inf'.

```python
import sys

large_float = 1.7e+308
overflowed_float = large_float * 2

print("Large float:", large_float)
print("Overflowed float (float * 2):", overflowed_float)  # inf

```

**III - UNSIGNED-LIKE WRAPAROUND (Simulated)**
Python doesn’t have unsigned int types by default, but you can simulate 32-bit or 64-bit wrap-around using modulo.

```python
x = (2**32) - 1  # UINT_MAX for 32-bit
y = 1
wraparound = (x + y) % (2**32)

print("Simulated 32-bit unsigned max:", x)
print("x + 1 wrapped around (mod 2^32):", wraparound)

```

**IV - OVERFLOW HANDLING IN PYTHON**

- Integer overflow: not a problem in Python (auto-handled).
- Float overflow: results in 'inf'.
- Use `math.isinf()` or `math.isnan()` to detect such cases.

```python
import math

if math.isinf(overflowed_float):
    print("Overflow detected: result is infinity.")

```
