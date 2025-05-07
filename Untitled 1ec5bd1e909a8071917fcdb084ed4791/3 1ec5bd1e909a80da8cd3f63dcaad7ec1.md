# 3

## **SLICING LISTS**

You can access a **range of elements** from the list using slicing.

```python
#SYNATAX my_list[start:end]

print(fruits[0:2])  # Output: ['apple', 'banana']
```

- `start`: Index of the first element you want to include.
- `end`: Index of the first element you want to exclude.

### **NESTED LISTS**

Lists can contain other lists as elements, creating a **nested list**.

```python
nested_list = [["apple", "banana"], ["cherry", "orange"]]
print(nested_list[0])  # Output: ['apple', 'banana']
print(nested_list[1][1])  # Output: orange

```

### **LIST COMPREHENTION**

List comprehension is a concise way to create lists based on existing lists.

```python
# SYNTAX: new_list = [expression for item in iterable if condition]

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

```