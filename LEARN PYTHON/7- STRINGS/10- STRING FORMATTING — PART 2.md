# 10- STRING FORMATTING — PART 2

### I - f-STRINGS

- Introduced in Python 3.6 for cleaner string formatting
- **Syntax:** `f"some text {expression}"`
- You can insert variables or expressions directly into strings
- Supports inline operations and method calls

### f-string Examples:

```python
# Example:
name = "Ali"
age = 25
print(f"My name is {name} and I am {age} years old.")
print(f"Next year, I’ll be {age + 1}.")
print(f"My name in uppercase is {name.upper()}.")

```

### II - IMPORTANT STRING METHODS

### 1. CASE METHODS

- `.lower()`: Converts all characters to lowercase
- `.upper()`: Converts all characters to uppercase
- `.capitalize()`: Capitalizes the first character
- `.title()`: Capitalizes the first letter of each word
- `.casefold()`: Unicode-safe lowercasing (more aggressive than `.lower()`)

### Example:

```python
print("HeLLo".lower())          # hello
print("hello".upper())          # HELLO
print("hello world".capitalize())  # Hello world
print("hello world".title())      # Hello World
print("ß".casefold())            # ß (Unicode safe)

```

### 2. LENGTH AND COUNT

- `len(string)`: Returns the total number of characters
- `.count(sub)`: Returns how many times 'sub' appears in the string

### Example:

```python
print(len("banana"))           # 6
print("banana".count("a"))     # 3

```

### 3. SEARCHING

- `.find(sub)`: Returns the index of the first occurrence or -1 if not found
- `.rfind(sub)`: Same as `.find()`, but searches from the end
- `.index(sub)`: Like `.find()`, but raises an error if not found

### Example:

```python
print("hello".find("e"))      # 1
print("hello".rfind("l"))     # 3
print("hello".index("h"))     # 0

```

### 4. REPLACE AND STRIP

- `.replace(old, new)`: Replaces all occurrences of `old` with `new`
- `.strip()`: Removes whitespace from both ends
- `.lstrip()`: Removes leading whitespace
- `.rstrip()`: Removes trailing whitespace

### Example:

```python
print("apple".replace("p", "b"))  # abble
print("   spaced   ".strip())     # 'spaced'
print("   spaced".lstrip())       # 'spaced'
print("spaced   ".rstrip())       # 'spaced'

```

### 5. TYPE CHECKING

- `.isalpha()`: True if all characters are letters
- `.isdigit()`: True if all characters are digits
- `.isalnum()`: True if all characters are alphanumeric
- `.isspace()`: True if all characters are whitespace
- `.islower()`, `.isupper()`: Check if all characters are lower/uppercase

### Example:

```python
print("Hello".isalpha())        # True
print("123".isdigit())          # True
print("Hello123".isalnum())     # True
print("   ".isspace())          # True
print("hello".islower())        # True
print("HELLO".isupper())        # True

```

### 6. SPLIT AND JOIN

- `.split(delimiter)`: Splits string into a list using `delimiter`
- `.rsplit(delimiter)`: Same as `.split()`, but from the right
- `.join(list)`: Joins list elements into a string with the specified separator

### Example:

```python
print("a,b,c".split(","))       # ['a', 'b', 'c']
print("a,b,c".rsplit(",", 1))   # ['a,b', 'c']
print("-".join(["a", "b", "c"]))  # a-b-c

```

### 7. START/END CHECKS

- `.startswith(prefix)`: Returns True if string starts with `prefix`
- `.endswith(suffix)`: Returns True if string ends with `suffix`

### Example:

```python
print("data.csv".endswith(".csv"))  # True
print("<https://example.com>".startswith("https"))  # True

```
