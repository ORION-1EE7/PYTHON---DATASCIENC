# 5

# GLOBAL AND LOCAL VARIABLES

**I- GLOBAL VARIABLES**

- Global variables are declared outside of all functions.
- They are accessible from any function in the program.
- Declared like local variables, but placed outside all function blocks.

**II- LOCAL VARIABLES**

- Local variables are declared inside a function.
- They are accessible only within the function in which they are declared.
- Declared like global variables, but placed inside a function block.

**Scope:**

- **Global scope:** accessible from any part of the program.
- **Local scope:** exists only during the function execution.

**EXAMPLE CODE:**

```python
# GLOBAL VARIABLE
a = 10

def fun():
    # LOCAL VARIABLE
    b = 20

    print("Global variable:", a)
    print("Local variable:", b)

def main():
    fun()  # Calling the function to demonstrate variable access

    # 'b' is not accessible here, but 'a' still is
    print("Accessing global variable from main:", a)

if __name__ == "__main__":
    main()

```