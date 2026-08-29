"""
Python Control Flow
- Conditional Statements
- For Loops
- While Loops
- Break, Continue and Pass
- Loop Else
- Nested Loops
- Basic Logic Programs
- Pattern Problems

"""


# ==================== CONDITIONAL STATEMENTS ====================

# Simple if statement
age = 21

if age >= 18:
    print("You are eligible to vote.")


# if-else statement
number = 7

if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")


# if-elif-else statement
score = 85

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Score: {score}, Grade: {grade}")


# Nested if statement
username = "pythondevai"
password = "python123"

if username == "pythondevai":
    if password == "python123":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")


# Multiple conditions using logical operators
age = 21
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")


# Conditional expression / Ternary operator
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(f"{number} is {result}")


# ==================== FOR LOOPS ====================

# Looping through a list
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)


# range()
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(2, 11, 2):
    print(i)


# Looping through a string
word = "Python"

for character in word:
    print(character)


# enumerate()
skills = ["Python", "Machine Learning", "Applied AI"]

for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")


# zip()
students = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for student, score in zip(students, scores):
    print(f"{student}: {score}")


# ==================== WHILE LOOPS ====================

# Basic while loop
count = 1

while count <= 5:
    print(count)
    count += 1


# Countdown
count = 5

while count > 0:
    print(count)
    count -= 1

print("Go!")


# ==================== BREAK, CONTINUE AND PASS ====================

# break stops the loop immediately
for number in range(1, 10):
    if number == 5:
        break

    print(number)


# continue skips the current iteration
for number in range(1, 6):
    if number == 3:
        continue

    print(number)


# pass acts as a placeholder when no action is required
for number in range(3):
    pass


# ==================== LOOP ELSE ====================

# The else block executes when the loop completes normally.
# It does not execute if the loop ends with break.

for number in range(1, 4):
    print(number)
else:
    print("Loop completed successfully")


# Searching for an item using loop else
target = "Python"
skills = ["C", "Java", "Python", "C++"]

for skill in skills:
    if skill == target:
        print(f"{target} found!")
        break
else:
    print(f"{target} not found")


# ==================== NESTED LOOPS ====================

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")


# ==================== BASIC LOGIC PROGRAMS ====================

# Sum of first n natural numbers
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print(total)


# Factorial
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)


# Fibonacci series
terms = 8
first, second = 0, 1

for _ in range(terms):
    print(first, end=" ")
    first, second = second, first + second

print()


# Prime number check
number = 29

if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not prime")
            break
    else:
        print(f"{number} is prime")
else:
    print(f"{number} is not prime")


# ==================== PATTERN PROBLEMS ====================

rows = 5


# Right triangle
# *
# **
# ***
# ****
# *****

for i in range(1, rows + 1):
    print("*" * i)


# Inverted triangle
# *****
# ****
# ***
# **
# *

for i in range(rows, 0, -1):
    print("*" * i)


# Number triangle
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Pyramid
#     *
#    ***
#   *****
#  *******
# *********

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)