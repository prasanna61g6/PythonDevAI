"""
Python Data Structures
- Lists
- Tuples
- Sets
- Dictionaries
- Comprehensions

"""


# ==================== LISTS ====================

# Lists are ordered, mutable, and allow duplicate values.
languages = ["Python", "Java", "C++", "Python"]

print(languages)

# Indexing
print(languages[0])
print(languages[-1])

# Slicing
print(languages[1:3])
print(languages[::-1])

# Modifying elements
languages[1] = "JavaScript"

# Adding elements
languages.append("SQL")
languages.insert(1, "Machine Learning")
languages.extend(["AI", "Data Science"])

print(languages)

# Removing elements
languages.remove("Python")
removed_item = languages.pop()

print(removed_item)
print(languages)

# Useful operations
numbers = [50, 10, 40, 20, 30]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# Copying lists
original = [1, 2, 3]

reference = original
copied_list = original.copy()

original.append(4)

print(reference)
print(copied_list)

# Nested lists
students = [
    ["Alice", 85],
    ["Bob", 90],
    ["Charlie", 78]
]

print(students[0])
print(students[0][0])


# ==================== TUPLES ====================

# Tuples are ordered and immutable.
coordinates = (10, 20, 30, 20)

print(coordinates)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:3])

# Tuple methods
print(coordinates.count(20))
print(coordinates.index(30))

# Tuple packing
student = "Prasanna", 21, "AIML"

# Tuple unpacking
name, age, branch = student

print(name)
print(age)
print(branch)

# Extended unpacking
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Single-element tuple
single_value = (10,)
print(type(single_value))


# ==================== SETS ====================

# Sets are unordered collections that store unique values.
numbers = {1, 2, 3, 4, 4, 5}

print(numbers)

# Adding elements
numbers.add(6)
numbers.update([7, 8])

print(numbers)

# Removing elements
numbers.remove(8)
numbers.discard(100)  # No error if the element does not exist.

print(numbers)

# Set operations
python_skills = {"Python", "Machine Learning", "SQL"}
ai_skills = {"Machine Learning", "Deep Learning", "Python"}

print(python_skills | ai_skills)   # Union
print(python_skills & ai_skills)   # Intersection
print(python_skills - ai_skills)   # Difference
print(python_skills ^ ai_skills)   # Symmetric difference

# Membership
print("Python" in python_skills)

# Removing duplicates
values = [1, 2, 2, 3, 4, 4, 5]
unique_values = list(set(values))

print(unique_values)


# ==================== DICTIONARIES ====================

# Dictionaries store data as key-value pairs.
student = {
    "name": "Prasanna",
    "age": 21,
    "branch": "AIML",
    "skills": ["Python", "C++"]
}

print(student)

# Accessing values
print(student["name"])
print(student.get("college", "Not Available"))

# Adding and updating values
student["college"] = "Engineering College"
student["age"] = 22

print(student)

# Removing values
student.pop("college")

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Iterating through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionaries
students = {
    "student_1": {
        "name": "Alice",
        "score": 85
    },
    "student_2": {
        "name": "Bob",
        "score": 90
    }
}

print(students["student_1"]["name"])

# Copying a dictionary
original = {"Python": 1, "Java": 2}
copied = original.copy()

original["C++"] = 3

print(copied)


# ==================== COMPREHENSIONS ====================

# List comprehension
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print(squares)

# List comprehension with a condition
even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)

# Transforming values
languages = ["python", "java", "c++"]

uppercase_languages = [
    language.upper()
    for language in languages
]

print(uppercase_languages)

# Nested list comprehension
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

flattened = [
    value
    for row in matrix
    for value in row
]

print(flattened)

# Set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_squares = {number ** 2 for number in numbers}

print(unique_squares)

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]

square_dictionary = {
    number: number ** 2
    for number in numbers
}

print(square_dictionary)

# Dictionary comprehension with a condition
even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_squares)


# ==================== PRACTICAL EXAMPLES ====================

# Word frequency counter
text = "python is powerful and python is easy"

frequency = {}

for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# Finding common elements
list_one = [1, 2, 3, 4, 5]
list_two = [4, 5, 6, 7, 8]

common_elements = list(set(list_one) & set(list_two))

print(common_elements)

# Filtering dictionary data
scores = {
    "Alice": 85,
    "Bob": 45,
    "Charlie": 90,
    "David": 50
}

passed_students = {
    name: score
    for name, score in scores.items()
    if score >= 50
}

print(passed_students)