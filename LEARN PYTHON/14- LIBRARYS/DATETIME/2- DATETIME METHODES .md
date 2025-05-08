# 2- DATETIME METHODES

- **`datetime.now()`** returns the current local date and time with microseconds.
- **`datetime.today()`** is similar to `now()`, but less customizable.
- **`datetime()`** lets you manually create a date-time object.
- **`strptime()`** parses a string into a datetime object.
- **`date()`** creates a date-only object.

```python
from datetime import datetime, date

now = datetime.now()
print(now)
# Example: 2025-05-08 14:30:00.123456

today = datetime.today()
print(today)
# Example: 2025-05-08 14:30:00.123456

manual = datetime(2024, 12, 25, 18, 0)
print(manual)
# Output: 2024-12-25 18:00:00

parsed = datetime.strptime("2023-03-15 09:30", "%Y-%m-%d %H:%M")
print(parsed)
# Output: 2023-03-15 09:30:00

d = date(2022, 1, 1)
print(d)
# Output: 2022-01-01

```

### **DATETIME ARITHMETIC**

You can perform date/time arithmetic using `timedelta`.

- **`timedelta`** represents a duration.
- You can **add** or **subtract** `timedelta` to/from `datetime` objects.

```python
from datetime import timedelta

now = datetime.now()
print(now)

# Add 7 days
future = now + timedelta(days=7)
print(future)

# Subtract 3 hours
past = now - timedelta(hours=3)
print(past)

```