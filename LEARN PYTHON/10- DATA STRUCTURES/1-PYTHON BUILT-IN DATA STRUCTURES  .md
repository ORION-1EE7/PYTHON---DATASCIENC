## PYTHON BUILT-IN DATA STRUCTURES

Python provides several built-in data structures — `list`, `tuple`, `set`, and `dict` — for efficiently storing and organizing data. Below is a detailed comparison of their behavior, usage, and properties.

### DIFFERENCE BETWEEN LIST, TUPLE, SET, AND DICTIONARY

| FEATURE                  | LIST                              | TUPLE                             | SET                      | DICTIONARY                      |
| ------------------------ | --------------------------------- | --------------------------------- | ------------------------ | ------------------------------- |
| **Type**           | Non-homogeneous                   | Non-homogeneous                   | Non-homogeneous          | Non-homogeneous                 |
| **Structure**      | Elements in a row (can be nested) | Elements in a row (can be nested) | Elements in a single row | Key-value pairs (can be nested) |
| **Syntax**         | `[ ]`                           | `( )`                           | `{ }`                  | `{ }`                         |
| **Duplicates**     | Allowed                           | Allowed                           | Not allowed              | Keys not allowed to duplicate   |
| **Nesting**        | Allowed                           | Allowed                           | Allowed                  | Allowed                         |
| **Example**        | `[1, 2, 3, 4, 5]`               | `(1, 2, 3, 4, 5)`               | `{1, 2, 3, 4, 5}`      | `{1: "a", 2: "b", 3: "c"}`    |
| **Constructor**    | `list()`                        | `tuple()`                       | `set()`                | `dict()`                      |
| **Mutability**     | Mutable                           | Immutable                         | Mutable                  | Mutable                         |
| **Order**          | Ordered                           | Ordered                           | Unordered                | Ordered (from Python 3.7+)      |
| **Empty Creation** | `l = []`                        | `t = ()`                        | `a = set()`            | `d = {}`                      |
