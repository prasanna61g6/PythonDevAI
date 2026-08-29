"""
Python Functions
- Basic Functions
- Function Arguments
- Lambda Functions
- Recursion
- Map, Filter and Reduce

"""


# ==================== BASIC FUNCTIONS ====================

# Defining and calling a function
def greet():
    print("Hello, Python!")


greet()


# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Prasanna")


# Function with a return value
def add(a, b):
    return a + b


result = add(10, 20)
print(result)


# Returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b


addition, subtraction, multiplication = calculate(10, 5)

print(addition)
print(subtraction)
print(multiplication)


# Function without an explicit return
def show_message():
    print("This function does not explicitly return a value.")


result = show_message()
print(result)  # None


# ==================== FUNCTION ARGUMENTS ====================

# Positional arguments
def introduce(name, age):
    print(f"Name: {name}, Age: {age}")


introduce("Prasanna", 21)


# Keyword arguments
introduce(age=21, name="Prasanna")


# Default arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Prasanna")


# Mixing positional and keyword arguments
def student_info(name, age, branch):
    print(f"{name} | {age} | {branch}")


student_info("Prasanna", branch="AIML", age=21)


# *args
# Collects multiple positional arguments into a tuple.
def find_sum(*numbers):
    return sum(numbers)


print(find_sum(10, 20))
print(find_sum(10, 20, 30, 40))


# **kwargs
# Collects multiple keyword arguments into a dictionary.
def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_info(
    name="Prasanna",
    branch="AIML",
    skill="Python"
)


# Combining normal arguments, *args and **kwargs
def example(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)


example(
    10,
    20,
    30,
    40,
    language="Python",
    domain="Applied AI"
)


# ==================== VARIABLE SCOPE ====================

# Local scope
def local_scope():
    message = "I exist only inside this function."
    print(message)


local_scope()


# Global scope
language = "Python"


def show_language():
    print(language)


show_language()


# Using the global keyword
count = 0


def increment():
    global count
    count += 1


increment()
print(count)


# LEGB Rule:
# Local -> Enclosing -> Global -> Built-in

def outer():
    message = "Enclosing"

    def inner():
        message = "Local"
        print(message)

    inner()
    print(message)


outer()


# ==================== LAMBDA FUNCTIONS ====================

# Lambda function with one argument
square = lambda number: number ** 2

print(square(5))


# Lambda function with multiple arguments
add = lambda a, b: a + b

print(add(10, 20))


# Lambda with a conditional expression
maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))


# Lambda with sorted()
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)


# ==================== RECURSION ====================

# A recursive function calls itself.
# It must have a base case to stop recursion.


# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(8):
    print(fibonacci(i), end=" ")

print()


# Sum of numbers using recursion
def recursive_sum(n):
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)


print(recursive_sum(10))


# ==================== MAP ====================

# map() applies a function to every item in an iterable.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print(squares)


# Using a normal function with map()
def cube(number):
    return number ** 3


cubes = list(map(cube, numbers))

print(cubes)


# ==================== FILTER ====================

# filter() selects elements based on a condition.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)


# Filtering strings
languages = ["Python", "C", "Java", "Go"]

long_names = list(
    filter(lambda language: len(language) > 2, languages)
)

print(long_names)


# ==================== REDUCE ====================

# reduce() repeatedly applies a function to reduce
# an iterable to a single value.

from functools import reduce


numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


# Finding the maximum value using reduce
maximum = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(maximum)


# ==================== PRACTICAL EXAMPLES ====================

# Calculate the average of numbers
def average(*numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


print(average(80, 90, 75, 95))


# Check whether a number is even
def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


# Apply discount using a function
def apply_discount(price, discount=10):
    return price - (price * discount / 100)


print(apply_discount(1000))
print(apply_discount(1000, 20))


# Filter passing scores
scores = [35, 45, 50, 67, 80, 42, 90]

passing_scores = list(
    filter(lambda score: score >= 50, scores)
)

print(passing_scores)