# 1- INTRODUCTION TO LOOPS

### WHAT IS A LOOP?

A loop is a control structure that allows you to repeat a block of code multiple times as long as a condition is true. This helps avoid writing the same code again and again.

### WHY USE LOOPS?

- To repeat tasks (like printing numbers, checking input, etc.)
- To reduce code duplication
- To handle tasks that need many repeated steps

### TYPES OF LOOPS IN PYTHON

1. **FOR** loop → when the number of repetitions is known
2. **WHILE** loop → when the condition is checked before each repetition

### HOW A LOOP WORKS (using FOR loop as an example)

```abap
    ┌──────────────┐
    │ Initialization │ ← (i = 0)
    └──────┬───────┘
           ↓
   ┌──────────────┐
   │ Check Condition? │ ← (i <= 5)
   └──────┬───────┘
           ↓ Yes
    ┌──────────────┐
    │ Run Block Code │ ← (print(i))
    └──────┬───────┘
           ↓
    ┌──────────────┐
    │  Update Step   │ ← (i += 1)
    └──────┬───────┘
           ↓
        Repeat ↺
           ↓
        No → Exit loop

```

### EXAMPLE: print numbers from 0 to 5

```python
for i in range(6):  # Loop from 0 to 5
    print(i)  # This line repeats 6 times

```
