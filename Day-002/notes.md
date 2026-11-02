# Day 2 — Variables and Assigning Values

## 1. What is a Variable?

A variable is a named storage location used to store data in a Python program.

It works like a labelled box where we can store information and use it whenever required.

**Example:**
```python
name = "Ala Ganesh"
age = 23
```

Here:
- `name` and `age` are variable names.
- `"Ala Ganesh"` and `23` are their respective values.

## 2. Assigning Values to Variables

In Python, the assignment operator (`=`) is used to assign a value to a variable.

**Syntax:**
```python
variable_name = value
```

**Example:**
```python
student_name = "Ganesh"
graduation_year = 2026
```

Python stores the assigned values and allows us to access them using the variable names.

## 3. Types of Values Stored in Variables

Variables can store different types of information.

| Data Type | Example |
|---|---|
| String (`str`) | `name = "Ganesh"` |
| Integer (`int`) | `age = 23` |
| Float (`float`) | `percentage = 85.5` |
| Boolean (`bool`) | `is_student = True` |

## 4. Using Variables in Calculations

Variables can store numbers and participate in mathematical operations.

Python supports:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

**Example:**
```python
monthly_salary = 50000
monthly_expenses = 30000

monthly_savings = monthly_salary - monthly_expenses

print(monthly_savings)
```

**Output:** `20000`

## 5. Updating Variable Values

A variable's value can be changed during program execution.

**Example:**
```python
score = 50
print(score)

score = 80
print(score)
```

**Output:**
```text
50
80
```

The latest assigned value replaces the previous value.

## 6. Rules for Naming Variables

Python follows certain rules when creating variable names:

1. Variable names must begin with a letter or underscore (`_`).
2. They cannot begin with a number.
3. Spaces are not allowed in variable names.
4. Special characters such as `@`, `#`, and `-` are not allowed.
5. Python variable names are case-sensitive.
6. Reserved Python keywords cannot be used as variable names.

**Examples:**

| Correct | Incorrect |
|---|---|
| `student_name` | `student name` |
| `age` | `2age` |
| `total_marks` | `total-marks` |
| `graduation_year` | `class` |

## 7. Python Naming Convention — snake_case

Python commonly uses the `snake_case` naming convention.

In this convention, variable names are written in lowercase, with multiple words separated by underscores.

**Example:**
```python
student_name = "Ganesh"
monthly_salary = 50000
total_marks = 285
```

Meaningful variable names make programs easier to understand and maintain.

## 8. Displaying Variables Using print()

The `print()` function displays variable values on the screen.

**Using commas:**
```python
name = "Ganesh"
age = 23

print("My name is", name)
print("My age is", age)
```

**Using f-strings:**
```python
print(f"My name is {name}")
print(f"My age is {age}")
```

An f-string allows variables and expressions to be inserted directly inside a string using curly brackets `{}`.

## 9. Important Points to Remember

- Variables are used to store and reuse information.
- The `=` operator assigns values to variables.
- Variables can store different data types.
- Variable values can be updated.
- Variables can be used in mathematical calculations.
- Python is case-sensitive.
- Meaningful names improve code readability.
- f-strings make output formatting easier.

## Key Takeaway

Variables are one of the fundamental concepts in Python programming. They allow us to store information, perform calculations, update values, and build programs efficiently.

They are especially important in Data Science because datasets contain information such as names, ages, marks, prices, salaries, and other numerical values that we need to store and process.