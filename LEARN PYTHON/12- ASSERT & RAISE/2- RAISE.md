# 2- RAISE

- The raise statement is used to manually trigger exceptions.

- It is useful when you want to signal that an error condition has occurred.

```python
# SYNTAX: raise ExceptionType("Error message")

```

**EXAMPLE CODE:**

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

print(divide(10, 2))   # Output: 5.0
print(divide(10, 0))   # Raises ZeroDivisionError: Cannot divide by zero.

```

### **TRY + RAISE TOGETHER**

You can catch exceptions that were raised using try-except blocks:

```python
def validate_username(username):
    if not username:
        raise ValueError("Username cannot be empty.")
    print("Valid username.")

try:
    validate_username("Alice")  # Valid username.
    validate_username("")       # Raises ValueError
except ValueError as e:
    print("Validation error:", e)

```

This is helpful for custom error handling and for creating more predictable and controlled failure modes in your programs.
