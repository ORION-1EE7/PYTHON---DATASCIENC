# 2- SETS METHODS

> Sets are unordered collections of unique elements. They are mutable, but do not support indexing or slicing.

### Adding Elements

```python
numbers.add(4)
print(numbers)
# {1, 2, 3, 4}

numbers.update([5, 6])
print(numbers)
# {1, 2, 3, 4, 5, 6}
```

### Removing Elements

```python
numbers.remove(3)
print(numbers)
# {1, 2, 4, 5, 6}

numbers.discard(10)  # No error if 10 not found
print(numbers)

popped = numbers.pop()  # Removes a random element
print(popped)
```
