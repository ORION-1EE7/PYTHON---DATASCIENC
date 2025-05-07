# 1

## IMPLICIT TYPE CONVERSION

- **Definition**: The ability of Python to automatically convert an object from one data type to another without intervention from the programmer.
- **Rules of Conversion**: Lower data types are converted to higher data types.
- **Hypothetical Rule of Conversion**: Higher data types are not automatically converted to lower data types.
- **Examples**:
    - Dividing two integers results in a floating-point value.
    - The type of the result depends on the operator and the value with the higher data type.
    - In C, it is possible for a higher data type to be converted to a lower data type.
    - In Python, implicit conversion from a higher to a lower data type is **not** possible.

### Code Example:

```python
x = 10
y = 20

total = x + y
print("the total is:" + total)  # TypeError: can only concatenate str (not "int") to str

```