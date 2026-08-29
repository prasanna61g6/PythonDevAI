"""
Python Error and File Handling

- Exception Handling
- File Handling
- JSON
- CSV

"""


# ==================== EXCEPTION HANDLING ====================

# An exception is a runtime error that interrupts
# the normal flow of a program.

try:
    number = int("100")
    print(number)

except ValueError:
    print("Invalid number.")


# Handling multiple exceptions

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Using a single except block for multiple exceptions

try:
    value = int("Python")

except (ValueError, TypeError) as error:
    print(f"An error occurred: {error}")


# The else block runs when no exception occurs.

try:
    number = int("25")

except ValueError:
    print("Invalid number.")

else:
    print(f"Conversion successful: {number}")


# The finally block always executes.

try:
    number = 10 / 2
    print(number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("This block always executes.")


# Catching an exception object

try:
    result = 10 / 0

except ZeroDivisionError as error:
    print(f"Error: {error}")


# ==================== RAISING EXCEPTIONS ====================

# raise allows us to manually generate an exception
# when invalid data is provided.

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount


try:
    remaining_balance = withdraw(5000, 2000)
    print(f"Remaining balance: {remaining_balance}")

except ValueError as error:
    print(error)


# ==================== CUSTOM EXCEPTIONS ====================

# Custom exceptions allow us to create errors
# specific to our application's requirements.

class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError(
            "Age must be 18 or above."
        )

    print("Age is valid.")


try:
    check_age(16)

except InvalidAgeError as error:
    print(error)


# ==================== FILE HANDLING ====================

# Files allow programs to store data permanently.

# Common file modes:
#
# "r"  -> Read
# "w"  -> Write (creates a file or overwrites existing content)
# "a"  -> Append
# "x"  -> Create a new file and fail if it already exists
#
# "rb" -> Read binary
# "wb" -> Write binary


# Writing to a file

with open("example.txt", "w") as file:
    file.write("Learning Python.\n")
    file.write("Learning Applied AI.\n")


# Reading the entire file

with open("example.txt", "r") as file:
    content = file.read()

print(content)


# ==================== READING FILES ====================

# read() reads the complete file.

with open("example.txt", "r") as file:
    content = file.read()

print(content)


# readline() reads one line at a time.

with open("example.txt", "r") as file:
    first_line = file.readline()

print(first_line)


# readlines() returns all lines as a list.

with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)


# Looping through a file is memory-efficient.

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


# ==================== APPENDING TO A FILE ====================

# "a" mode adds new content without removing existing content.

with open("example.txt", "a") as file:
    file.write("File handling is useful for storing data.\n")


# ==================== FILE NOT FOUND HANDLING ====================

try:
    with open("missing_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("The requested file does not exist.")


# ==================== JSON ====================

# JSON stands for JavaScript Object Notation.
# It is commonly used to exchange data between applications.

import json


# Python dictionary

student = {
    "name": "Prasanna",
    "branch": "AIML",
    "skills": [
        "Python",
        "Machine Learning",
        "Applied AI"
    ]
}


# Writing Python data to a JSON file

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


# Reading JSON data from a file

with open("student.json", "r") as file:
    student_data = json.load(file)

print(student_data)


# Accessing JSON data

print(student_data["name"])
print(student_data["skills"])


# ==================== JSON STRING CONVERSION ====================

# dumps() converts Python data into a JSON string.

data = {
    "language": "Python",
    "domain": "Applied AI"
}

json_string = json.dumps(data, indent=4)

print(json_string)


# loads() converts a JSON string into Python data.

json_data = """
{
    "name": "Prasanna",
    "role": "Applied AI Engineer"
}
"""

python_data = json.loads(json_data)

print(python_data)
print(python_data["role"])


# ==================== CSV ====================

# CSV stands for Comma-Separated Values.
# It is commonly used to store tabular data.

import csv


# Writing data to a CSV file

students = [
    ["Name", "Branch", "Score"],
    ["Prasanna", "AIML", 90],
    ["Alex", "CSE", 85],
    ["Sam", "ECE", 88]
]

with open(
    "students.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerows(students)


# Reading data from a CSV file

with open(
    "students.csv",
    "r"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# ==================== DICTIONARY CSV ====================

# DictWriter writes dictionaries to a CSV file.

employees = [
    {
        "name": "Prasanna",
        "role": "AI Engineer",
        "salary": 80000
    },
    {
        "name": "Alex",
        "role": "Backend Developer",
        "salary": 70000
    }
]

fieldnames = ["name", "role", "salary"]

with open(
    "employees.csv",
    "w",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(employees)


# Reading CSV data as dictionaries

with open(
    "employees.csv",
    "r"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"{row['name']} - "
            f"{row['role']} - "
            f"{row['salary']}"
        )


# ==================== PRACTICAL EXAMPLE ====================

# A simple function that saves user data
# into a JSON file.

def save_user(name, role, skills):
    user = {
        "name": name,
        "role": role,
        "skills": skills
    }

    with open("user.json", "w") as file:
        json.dump(user, file, indent=4)


def load_user():
    try:
        with open("user.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("User file does not exist.")
        return None

    except json.JSONDecodeError:
        print("User file contains invalid JSON.")
        return None


save_user(
    "Prasanna",
    "Applied AI Engineer",
    ["Python", "Machine Learning", "Generative AI"]
)

user = load_user()

if user:
    print(user["name"])
    print(user["role"])

    for skill in user["skills"]:
        print(skill)