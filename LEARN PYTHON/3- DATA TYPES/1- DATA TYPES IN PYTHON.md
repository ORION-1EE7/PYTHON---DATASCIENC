# 1- DATA TYPES IN PYTHON

**I - BIT / BYTE**

1. **BIT**: The smallest unit of data in a computer. It can be 0 or 1.
2. **BYTE**: A group of 8 bits.

**II - DATA TYPES**
Python provides several fundamental data types:

1. **int** → Used to store whole numbers.
2. **float** → Used to store decimal numbers.
3. **complex** → Used to store complex numbers.
4. **str** → Used to store strings (characters).
5. **bool** → Represents Boolean values (True or False).
6. **None** → Represents no value (used for nothing).

**TYPES AND SIZE IN PYTHON**
Python does not use a fixed size for its types (like C++), so you can rely on the system to determine the size.
For example:

- **int** is dynamically sized (usually 4 or 8 bytes, depending on the system).
- **float** typically takes 8 bytes (double precision).
- **str** (string) is dynamic in size and is not fixed.
- **bool** takes 1 byte.

**EXAMPLE CODE:**

```python
# VARIABLES WITH VALUES
a = 1337           # int
b = 10.5           # float
c = 10.5 + 2j      # complex
d = 'A'            # str (char in C++ is just a string with one character)
fullName = "mtaleb" # str

# Printing values with the variable types
print(f"int: {a}")
print(f"float: {b}")
print(f"complex: {c}")
print(f"str: {d}")
print(f"string: {fullName}")

```

**OUTPUT:**

```
int: 10
float: 10.5
complex: (10.5+2j)
str: A
string: Ali
```
