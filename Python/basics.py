"""
Python Basics
- Variables and Data Types
- Input and Output
- Type Casting
- Operators
- Strings

"""

# ==================== VARIABLES AND DATA TYPES ====================

# Variables store data.
name = "Prasanna"
age = 21
cgpa = 8.5
is_learning_python = True
future_goal = None

print(name)
print(age)
print(cgpa)
print(is_learning_python)
print(future_goal)

# Python is dynamically typed.
value = 100
print(value, type(value))

value = "Python"
print(value, type(value))

# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Assigning the same value
a = b = c = 100
print(a, b, c)

# Numeric data types
integer_number = 10
float_number = 10.5
complex_number = 2 + 3j

print(type(integer_number))
print(type(float_number))
print(type(complex_number))

# Boolean
is_python_fun = True
is_exam_finished = False

print(type(is_python_fun))
print(type(is_exam_finished))

# None
result = None
print(result, type(result))

# Type checking
number = 25

print(isinstance(number, int))
print(isinstance(number, str))

# Object identity
language = "Python"
print(id(language))


# ==================== INPUT AND OUTPUT ====================

# Basic output
print("Hello, Python!")
print("Learning Python for Applied AI")

# Printing multiple values
student_name = "Prasanna"
technology = "Python"

print(student_name, technology)

# sep
print("Python", "Applied AI", "Engineering", sep=" | ")

# end
print("Hello", end=" ")
print("Machha")

# String formatting
name = "Prasanna"
domain = "PythonDevAI"

print("Name:", name, "Domain:", domain)
print("Name: {}, Domain: {}".format(name, domain))
print(f"Name: {name}, Domain: {domain}")

# Formatting expressions
score = 85
total = 100

print(f"Score: {score}/{total}")
print(f"Percentage: {(score / total) * 100:.2f}%")

# input() always returns a string.
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

user_age = int(input("Enter your age: "))
print(f"Next year, you will be {user_age + 1}.")


# ==================== TYPE CASTING ====================

# Implicit type conversion
integer_value = 10
float_value = 5.5

result = integer_value + float_value

print(result)
print(type(result))

# String to integer
number_as_string = "100"

converted_number = int(number_as_string)

print(converted_number)
print(type(converted_number))

# Integer to float
number = 25

converted_float = float(number)

print(converted_float)
print(type(converted_float))

# Number to string
number = 500

converted_string = str(number)

print(converted_string)
print(type(converted_string))

# Float to integer
# int() removes the decimal part; it does not round.
price = 99.99

integer_price = int(price)

print(integer_price)

# Boolean conversion
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2, 3]))


# ==================== OPERATORS ====================

a = 10
b = 3

# Arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical operators
is_student = True
has_id_card = True

print(is_student and has_id_card)
print(is_student or has_id_card)
print(not is_student)

# Assignment operators
number = 10

number += 5
print(number)

number -= 2
print(number)

number *= 2
print(number)

number //= 3
print(number)

# Membership operators
languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("JavaScript" not in languages)

# Identity operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x == z)

# Bitwise operators
x = 5
y = 3

print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << 1)
print(x >> 1)


# ==================== STRINGS ====================

# Creating strings
language = "Python"
message = "Applied AI Engineer"

multi_line_text = """
Python is widely used in:
- Artificial Intelligence
- Machine Learning
- Data Science
- Automation
"""

print(language)
print(message)
print(multi_line_text)

# Indexing
word = "Python"

print(word[0])
print(word[1])
print(word[-1])
print(word[-2])

# Slicing
print(word[0:3])
print(word[:4])
print(word[2:])
print(word[::2])
print(word[::-1])

# Strings are immutable.
language = "Python"

# language[0] = "J"  # This causes an error.

new_language = "J" + language[1:]
print(new_language)

# String methods
text = "  python for applied ai  "

print(text.upper())
print(text.lower())
print(text.strip())
print(text.title())

# Searching
sentence = "Python is powerful and Python is popular"

print(sentence.find("Python"))
print(sentence.count("Python"))
print("powerful" in sentence)

# Replacing
updated_sentence = sentence.replace("Python", "Py")
print(updated_sentence)

# Splitting
skills = "Python,Machine Learning,AI,Data Science"

skill_list = skills.split(",")
print(skill_list)

# Joining
joined_skills = " | ".join(skill_list)
print(joined_skills)

# f-string
name = "Prasanna"
role = "Applied AI Engineer"

introduction = f"My name is {name} and I am becoming an {role}."
print(introduction)

# String validation methods
username = "PythonDevAI123"

print(username.isalpha())
print(username.isnumeric())
print(username.isalnum())
print(username.islower())
print(username.isupper())