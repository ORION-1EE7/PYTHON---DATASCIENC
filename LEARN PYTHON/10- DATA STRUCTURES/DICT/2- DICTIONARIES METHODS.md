# 2- DICTIONARIES METHODS

> Dictionaries are unordered, mutable collections of key-value pairs.

### Adding & Updating Elements

```python
person["city"] = "New York"
print(person)
# {'name': 'Alice', 'age': 25, 'city': 'New York'}

person["age"] = 26  # Update value

```

### Removing Elements

```python
del person["city"]
print(person)
# {'name': 'Alice', 'age': 26}

age = person.pop("age")
print(age)  # Output: 26
print(person)
# {'name': 'Alice'}

```
