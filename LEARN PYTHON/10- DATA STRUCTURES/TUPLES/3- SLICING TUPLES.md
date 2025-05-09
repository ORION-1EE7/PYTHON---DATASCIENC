# 3- SLICING TUPLES

You can access a **range of elements** using slicing, just like lists.

```python
colors = ("red", "green", "blue", "yellow")
print(colors[1:3])  # Output: ('green', 'blue')

```

- Tuples support slicing because they are ordered.

### **NESTED TUPLES**

Tuples can contain other tuples or lists.

```python
nested = (("a", "b"), ("c", "d"))
print(nested[1])      # Output: ('c', 'd')
print(nested[0][1])   # Output: b

```

### **TUPLE COMPREHENSION (via Generator -> Tuple)**

Tuples don’t support direct comprehension, but you can convert a generator:

```python
evens = tuple(x for x in range(10) if x % 2 == 0)
print(evens)  # Output: (0, 2, 4, 6, 8)

```
