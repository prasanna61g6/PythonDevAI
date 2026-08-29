"""
Advanced Python

- Iterators
- Generators
- Decorators
- Modules and Packages

"""


# ==================== ITERATORS ====================

# An iterable is an object that can be iterated over.
# Examples: list, tuple, string, set, and dictionary.

numbers = [10, 20, 30]

for number in numbers:
    print(number)


# iter() creates an iterator from an iterable.

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Calling next(iterator) again would raise StopIteration.


# A for loop internally uses iter() and next().

for number in numbers:
    print(number)


# Creating a custom iterator.

class CountUpTo:
    def __init__(self, maximum):
        self.maximum = maximum
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.maximum:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


counter = CountUpTo(5)

for number in counter:
    print(number)


# ==================== GENERATORS ====================

# A generator produces values one at a time instead of
# storing all values in memory at once.

def count_up_to(maximum):
    current = 1

    while current <= maximum:
        yield current
        current += 1


generator = count_up_to(5)

print(next(generator))
print(next(generator))

for number in generator:
    print(number)


# A generator can also be iterated using a for loop.

for number in count_up_to(5):
    print(number)


# Generator expression.
# Similar to list comprehension, but uses parentheses.

squares = (number ** 2 for number in range(1, 6))

for square in squares:
    print(square)


# yield from can delegate yielding values from another iterable.

def combined_numbers():
    yield from [1, 2, 3]
    yield from [4, 5, 6]


for number in combined_numbers():
    print(number)


# Practical generator example.
# Generates even numbers up to a given limit.

def generate_even_numbers(limit):
    for number in range(0, limit + 1, 2):
        yield number


for number in generate_even_numbers(10):
    print(number)


# ==================== ITERATORS VS GENERATORS ====================

# Custom iterators usually require implementing:
# __iter__() and __next__()
#
# Generators use the yield keyword and Python automatically
# handles iterator behavior.

# A generator object can only move forward.
# Once a value is consumed, it cannot be retrieved again.

generator = (number for number in range(3))

print(next(generator))
print(next(generator))
print(next(generator))


# ==================== DECORATORS ====================

# A decorator adds or modifies the behavior of a function
# without changing the original function's code.

def simple_decorator(function):
    def wrapper():
        print("Before the function runs")
        function()
        print("After the function runs")

    return wrapper


@simple_decorator
def greet():
    print("Hello, Prasanna!")


greet()


# The above is equivalent to:
#
# greet = simple_decorator(greet)


# Decorator with function arguments.

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Finished function: {function.__name__}")

        return result

    return wrapper


@logging_decorator
def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# ==================== functools.wraps ====================

# wraps() preserves metadata such as the original
# function name and documentation.

from functools import wraps


def logging_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Running {function.__name__}")

        return function(*args, **kwargs)

    return wrapper


@logging_decorator
def multiply(a, b):
    """Returns the multiplication of two numbers."""
    return a * b


print(multiply(5, 4))
print(multiply.__name__)


# ==================== DECORATOR WITH ARGUMENTS ====================

# A decorator can itself accept arguments.
# This requires an additional outer function.

def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello!")


say_hello()


# ==================== PRACTICAL DECORATOR EXAMPLE ====================

# This decorator measures how long a function takes to run.

import time


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        print(
            f"{function.__name__} took "
            f"{end_time - start_time:.6f} seconds"
        )

        return result

    return wrapper


@measure_time
def calculate_sum(limit):
    return sum(range(limit))


print(calculate_sum(1_000_000))


# ==================== MODULES ====================

# A module is a Python file containing reusable code.

# Example module: calculator.py
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
#
# Another Python file can import it using:
#
# import calculator
# print(calculator.add(10, 20))


# Importing specific functions.
#
# from calculator import add, subtract
#
# print(add(10, 20))


# Importing with an alias.
#
# import calculator as calc
#
# print(calc.add(10, 20))


# Python also provides built-in modules.

import math
import random


print(math.sqrt(25))
print(math.factorial(5))

print(random.randint(1, 10))


# ==================== __name__ AND __main__ ====================

# When a Python file is executed directly,
# __name__ becomes "__main__".
#
# When the file is imported,
# __name__ contains the module name.

def main():
    print("This code runs when the file is executed directly.")


if __name__ == "__main__":
    main()


# ==================== PACKAGES ====================

# A package is a directory that groups related Python modules.

# Example structure:
#
# project/
# │
# ├── main.py
# │
# └── utilities/
#     ├── __init__.py
#     ├── calculator.py
#     └── text_tools.py
#
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
#
# main.py
#
# from utilities.calculator import add
#
# print(add(10, 20))


# ==================== IMPORT STYLES ====================

# Import an entire module:
#
# import math
# print(math.sqrt(16))


# Import a specific item:
#
# from math import sqrt
# print(sqrt(16))


# Import with an alias:
#
# import math as m
# print(m.sqrt(16))


# Avoid using:
#
# from module import *
#
# because it can create naming conflicts.


# ==================== PRACTICAL EXAMPLE ====================

# A generator processes data one item at a time.

def process_scores(scores):
    for score in scores:
        if score >= 50:
            yield score


scores = [35, 78, 45, 90, 50, 42, 88]

passing_scores = process_scores(scores)

for score in passing_scores:
    print(f"Passing score: {score}")


# A decorator can add logging behavior to functions.

def log_function_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Executing: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Completed: {function.__name__}")

        return result

    return wrapper


@log_function_call
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


scores = [80, 85, 90, 95]

average = calculate_average(scores)

print(f"Average: {average}")