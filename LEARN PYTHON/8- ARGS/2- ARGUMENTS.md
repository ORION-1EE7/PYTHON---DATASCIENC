# 2- ARGUMENTS

### PRINT PARAMS

🚨 **WHEN YOU DON'T USE ARGC IN YOUR CODE, YOU SHOULD USE `ARGC = None` OR `VOID(ARGC)` TO AVOID COMPILATION ERRORS.**

### Python Code Example:

```python
import sys

def main():
    i = 1  # Start from the first argument (ignoring the script name)
    while i < len(sys.argv):
        j = 0
        while j < len(sys.argv[i]):
            # Print each character of the argument using sys.stdout.write
            sys.stdout.write(sys.argv[i][j])
            j += 1
        # Print a newline after each argument
        sys.stdout.write("\\n")
        i += 1

if __name__ == "__main__":
    main()

```
