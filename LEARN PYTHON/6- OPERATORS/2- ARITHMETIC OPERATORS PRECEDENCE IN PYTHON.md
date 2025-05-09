# 2- ARITHMETIC OPERATORS PRECEDENCE IN PYTHON

The precedence of operators in Python dictates the order in which operations are performed. Operators with higher precedence are evaluated before those with lower precedence.

Here's the order of precedence from highest to lowest for arithmetic operators:

- **Highest**: `*`
- `%, //, /, *`
- **Lowest**: `, +`

```abap
			highest 								  **
				 |						      %, //, /, *
			 lowest							     -, +
```

Operations with the same precedence are evaluated left to right (left-associative). However, exponentiation is right-associative, meaning it evaluates from right to left.

### EXAMPLES:

```python
# Example 1: Exponentiation takes precedence over multiplication.
result = 2 + 3 * 2 ** 2
print(f"2 + 3 * 2 ** 2 = {result}")  # Output: 2 + 3 * 4 = 14
# Explanation: 2 ** 2 = 4, then 3 * 4 = 12, finally 2 + 12 = 14

# Example 2: Parentheses override operator precedence.
result = (2 + 3) * 2 ** 2
print(f"(2 + 3) * 2 ** 2 = {result}")  # Output: 5 * 4 = 20
# Explanation: Parentheses are evaluated first, so (2 + 3) = 5, then 5 * 4 = 20

# Example 3: Subtraction and addition have the same precedence and are evaluated from left to right.
result = 10 - 5 + 2
print(f"10 - 5 + 2 = {result}")  # Output: 7
# Explanation: 10 - 5 = 5, then 5 + 2 = 7

# Example 4: Floor division has higher precedence than addition.
result = 10 + 5 // 2
print(f"10 + 5 // 2 = {result}")  # Output: 10 + 2 = 12
# Explanation: 5 // 2 = 2, then 10 + 2 = 12

# Example 5: Modulo has the same precedence as multiplication and division and is evaluated from left to right.
result = 10 % 3 * 2
print(f"10 % 3 * 2 = {result}")  # Output: 1 * 2 = 2
# Explanation: 10 % 3 = 1, then 1 * 2 = 2

# Example 6: Exponentiation is right-associative, so it evaluates from right to left.
result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result}")  # Output: 2 ** (3 ** 2) = 2 ** 9 = 512
# Explanation: 3 ** 2 = 9, then 2 ** 9 = 512

```
