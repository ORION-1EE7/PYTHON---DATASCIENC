# 4- INTEGER TYPES IN PYTHON (NO SHORT / LONG LIMITS

**I - PYTHON INTEGERS**
In Python, there is only one built-in integer type: `int`. It can handle very large numbers automatically. Python abstracts away "short", "long", "unsigned", etc., which are necessary in C++.

Python integers are:

- Arbitrary-precision (limited by system memory, not fixed size)
- Signed by default (can be positive or negative)

```python
a = 10                       # Regular int
b = 9223372036854775807      # Large int (fits easily)
c = -2147483648              # Negative int

print("a (regular int):", a)
print("b (large int):", b)
print("c (negative int):", c)

```

**II - BYTE REPRESENTATION (If needed)**
You can work with specific sizes using the `struct` module or `ctypes` for C-style behavior.

```python
import struct

short_val = struct.pack("h", 32000)     # signed short (2 bytes)
unshort_val = struct.pack("H", 65000)   # unsigned short (2 bytes)

# To interpret:
short_num = struct.unpack("h", short_val)[0]
unshort_num = struct.unpack("H", unshort_val)[0]

print("Signed short (struct):", short_num)
print("Unsigned short (struct):", unshort_num)

```

**III - BYTE SIZE INFORMATION**
You can check the size of numbers using the `__sizeof__()` method.

```python
x = 10
big = 10**100

print("Size of x:", x.__sizeof__(), "bytes")
print("Size of big:", big.__sizeof__(), "bytes")

```

**Summary:**

- Python hides low-level data types like short/long.
- Use `int` for all integer operations.
- For bit-size control, use modules like `struct`, `array`, or `ctypes`.
