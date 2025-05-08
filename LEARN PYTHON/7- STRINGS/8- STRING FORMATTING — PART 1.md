# 8- STRING FORMATTING — PART 1

### I- STRING FORMATTING

1. **INTERPOLATION**:
   - Interpolation is the insertion of something of a different nature into something else.
2. **STRING INTERPOLATION OR STRING FORMATTING**:
   - The process of inserting an object into a predefined string is called string interpolation or string formatting.

### II- % FORMATTING

- The oldest technique used to insert an object into a string.
- Multiple variables are allowed.

### Example:

```python
name = "Ali"
age = 25
print("My name is %s and I am %d years old." % (name, age))

```

**Output:**

```
My name is Ali and I am 25 years old.

```

### III- `str.format()` FUNCTION

- The placeholders are replaced by curly braces in this technique.
- Referencing variables through indexing is possible.
- To improve readability, keywords can also be used.
- Format specifiers like `f` for float, `b` for binary, and `d` for integer can be used.
- An int can be provided in place of a float.
- Providing a string in place of a float will result in an error.
- The length of the values after the decimal point can be controlled.

### Examples:

```python
print("Hello, {}!".format("Sara"))

```

**Output:**

```
Hello, Sara!

```

```python
print("Value: {:.2f}".format(3.14159))

```

**Output:**

```
Value: 3.14

```

```python
print("Binary of 5 is {:b}".format(5))

```

**Output:**

```
Binary of 5 is 101

```

```python
print("Name: {name}, Age: {age}".format(name="Lina", age=30))

```

**Output:**

```
Name: Lina, Age: 30

```
