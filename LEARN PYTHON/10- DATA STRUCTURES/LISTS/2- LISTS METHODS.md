# 2- LISTS METHODS

### ADD ELEMENTS

You can add elements to a list using methods like `.append()`, `.insert()`, or `.extend()`.

- **`append()`** adds an element at the end of the list.
- **`insert()`** adds an element at a specific index.
- **`extend()`** adds multiple elements at the end of the list.

### REMOVING ELEMENTS

You can remove elements using methods like `.remove()`, `.pop()`, or `del`.

- **`remove()`** removes the first occurrence of a value.
- **`pop()`** removes an element at a specific index and returns it.
- **`del`** deletes an element at a specific index or the entire list.

```python
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

fruits.insert(1, "mango")
print(fruits)  # Output: ['apple', 'mango', 'blueberry', 'cherry', 'orange']

fruits.extend(["grapes", "kiwi"])
print(fruits)  # Output: ['apple', 'mango', 'blueberry', 'cherry', 'orange', 'grapes', 'kiwi']

fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'mango', 'blueberry', 'orange', 'grapes', 'kiwi']

removed_fruit = fruits.pop(2)  # Removes 'blueberry'
print(fruits)  # Output: ['apple', 'mango', 'orange', 'grapes', 'kiwi']
print(removed_fruit)  # Output: blueberry

del fruits[1]  # Deletes 'mango'
print(fruits)  # Output: ['apple', 'orange', 'grapes', 'kiwi']

```
