# 3- OBJECTS IN PYTHON

- Every data item is an object in Python.
- An object is an entity that contains data along with properties and behavior.
- An object refers to a specific blueprint called a class.

## CLASS VS OBJECT

A class is like a blueprint or template.
An object is an instance created based on that blueprint.

**Example:**
CLASS: Person
OBJECT: mtaleb (a specific person created from the Person class)

```abap
╔═════════════════════════════╗     ╔══════════════════════════════╗
║            CLASS            ║     ║            OBJECT            ║
╠═════════════════════════════╣     ╠══════════════════════════════╣
║ - Defined with `class`      ║     ║ - Created from a class       ║
║ - Acts as a blueprint       ║     ║ - Holds actual data          ║
║ - No memory until used      ║     ║ - Occupies memory            ║
║ - Defines methods/attributes║     ║ - Uses class methods/attrs   ║
║ - Example: class Person:    ║     ║ - Example: mtaleb = Person() ║
╚═════════════════════════════╝     ╚══════════════════════════════╝

```

## SUMMARY

- In C, a variable itself is a memory location.
- In Python, a variable is a label attached to some object.

**EXAMPLE CODE:**

```python
class Person:
    def __init__(self, name):
        self.name = name

# mtaleb is an object of the class Person
mtaleb = Person("Mtaleb")
print(mtaleb.name)  # Output: Mtaleb

```
