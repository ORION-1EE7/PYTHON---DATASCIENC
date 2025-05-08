# 1- ASSERT

- `assert` is used to **test assumptions**.
- It raises an `AssertionError` if the condition is `False`.
- Commonly used in **debugging** and **unit testing**.

```python
#SYNTAX: assert condition, "Error message"
```

**EXAMPLE CODE:**

```python
x = 10
assert x > 0, "x should be positive"  # No error

y = -5
assert y > 0, "y should be positive"  # Raises AssertionError: y should be positive

```

### **TRY + ASSERT TOGETHER**

You can combine `try` and `assert` to handle failed assertions gracefully.

```python
def check_age(age):
    try:
        assert age >= 18, "You must be 18 or older."
        print("Access granted.")
    except AssertionError as e:
        print("Access denied:", e)

check_age(20)  # Output: Access granted.
check_age(15)  # Output: Access denied: You must be 18 or older.

```
