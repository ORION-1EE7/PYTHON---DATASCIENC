# 5- STRING OPERATORS — PART 3

### I- MEMBERSHIP OPERATORS

1. **THE `in` OPERATOR**
   - The membership operator (`in`) returns `True` if the first operand is contained within the second operand.
2. **THE `not in` OPERATOR**
   - The membership operator (`not in`) returns `True` if the first operand is not contained within the second operand.

### Example:

```python
sentence = "Hello, welcome to Python!"
word = "Python"

# 'in' Operator
print("'Python' in sentence:", word in sentence)   # True

# 'not in' Operator
print("'Java' not in sentence:", "Java" not in sentence)  # True

```

### II- ESCAPE SEQUENCE OPERATOR

- Escape characters are used to insert non-allowed characters in a string.
- Escape characters consist of a backslash (`\\`) followed by a non-allowed character.
- Some escape characters include: `\\n`, `\\b`, `\\t`, `\\\\`, `\\ooo`, and `\\xhh`.

### Example:

```python
print("Newline example:\\nThis is after newline")   # \\n adds a newline
print("Tab example:\\tIndented text")               # \\t adds a tab
print("Backslash example: \\\\")                     # \\\\ prints a single backslash
print("Unicode escape: \\u0048\\u0065\\u006c\\u006c\\u006f")  # \\u for Unicode (Hello)

```

### III- STRING FORMATTING OPERATOR

- The string formatting operator (`%`) is used to format a string.
- `%d`, `%c`, `%s`, and `%f` are some commonly used string formatters.

### Example:

```python
name = "John"
age = 25
height = 5.9

print("Hello, my name is %s. I am %d years old and %.1f feet tall." % (name, age, height))

```
