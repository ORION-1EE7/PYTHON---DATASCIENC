# 1

## **TRY, EXCEPT AND ASSERT IN PYTHON**

### **I- TRY & EXCEPT**

- Used for **error handling**.
- The code in the `try` block is executed first.
- If an error (exception) occurs, Python jumps to the `except` block.
- Prevents the program from crashing due to runtime errors.

**Syntax:**

```python
try:
    # Code that might raise an error
    ...
except ErrorType:
    # Code that runs if an error occurs
    ...

```

**EXAMPLE CODE:**

```python
def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

divide(10, 2)  # Output: Result: 5.0
divide(5, 0)   # Output: Error: Cannot divide by zero.

```