# 1- ARITHMETIC OPERATORS

**OPERATORS:** An operator is a symbol that performs an operation on one or more operands. An operand is a variable or a value on which we perform the operation:

- `[ + ]` Addition
- `[ - ]` Subtraction
- `[ * ]` Multiplication
- `[ / ]` Division (returns float result even with ints)
- `[ // ]` Floor Division (integer result, like in C++)
- `[ % ]` Modulus (remainder of division)
- `[ ** ]` Exponentiation (power)

```python
# Python version of arithmetic operations
x = 9
y = 4

# 1- ADDITION OPERATOR
res = x + y
print("x + y =", res)  # Adds x and y

# 2- SUBTRACTION OPERATOR
res = x - y
print("x - y =", res)  # Subtracts y from x

# 3- MULTIPLICATION OPERATOR
res = x * y
print("x * y =", res)  # Multiplies x and y

# 4- DIVISION OPERATOR
res = x / y
print("x / y =", round(res, 2))  # True division, returns float (2.25)

# 5- FLOOR DIVISION
res = x // y
print("x // y =", res)  # Truncates decimal like C++ integer division (2)

# 6- MODULUS OPERATOR
res = x % y
print("x % y =", res)  # Remainder when x is divided by y (1)

# 7- EXPONENTIATION OPERATOR
res = x ** y
print("x ** y =", res)  # x raised to the power y (9^4 = 6561)

```
