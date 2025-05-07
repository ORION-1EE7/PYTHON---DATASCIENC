# 6

# DEEPER LOOK INTO PYTHON DATA TYPES

- TYPES:
. Types are fundamental to any Python program.
. They describe what kind of data we are working with and what we can do with it.

Python has a flexible and dynamic type system:
. Primitive/Built-in types – defined by the language
. User-defined types – created using classes and objects

## Built-in Primitive Types

### Primitive Types

***|***\_
\| |
Arithmetical types Special types (None)

***|***
\| |
Integer & Boolean Floating-point
(int, bool) types types (float)

Python examples of primitive types:

```python
a = 42              # int
b = 3.14            # float
c = True            # bool
d = "hello"         # str (sequence type, not arithmetic)
e = None            # NoneType (similar to `void` in C++)

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))
print("Type of e:", type(e))

```

You can also define your own data types in Python using classes:

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print("Custom object type:", type(p))

```