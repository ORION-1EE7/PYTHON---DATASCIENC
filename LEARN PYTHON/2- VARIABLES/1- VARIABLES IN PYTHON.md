# 1- VARIABLES IN PYTHON

A variable is a name attached to a value which can be changed and is used later in a code.
You need a declaration, for example:

- `x = 0`
- `name = "mohamed"`

## COMPARISON WITH C LANGUAGE

In **C language**, the type of variables needs to be specified in advance and the variable can store only that type of value during its lifetime.

```c
 ____________________________________
|   variable of type int             |
|        ↓                           |
|   int x = 10;                      |
|   x = 4.55; <- can't store a float |
|____________________________________|

```

In **Python**, the type of a variable need not be specified in advance and the variable can store **any** type of value during its lifetime.

```c
 ____________________________________
|   variable of type int             |
|        ↓                           |
|   x = 10                           |
|   x = 4.55 <- not a problem        |
|____________________________________|

```