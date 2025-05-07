# 1

## LISTS IN PYTHON

### 1. **Definition**

- **Lists** are **ordered collections** of items, which can be of different types, such as integers, strings, or even other lists. Lists are **mutable**, meaning that their content can be changed after they are created.

### 2. **Creating a List**

You can create a list by enclosing elements in square brackets `[]` and separating them by commas.

### Syntax:

```python
# SYNTAX:my_list = [element1, element2, element3]
fruits = ["apple", "banana", "cherry"]
```

### 3. **Accessing Elements**

- List elements can be accessed using their **index**. Indexing starts at `0`.
- You can use negative indices to access elements from the end of the list.

```python
#SYNTAX 
my_list[index]

#EXEMPLE
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

print(fruits[-1])  # Output: cherry (last element)
print(fruits[-2])  # Output: banana (second last element)
```

### 4. **List Length**

You can find the length of a list using the `len()` function.

```python
print(len(fruits))  # Output: 4
```