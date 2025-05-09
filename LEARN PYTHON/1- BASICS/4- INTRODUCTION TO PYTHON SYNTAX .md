# 4- INTRODUCTION TO PYTHON SYNTAX

This guide will give you a brief overview of basic Python syntax — how to write and understand Python code.

## I - PYTHON FILES

Python code is written in plain text files with the `.py` extension.
**Example file name:** `hello.py`

## II - PRINTING TO THE SCREEN

You use the `print()` function to output information to the console.

```python
print("Hello, world!")

```

**Output:**

```
Hello, world!

```

## III - INDENTATION

Python uses **indentation** (spaces or tabs) to define blocks of code.
Unlike C++ or Java, Python does **not** use `{}` to group code.
**Example:**

```python
if 5 > 3:
    print("Five is greater than three")

```

## IV - VARIABLES AND DATA TYPES

You do not need to declare variable types in Python — it's **dynamically typed**.

```python
name = "Alice"     # String
age = 25           # Integer
height = 5.6       # Float
is_student = True  # Boolean

```

## V - COMMENTS

Use `#` for single-line comments.

```python
# This is a comment

```

## VI - BASIC INPUT

You can use `input()` to take user input as a string.

```python
username = input("Enter your name: ")
print("Hello,", username)

```

## VII - BASIC IF STATEMENT

```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

```

## VIII - FUNCTIONS

You define a function using the `def` keyword.

```python
def greet(name):
    print("Hello,", name)

greet("Ali")

```

## IX - LOOPS

### While Loop

```python
count = 0
while count < 3:
    print("Count:", count)
    count += 1

```

### For Loop

```python
for i in range(3):
    print("Loop index:", i)

```

## OUTPUT EXAMPLES:

```
Hello, world!
Five is greater than three
Hello, Ali
Count: 0
Count: 1
Count: 2
Loop index: 0
Loop index: 1
Loop index: 2

```
