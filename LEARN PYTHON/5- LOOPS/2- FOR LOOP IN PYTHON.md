# 2- FOR LOOP in Python

### Example 1: for loop with local variable

```python
for i in range(6):  # range(6) generates numbers from 0 to 5
    print(i)

```

### Example 2: declaring loop variable outside so it's accessible after

```python
x = 0
for x in range(6):
    print(x)
print("OUT OF BLOCK:", x)

```

### Example 3: user input to set loop range

```python
n = int(input("ENTER A NUMBER: "))

for A in range(n+1):  # range(n+1) generates numbers from 0 to n
    print(f"{A}\\\\", end="")  # To print without newline, use end=""

```
