# 3- ARGUMENTS

### REV PARAMS

### Python Code Example:

```python
import sys

def main():
    i = len(sys.argv) - 1  # Start from the last argument (ignoring the script name)

    while i > 0:
        j = 0
        while j < len(sys.argv[i]):
            # Print each character of the argument using sys.stdout.write
            sys.stdout.write(sys.argv[i][j])
            j += 1
        # Print a newline after each argument
        sys.stdout.write("\\n")
        i -= 1

if __name__ == "__main__":
    main()

```
