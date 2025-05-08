# 1- STRINGS IN PYTHON

### I- STRING DATA TYPE:

- A string is a sequence of characters.
- Can be enclosed in single or double quotes.

### Example:

```python
name = "Mohamed"
greeting = 'Hello'

```

- If single quotes are used inside the string, then the string should be enclosed within double quotes, and vice versa.

### Valid Example:

```python
statement1 = "The language 'Python' is named after Monty Python."

```

### Invalid Example:

```python
statement2 = "Hello! " I am Mtaleb". How's your mother?"  # INVALID SYNTAX

```

- Alternatively, single or double quotes within a string can be escaped using the backslash (`\\`) character.

### Escaped Quotes Example:

```python
statement3 = "Hello! \\"I am Mtaleb\\". How's your mother?"
statement4 = 'The language \\'Python\\' is named after Monty Python.'

```

### II- MULTI-LINE STRINGS:

- A multi-line string is enclosed in triple-single-quotes (''') or triple-double-quotes.
- Useful for large blocks of text, documentation, or multi-line messages.

### Example:

```python
multi_line_text = '''This is a multi-line string.
It can span several lines
and preserves formatting.'''

print(multi_line_text)

```

### III- CODE EXAMPLE (Combining all concepts):

```python
# Single line strings with quotes and escapes
name = "Mtaleb"
quote = "He said, \\"Python is powerful!\\""
language_info = 'The language \\'Python\\' was named after Monty Python.'
test = "info", 245, 2.4 , "mtaleb"

# Multi-line string
bio = """My name is Mtaleb.
I'm learning Python at 1337 school.
I love strings and multi-line formatting."""

bio2 = '''My name is Mtaleb.
I'm learning Python at 1337 school.
I love strings and multi-line formatting.'''

# Print all
print(test[1])
print("\\n", bio2)

```
