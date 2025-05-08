# 2- ACCESSING TO STRING CHARACTERS

### I- ACCESSING INDIVIDUAL CHARACTERS

```
          ___________________
         | H | E | L | L | O |
         |___|___|___|___|___|
           0   1   2   3   4

```

### Example:

```python
string = "HELLO"
print(f"First character: {string[0]}")  # H
print(f"Second character: {string[1]}")  # E
print(f"Last character: {string[4]}")  # O

```

### II- ACCESSING INDIVIDUAL CHARACTERS FROM THE LAST

```
          ___________________
         | H | E | L | L | O |
         |___|___|___|___|___|
           0   1   2   3   4
          -5  -4  -3  -2  -1

```

### Example:

```python
print(f"Last character (using negative index): {string[-1]}")  # O
print(f"Second last character (using negative index): {string[-2]}")  # L

```

### III- ACCESSING THE SUBSTRING OF A STRING

- A range of characters can be accessed using slicing.
- **SYNTAX:** `name_of_variable[start_index: end_index]`

### Example:

```python
substring = string[1:4]  # From index 1 to 3
print(f"Substring (from index 1 to 3): {substring}")  # ELL

```
