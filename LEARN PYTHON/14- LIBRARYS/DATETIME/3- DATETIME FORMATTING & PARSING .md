# 3- DATETIME FORMATTING & PARSING

You can format or parse datetime objects using `.strftime()` and `.strptime()`.

- **`.strftime()`** formats a `datetime` object into a string.
- **`.strptime()`** parses a string into a `datetime` object using a format.

```python
now = datetime.now()

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
# Output: 2025-05-08 14:30:00

parsed = datetime.strptime("2024-04-10", "%Y-%m-%d")
print(parsed)
# Output: 2024-04-10 00:00:00

```

---

### 📋 **Common Format Codes for `strftime()` and `strptime()`**

| Code   | Meaning                       | Example                     |
| ------ | ----------------------------- | --------------------------- |
| `%Y` | 4-digit year                  | `2025`                    |
| `%y` | 2-digit year                  | `25`                      |
| `%m` | 2-digit month                 | `05`                      |
| `%B` | Full month name               | `May`                     |
| `%b` | Abbreviated month name        | `May`                     |
| `%d` | Day of the month (01–31)     | `08`                      |
| `%A` | Full weekday name             | `Thursday`                |
| `%a` | Abbreviated weekday name      | `Thu`                     |
| `%H` | Hour (24-hour clock, 00–23)  | `14`                      |
| `%I` | Hour (12-hour clock, 01–12)  | `02`                      |
| `%p` | AM or PM                      | `PM`                      |
| `%M` | Minutes (00–59)              | `30`                      |
| `%S` | Seconds (00–59)              | `00`                      |
| `%f` | Microseconds (000000–999999) | `123456`                  |
| `%z` | UTC offset                    | `+0000`                   |
| `%Z` | Time zone name                | `UTC`                     |
| `%j` | Day of the year (001–366)    | `129`                     |
| `%U` | Week number (Sunday start)    | `18`                      |
| `%W` | Week number (Monday start)    | `19`                      |
| `%c` | Locale’s date and time       | `Thu May 8 14:30:00 2025` |
| `%x` | Locale’s date                | `05/08/25`                |
| `%X` | Locale’s time                | `14:30:00`                |
