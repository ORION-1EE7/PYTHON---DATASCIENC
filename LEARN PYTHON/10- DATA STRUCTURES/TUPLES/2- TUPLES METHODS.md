# 2- TUPLES METHODS

> Tuples are ordered, immutable collections. Once created, elements cannot be changed or removed directly.

### Creating a Tuple

```python
colors = ("red", "green", "blue")

```

### Accessing Elements

```python
print(colors[0])   # Output: red
print(colors[-1])  # Output: blue

```

### Tuple Conversion (Workaround for Modification)

To "modify" a tuple, convert it to a list, change it, then convert back:

```python
colors = list(colors)
colors.append("yellow")
colors = tuple(colors)
print(colors)
# ('red', 'green', 'blue', 'yellow')

```
