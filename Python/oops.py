"""
Python Object-Oriented Programming
- Classes and Objects
- Constructors
- Class and Instance Variables
- Public, Protected and Private Members
- Encapsulation
- Instance, Class and Static Methods
- Inheritance
- super() and Method Resolution Order
- Polymorphism
- Operator Overloading
- Abstraction
- Dunder Methods
- isinstance() and issubclass()

"""


# ==================== CLASSES AND OBJECTS ====================

# A class is a blueprint used to create objects.
# An object is an instance of a class.

class Student:
    def introduce(self):
        print("Hello, I am a student.")


student1 = Student()
student1.introduce()


# ==================== CONSTRUCTORS ====================

# __init__() is a constructor-like special method.
# It runs automatically when an object is created.

class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Branch: {self.branch}")


student1 = Student("Prasanna", 21, "AIML")
student1.display()


# ==================== INSTANCE AND CLASS VARIABLES ====================

# Instance variables belong to individual objects.
# Class variables are shared by all objects of the class.

class Employee:
    company = "PythonDevAI"  # Class variable

    def __init__(self, name, role):
        self.name = name      # Instance variable
        self.role = role      # Instance variable


employee1 = Employee("Prasanna", "AI Engineer")
employee2 = Employee("Alex", "Backend Developer")

print(employee1.name)
print(employee2.name)

print(Employee.company)
print(employee1.company)


# ==================== PUBLIC, PROTECTED AND PRIVATE ====================

# Python does not strictly enforce access modifiers like Java or C++.
#
# public_name     -> Public member
# _protected_name -> Protected by convention
# __private_name  -> Private using name mangling

class AccessExample:
    def __init__(self):
        self.public = "Accessible from anywhere"
        self._protected = "Intended for internal use or subclasses"
        self.__private = "Accessible inside the class"

    def show_private(self):
        return self.__private


example = AccessExample()

# Public member
print(example.public)

# Protected member
# It can still be accessed, but the underscore indicates
# that it should normally be treated as internal.
print(example._protected)

# Private member should be accessed through a method.
print(example.show_private())

# print(example.__private)  # This raises AttributeError.


# ==================== ENCAPSULATION ====================

# Encapsulation combines data and methods inside a class
# and controls how internal data is accessed or modified.

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Prasanna", 5000)

account.deposit(2000)
account.withdraw(1000)

print(account.get_balance())


# ==================== PROPERTY, GETTER AND SETTER ====================

# @property allows a method to be accessed like an attribute.
# A setter can validate data before updating it.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative.")


product = Product("Laptop", 50000)

print(product.price)

product.price = 55000
print(product.price)

product.price = -100


# ==================== INSTANCE, CLASS AND STATIC METHODS ====================

class Employee:
    company = "PythonDevAI"

    def __init__(self, name):
        self.name = name

    # Instance method:
    # Uses self and works with object-specific data.
    def display_name(self):
        print(f"Employee: {self.name}")

    # Class method:
    # Uses cls and works with class-level data.
    @classmethod
    def display_company(cls):
        print(f"Company: {cls.company}")

    # Static method:
    # Does not require self or cls.
    # It is placed inside the class because it is logically related.
    @staticmethod
    def is_valid_age(age):
        return age >= 18


employee = Employee("Prasanna")

employee.display_name()

Employee.display_company()

print(Employee.is_valid_age(21))


# ==================== SINGLE INHERITANCE ====================

# Inheritance allows a child class to reuse features
# from a parent class.

class Animal:
    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


dog = Dog()

dog.eat()
dog.bark()


# ==================== super() ====================

# super() is used to access methods or constructors
# from the parent class.

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch

    def display(self):
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")


student = Student("Prasanna", "AIML")
student.display()


# ==================== MULTILEVEL INHERITANCE ====================

class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")


class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")


class Child(Parent):
    def child_method(self):
        print("Child method")


child = Child()

child.grandparent_method()
child.parent_method()
child.child_method()


# ==================== MULTIPLE INHERITANCE ====================

# A class can inherit from more than one parent class.

class Father:
    def father_skill(self):
        print("Father's skill")


class Mother:
    def mother_skill(self):
        print("Mother's skill")


class Child(Father, Mother):
    def child_skill(self):
        print("Child's skill")


child = Child()

child.father_skill()
child.mother_skill()
child.child_skill()


# ==================== METHOD RESOLUTION ORDER ====================

# When multiple inheritance is used, Python follows the MRO
# to decide which method should be called first.

class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


object_d = D()

object_d.show()

# Python checks the classes according to Method Resolution Order.
print(D.mro())


# ==================== POLYMORPHISM ====================

# Polymorphism means the same method name or interface
# can behave differently for different objects.

class Animal:
    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")


class Cat(Animal):
    def sound(self):
        print("Cat meows.")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# ==================== METHOD OVERRIDING ====================

# Method overriding happens when a child class provides
# its own implementation of a parent class method.

class Employee:
    def work(self):
        print("Employee is working.")


class AIEngineer(Employee):
    def work(self):
        print("AI Engineer is building AI applications.")


engineer = AIEngineer()
engineer.work()


# ==================== DUCK TYPING ====================

# Python focuses on what an object can do rather than
# requiring it to belong to a specific class.

class Developer:
    def work(self):
        print("Writing code.")


class Designer:
    def work(self):
        print("Designing user interfaces.")


def start_work(person):
    person.work()


start_work(Developer())
start_work(Designer())


# ==================== OPERATOR OVERLOADING ====================

# Operator overloading allows operators such as +
# to work with user-defined objects.

class Vector:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Vector(self.value + other.value)

    def __str__(self):
        return f"Vector({self.value})"


vector1 = Vector(10)
vector2 = Vector(20)

result = vector1 + vector2

print(result)


# ==================== ABSTRACTION ====================

# Abstraction hides unnecessary implementation details
# and defines only the essential behavior.

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


credit_card = CreditCardPayment()
upi = UPIPayment()

credit_card.pay(1000)
upi.pay(500)


# ==================== DUNDER METHODS ====================

# Dunder means "double underscore".
# These special methods allow objects to work with
# built-in Python operations.

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def __str__(self):
        return f"{self.name} - {self.branch}"

    def __len__(self):
        return len(self.name)


student = Student("Prasanna", "AIML")

print(student)
print(len(student))


# ==================== isinstance() AND issubclass() ====================

class Vehicle:
    pass


class Car(Vehicle):
    pass


car = Car()

# Checks whether an object belongs to a class
# or its parent class.
print(isinstance(car, Car))
print(isinstance(car, Vehicle))

# Checks whether one class inherits from another.
print(issubclass(Car, Vehicle))
print(issubclass(Vehicle, Car))


# ==================== PRACTICAL OOP EXAMPLE ====================

# This example combines inheritance, encapsulation,
# polymorphism and class methods.

class Employee:
    company = "PythonDevAI"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def work(self):
        print(f"{self.name} is working.")

    @classmethod
    def get_company(cls):
        return cls.company


class AIEngineer(Employee):
    def work(self):
        print(f"{self.name} is building Applied AI applications.")


class BackendDeveloper(Employee):
    def work(self):
        print(f"{self.name} is developing backend systems.")


employees = [
    AIEngineer("Prasanna", "AI Engineer", 80000),
    BackendDeveloper("Alex", "Backend Developer", 70000)
]

for employee in employees:
    employee.work()
    print(f"Salary: {employee.get_salary()}")

print(Employee.get_company())