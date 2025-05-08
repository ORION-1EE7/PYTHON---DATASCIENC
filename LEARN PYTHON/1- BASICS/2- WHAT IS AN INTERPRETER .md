# 2- WHAT IS AN INTERPRETER?

An **INTERPRETER** is a program that reads and executes code line by line, instead of translating the whole program at once like a compiler.

> Imagine you're reading a book aloud to someone — each time you read a line, the listener understands it immediately.
This is similar to how an interpreter works.
> 

### INTERPRETER vs COMPILER

- A **compiler** translates the whole program into machine code **before** running it.
- An **interpreter** reads the code and runs it **line by line**, translating it on the fly.

## HOW DOES AN INTERPRETER WORK?

1. The interpreter reads the first line of code.
2. It translates that line into machine code and executes it.
3. The interpreter then moves to the next line of code and repeats the process.
4. This continues until the program finishes.

## EXAMPLE OF INTERPRETER

**Python Program (`my_program.py`)**
→

```
+------------------+
| Interpreter      |  ← Reads and executes line by line
+------------------+
        ↓
+-------------------------------+
| Line 1: print("Hello, world!") |  ← Executes and prints
+-------------------------------+
        ↓
+------------------+
| Line 2: (Next line)           |  ← Continues to next line
+------------------+
        ↓
Continue until program ends...

```

## NOTES

**INTERPRETERS** are generally **slower** than compilers because they translate and execute the code line by line.

However, they are also:

- **More flexible**
- **Easier for debugging**, since they allow you to test code in small chunks without compiling the whole program.