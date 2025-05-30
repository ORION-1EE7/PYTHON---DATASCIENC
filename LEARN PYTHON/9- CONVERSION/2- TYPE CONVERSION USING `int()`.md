# 2- TYPE CONVERSION USING `int()`

- **Definition**: Refers to the conversion of an object of one type to the integer type via the programmer's intervention.
- **Syntax**:

  ```python
  int(value, base)

  ```

  - `value`: The object you want to convert.
  - `base`: (Optional) The base of the number system (e.g., binary, octal, decimal, hexadecimal).

### Code Example:

```python
x = "110"
print(x)                  # Output: "110"
print(type(x))            # Output: <class 'str'>

# Convert string to integer
x = int(x)
print(x)                  # Output: 110
print(type(x))            # Output: <class 'int'>

# Convert string '110' from binary (base 2) to integer
x = int(x, 2)
print(x)                  # Output: 6 (binary 110 is 6 in decimal)

```
