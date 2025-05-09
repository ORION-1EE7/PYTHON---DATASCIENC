# 4- VARIABLES NAMING RULES AND BEST PRACTICES

**I- NAMING RULES**

1. Must be unique.
2. Case sensitive.
3. Must start with a letter or an underscore.
4. Cannot start with numbers.
5. No white space or special characters.
6. Reserved keywords are not allowed (e.g., class, public, int, etc.).

**II- BEST PRACTICES**

1. Name should relate to the variable's purpose.
2. Writing styles for multi-word variable names:
A. **camelCase:** First word lowercase, next words start with uppercase.
B. **snake\_case:** All lowercase, words separated by underscores.
C. **PascalCase:** Every word starts with an uppercase letter.
D. **SCREAMING\_CASE:** All uppercase, words separated by underscores (often used for constants).

**EXAMPLE CODE:**

```python
def main():
    # NAMING RULES EXAMPLES
    age = 10
    Age = 20  # Different from 'age' (case-sensitive)
    _age = 30
    age2 = 40
    # Invalid examples (would cause errors if uncommented)
    # 2age = 50      # ❌ Starts with a number
    # age$ = 60      # ❌ Special character not allowed
    # class = 70     # ❌ Reserved keyword

    # print (int(int))
    # BEST PRACTICES EXAMPLES

    # 1. Name related to purpose
    student_age = 18  # Good: name describes the value

    # 2. Writing styles

    # A. camelCase
    age_of_student = 19
    print(f"camelCase: {age_of_student}")

    # B. snake_case
    age_of_student = 20
    print(f"snake_case: {age_of_student}")

    # C. PascalCase
    AgeOfStudent = 21
    print(f"PascalCase: {AgeOfStudent}")

    # D. SCREAMING_CASE (often used for constants)
    AGE_OF_STUDENT = 22
    print(f"SCREAMING_CASE: {AGE_OF_STUDENT}")

    print(int)

if __name__ == "__main__":
    main()

```