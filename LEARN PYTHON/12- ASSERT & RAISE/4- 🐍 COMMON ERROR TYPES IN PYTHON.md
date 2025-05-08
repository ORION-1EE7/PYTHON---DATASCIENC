# 4- 🐍 COMMON ERROR TYPES IN PYTHON

Python has several built-in error types that help you identify problems in your code. Understanding these error types is essential for debugging and writing robust programs.

- **`SyntaxError`**: Raised when code is not structured correctly.
- **`NameError`**: Occurs when a variable or function name is not defined.
- **`TypeError`**: Happens when an operation is applied to an inappropriate type.
- **`IndexError`**: Raised when trying to access an invalid index.
- **`ValueError`**: Occurs when a function receives a correct type but invalid value.
- **`ZeroDivisionError`**: Raised when dividing a number by zero.
- **`AttributeError`**: Happens when trying to access an undefined attribute or method on an object.

## EXEMPLES

```python
#SyntaxError
if True # Missing colon after if
    print("Hello")

#NameError
print(x)  # x is not defined

#TypeError
x = "10"
y = 5
print(x + y)  # Cannot add string and integer

#IndexError
lst = [1, 2, 3]
print(lst[5])  # Index 5 does not exist

#ValueError
int("abc")  # Cannot convert string to integer

#ZeroDivisionError
print(10 / 0)

#AttributeError
x = 10
x.append(5)  # int has no 'append' method
```
