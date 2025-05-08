# 1- WHAT IS A COMPILER?

A COMPILER is a special program that takes the code you write in a language like C or C++
and **translates it into machine code** — the low-level code that your computer can actually run.

The machine code is usually saved in an executable file (like `.exe` on Windows).

This process is called **compilation** — and it happens in several steps.

# I- STEPS OF COMPILATION

1. PREPROCESSING
   - Handles lines that start with #, like #include or #define
   - It includes necessary files and prepares the code before actual compilation.
2. COMPILING
   - Translates the preprocessed code into assembly language (a low-level language).
   - Checks for syntax errors (missing semicolons, typos, etc.)
3. ASSEMBLING
   - Converts the assembly code into machine code (binary instructions).
   - Creates an object file (.o or .obj)
4. LINKING
   - Combines your object file with other necessary code (like libraries).
   - Produces the final executable program................

```c
TEXT DIAGRAM

+------------------+
| Your Code        |   <- main.cpp
+------------------+
        |
        v
+------------------+
| Preprocessor     |   <- [Handles #include, #define, etc.]
+------------------+
|
v
+------------------+
| Compiler         |   <- [Converts to Assembly Language]
+------------------+
       |
       v
+------------------+
| Assembler        |   <- [Converts to Machine Code]
+------------------+
       |
       v
+------------------+
| Linker           |   <- [Combines object files & libraries]
+------------------+
       |
       v
+------------------+
| Final Program    |   <- main.exe or a.out
+------------------+

```
