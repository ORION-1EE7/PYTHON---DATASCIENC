# 1- ARGUMENTS TO MAIN

### I - INTRODUCTION

1. **MAIN()** can take arguments, just like any other function.
2. The arguments to **MAIN()** are:
   - **ARGC**: An integer that represents the number of arguments on the command line.
   - **ARGV**: An array of strings that contain the arguments.
3. The prototype for **MAIN()** is:

### II - SYNTAX

```python
def main():
   ARGC: An integer that represents the number of arguments on the command line.
   ARGV: A list of strings that contain the arguments.

```

### III - COMMANDS

```bash
python script.py MOHAMED TALEB 1337
ARG0   ARG1   ARG2  ARG3

```

- `script.py`: The name of the script file.
- `MOHAMED`: The first argument.
- `TALEB`: The second argument.
- `1337`: The third argument.
- **ARGC**: 4 (the number of arguments).

### IV - ARGV

Remember that when it is passed to a function, the list name is a reference to the first element of the list.
In Python, we don’t need to declare a list as a pointer.

### V - ARGC

When a program starts, the arguments to **MAIN** will have been initialized to meet the following conditions:

1. **ARGC** is greater than 0.
2. **ARGV\[ARGC]** is a NULL pointer (in C), but in Python, the list does not contain a NULL value.

### Example:

```abap
                                            _____________
                           |--ARGC = 4-->  |  ARGV[3]   |-->   1337
   ____________            |               |____________|
  |  ARGV     |____________|--ARGC = 3-->  |  ARGV[2]   |--> TALEB
  |___________|            |               |____________|
   ___________             |--ARGC = 2-->  |  ARGV[1]   |--> MOHAMED
  | ARGC = 4 |             |               |____________|
  |__________|             |--ARGC = 1-->  |  ARGV[0]   |--> scp.py
                                           |____________|

```

### Python Code Example:

```python
import sys

def main():
    # The number of arguments (ARGC equivalent)
    argc = len(sys.argv)

    # Print ARGC
    print(argc)

    # Print arguments (this is equivalent to the C code's argv access)
    # sys.argv[argc] would throw an IndexError, so we handle it carefully
    try:
        print(sys.argv[argc])  # This is out of range and will cause an IndexError
    except IndexError:
        print("Index out of range")

    # Print the last argument (argc - 1)
    if argc > 1:
        print(sys.argv[argc - 1])  # Equivalent to argv[argc - 1]

    # Print the second-to-last argument (argc - 2)
    if argc > 2:
        print(sys.argv[argc - 2])  # Equivalent to argv[argc - 2]

    # Print the name of the executable (argv[0] in C)
    print(sys.argv[0])  # This is the name of the script

if __name__ == "__main__":
    main()

```
