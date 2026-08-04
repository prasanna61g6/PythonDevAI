# import array as arr
# import math
# from functools import reduce

# ------------------------------------------------------------ SET 01 ----------------------------------------------------------------------------
# ------------------------------------------------ 1.1 -----------------------------------------------------------------
# user_input = input("Enter integers separated by space: ")
# numbers = list(map(int, user_input.split()))

# total_runs = 0
# highest_runs = float('-inf')
# lowest_runs = float('inf')
# average = 0
# cnt = 0
# n = len(numbers)
# bytes_used = n * 4

# for i in range(0, n):
#     total_runs += numbers[i]
#     highest_runs = max(highest_runs, numbers[i])
#     lowest_runs = min(lowest_runs, numbers[i])
#     if(numbers[i] == 0):
#         cnt = cnt + 1

# average = total_runs / n
# print("Total runs: ", total_runs)
# print("Highest over: ", highest_runs)
# print("Lowest over: ", lowest_runs)
# print("Average per over: ",average)
# print("Maiden overs: ", cnt)
# print("Bytes used: ", bytes_used)

# ----------------------------------------------- 1.2 ------------------------------------------------------------------
# user_input = input("Enter integers separated by space: ")
# numbers = list(map(int, user_input.split()))

# my_array = arr.array('i', numbers)

# my_array.append(60)
# print("After append: ", my_array)

# my_array.insert(1, 15)
# print("After insert: ", my_array)

# my_array.remove(30)
# print("After remove: ", my_array)

# my_array.pop(0)
# print("After pop: ", my_array)
# print("After reverse: ", my_array[::-1])

# ----------------------------------------------- 1.3 ------------------------------------------------------------------
# user_input = input("Enter integers separated by space: ")
# numbers = list(map(int, user_input.split()))

# maxi1 = float('-inf')
# maxi2 = float('-inf')

# n = len(numbers)

# for i in range(0, n):
#     if numbers[i] > maxi1 :
#         maxi2 = maxi1  
#         maxi1 = numbers[i]
#     elif numbers[i] > maxi2 and numbers[i] != maxi1 :
#         maxi2 = numbers[i]

# if maxi2 != float('-inf') :
#     print("Second largest = ", maxi2)
# else:
#     print("No second largest")

# ---------------------------------------------- 1.4 -------------------------------------------------------------------
# user_input = input("Enter integers separated by space: ")
# numbers = list(map(int, user_input.split()))

# k = int(input("Enter nunber of rotations required: "))

# d = 0
# while(d < k):
#     temp = numbers[0]
#     numbers.pop(0)
#     numbers.append(temp)
#     d = d + 1

# print(numbers)

# ---------------------------------------------- 1.5 -------------------------------------------------------------------
# user_input1 = input("Enter integers separated by space for first array: ")
# numbers1 = list(map(int, user_input1.split()))

# user_input2 = input("Enter integers separated by space for second array: ")
# numbers2 = list(map(int, user_input2.split()))

# total_length = len(numbers1) + len(numbers2)
# answer = [0] * total_length

# i = 0
# j = 0
# k = 0
# while(i < len(numbers1) and j < len(numbers2)):
#     if(numbers1[i] < numbers2[j]):
#         answer[k] = numbers1[i]
#         k = k + 1
#         i = i + 1
#     elif(numbers1[i] > numbers2[j]):
#         answer[k] = numbers2[j]
#         k = k + 1
#         j = j + 1
#     else:
#         answer[k] = numbers1[i]
#         k = k + 1
#         answer[k] = numbers2[j]
#         i = i + 1
#         j = j + 1
#         k = k + 1

# while(i < len(numbers1)):
#     answer[k] = numbers1[i]
#     k = k + 1
#     i = i + 1
# while(j < len(numbers2)):
#     answer[k] = numbers2[j]
#     k = k + 1
#     j = j + 1

# print(answer)

# ------------------------------------------------------------ SET 02 ----------------------------------------------------------------------------
#------------------------------------------------- 2.1 -----------------------------------------------------------------
# def place_order(customer, *items, **charges):
#     print("Customer: ", customer)
#     print(f"Items ordered {len(items)}: ")
#     for i in range(0, len(items)):
#         print(f"{i + 1}.{items[i]}")
#     print("Charges: ")
#     for key, value in charges.items():
#         print(f"{key} : {value}")

# place_order("Ravi", "Biryani", "Coke", "Gulab jam", delivery = 40, gst = 25, discount = 50)

# ------------------------------------------------ 2.2 -----------------------------------------------------------------
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# choice = input("Enter the operator: ")
# if b == 0 and choice == '/' :
#     print("Error : cannot divide by zero")
# else:
#     match choice:
#         case '+' :
#             print(a + b)
#         case '-' :
#             print(a - b)
#         case '*' :
#             print(a * b)
#         case '/' :
#             print(a / b)
#         case _ :
#             print(f"Error: unknow operator {choice}")

# ------------------------------------------------ 2.3 -----------------------------------------------------------------
# def build_query(**filters):
#     a = ""
#     for key, value in filters.items():
#         a += f"{key} = {value}&"
#     if a != "" :
#         print(a)
#     else:
#         print("empty string")

# d = {}
# n = int(input())
# for i in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     d[key] = value

# build_query(**d)

# ------------------------------------------------ 2.4 -----------------------------------------------------------------
# def add_to_cart(item):
#     cart = []
#     cart.append(item)
#     return cart

# print(add_to_cart("pen"))
# print(add_to_cart("book"))
# print(add_to_cart("bag"))

# """ The bug is that the default list is created only once, so every function call shares the same list
#      to fix this create a new list inside the function """

# ------------------------------------------------- 2.5 ----------------------------------------------------------------
# def report(name, m, section, year):
#     print("Student: ", name)
#     print("Section: ", section)
#     print("Year: ", year)
#     print("Marks: ", m)
#     total_marks = 0
#     for i in range(0, len(m)):
#         total_marks += m[i]
#     print("Total: ", total_marks)
#     print("Average: ", total_marks / len(m))
#     if(total_marks/len(m) >= 40):
#         print("PASS")
#     else:
#         print("FAIL")

# name = input("Enter a name: ")
# marks = input("Enter marks: ")
# m = list(map(int, marks.split()))
# section = input("Enter a section: ")
# year = int(input("Enter year: "))

# report(name, m, section, year)

# -------------------------------------------------- 2.6 ---------------------------------------------------------------
# commet : 
# 1, [1], (), {}
# 2, [9, 2], (), {}
# 3, [1, 3], (), {}
# 4, [7, 4], (8, 9), {'x' : 10}

# def mystery(a, b = [], *c, **d):
#     b.append(a)
#     return a, b, c, d

# print(mystery(1))
# print(mystery(2, [9]))
# print(mystery(3))
# print(mystery(4, [7], 8, 9, x = 10))

# ------------------------------------------------------------ SET 03 ----------------------------------------------------------------------------
# -------------------------------------------------- 3.1 ---------------------------------------------------------------
# Puzzle A
# comment:
# 10
# 20

# Puzzle B
# comment:
# 5

# Puzzle C
# comment :
# enclosing

# Puzzle D
# comment:
# 99

# x = 10
# def f():
#     global x
#     print(x)
#     x = 20
# f()
# print(x)

# x = 5
# def f(x):
#     x = 10
# f(x)
# print(x)

# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         print(x)
#     inner()
# outer()

# --------------------------------------------------- 3.2 --------------------------------------------------------------
# Total_seats = int(input("Enter total number of seats: "))
# Available_seats = Total_seats
# def book(n):
#     global Total_seats

#     if(n <= Total_seats):
#         Total_seats = Total_seats - n
#         print(f"Booked {n} seats.Remaining: {Total_seats}")
#     else:
#         print(f"Only {Total_seats} seats left.Booking failed")

# def cancel(n):
#     global Total_seats
#     Total_seats = Total_seats + n
#     print(f"Cancelled {n} seats. Remaining: {Total_seats}")

# def status():
#     print(f"{Total_seats} seats available out of {Available_seats}")

# book(3)
# book(10)
# book(200)
# cancel(5)
# status()

# ----------------------------------------------------- 3.3 ------------------------------------------------------------
# version A
# count = 0
# def outer():
#     global count
#     count += 1
#     return count
# c = outer
# print("Version A:", c(), c(), c())

# version B
# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
# c = outer()
# print("Version B:", c(), c(), c())
# """ Non-local is more safer because the variable is hidden inside the function and cannot be modified directly from outside
#         moreover a global variable can be changed by any part of the program which might lead to bugs """

# ------------------------------------------------------ 3.4 -----------------------------------------------------------
# L - Local variable
# E - Enclosing variable
# G - Global variable
# B - Built-in

# msg = "I am global"     # Global
# def outer():
#     msg = "I am enclosing"     # Enclosing
#     def inner():
#         msg = "I am local"     # Local
#         print("Local     :", msg)
#         print("Enclosing :", outer_msg)
#         print("Global    :", globals()["msg"])
#         print("Built-in  :", len("hello"))
#     outer_msg = msg
#     inner()
# outer()

#  -------------------------------------------------------- SET 07 ------------------------------------------------------------------------------
#  -------------------------------------------------- 7.1 -------------------------------------------------------------
# def apply_twice(fun, val):
#     return fun(fun(val))

# fun1 = lambda x: x + 3
# print(apply_twice(fun1, 10))   

# fun2 = lambda x: x * 2
# print(apply_twice(fun2, 5))

# fun3 = lambda x: x.upper()
# print(apply_twice(fun3, "hi"))
    
# ------------------------------------------------- 7.2 ----------------------------------------------------------------
# def compose(f, g):
#     return lambda x: f(g(x))

# add_one = lambda x: x + 1
# double = lambda x: x * 2

# f = compose(add_one, double)
# print(f(5))

# g = compose(double, add_one)
# print(g(5))

# # ------------------------------------------------- 7.3 --------------------------------------------------------------
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def pro(a, b):
#     return a * b
# def div(a, b):
#     return a / b 

# dict = {
#     '+' : add,
#     '-' : sub,
#     '*' : pro,
#     '/' : div
# }

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# operator = input("Enter the Operator: ")

# if operator in dict :
#     print(dict[operator](num1, num2))
# else :
#     print(f'Unknown Operator: {operator}')
    
# ------------------------------------------------------- 7.4 ----------------------------------------------------------
# players = [
#     {"name": "Kohli",   "runs": 741, "team": "RCB"},
#     {"name": "Gill",    "runs": 890, "team": "GT"},
#     {"name": "Rahul",   "runs": 616, "team": "LSG"},
#     {"name": "Jaiswal", "runs": 625, "team": "RR"},
#     {"name": "Samson",  "runs": 616, "team": "RR"}
# ]

# print("By runs (high to low):")
# res1 = sorted(players, key = lambda item: item['runs'], reverse = True)
# for i in range(0, len(players)):
#     print(f'{res1[i]["name"]}  {res1[i]["runs"]}')

# print("By team, then runs (high to low):")
# res2 = sorted(players, key = lambda item: (item['team'], -item['runs']))
# for i in range(0, len(players)):
#     print(f'{res2[i]["team"]}  {res2[i]["name"]}  {res2[i]["runs"]}')
    
# print("By name length: ")
# res3 = sorted(players, key = lambda item: len(item["name"]))
# print(', '.join(players["name"] for players in res3))

# ------------------------------------------------------- 7.5 ----------------------------------------------------------
# def clean(text):
#     return text.strip()

# def to_lower(text):
#     return text.lower()

# def remove_spaces(text):
#     return text.replace(" ", "_")

# def add_prefix(text):
#     return "user_" + text

# def pipeline(text, *operations):
#     print(f"Starting with: '{text}'")
#     for operation in operations:
#         text = operation(text)
#         print(f"after {operation.__name__ : <14}: '{text}'")
#     print("Final:", text)
# text = "   Ravi Kumar Sharma   "
# pipeline(text, clean, to_lower, remove_spaces, add_prefix)

# -------------------------------------------------------- SET 08 ------------------------------------------------------------------------------
# ---------------------------------------------- 8.1 -------------------------------------------------------------------
# is_even = lambda n: n % 2 == 0
# print(f"is_even(10)    -> {is_even(10)}")

# is_leap = lambda year: (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
# print(f"is_leap(2024)    -> {is_leap(2024)}") 
# print(f"is_leap(1900)    -> {is_leap(1900)}")

# reverse = lambda s: s[::-1]
# print(f'reverse("python")    -> {reverse('python')}')

# bigger = lambda a, b: a if a > b else b
# print(f"bigger(10, 20)    -> {bigger(10, 20)}")

# area_circle = lambda r: math.pi * r * r 
# print(f'area_circle(7)     -> {area_circle(7)}')

# --------------------------------------------- 8.2 --------------------------------------------------------------------
# grade = lambda marks: "A" if marks >= 90 else "B" if marks >= 75 else "C" if marks >= 60 else "D" if marks >= 40 else "F"

# print(f"grade(95) -> {grade(95)}")
# print(f"grade(82) -> {grade(82)}")
# print(f"grade(65) -> {grade(65)}")
# print(f"grade(45) -> {grade(45)}")
# print(f"grade(20) -> {grade(20)}")

# -------------------------------------------- 8.3 ---------------------------------------------------------------------
# fruits = ["banana", "Apple", "cherry", "Date"]

# result = sorted(fruits, key = lambda x: x.lower())
# print(result)

# ------------------------------------------- 8.4 ----------------------------------------------------------------------
# Given snippet
# funcs = []
# for i in range(3):     # all lambda values refer to same i
#     funcs.append(lambda: i * 10)   # after the loop ends at 2, i = 2 then 2 * 10 = 20

# print([f() for f in funcs])  # to rectify this make argument i = i to hold current value of i
# # correct version
# funcs = []
# for i in range(3):
#     funcs.append(lambda i=i: i * 10)

# print([f() for f in funcs])

# -------------------------------------------- 8.5 ---------------------------------------------------------------------
# Given Snippet
# process = lambda d: {k: (v * 2 if isinstance(v, int) else v.upper() if isinstance(v, str) else v) for k, v in d.items()}
# print(process({"a": 5, "b": "hi", "c": 3.5}))


# def process(data):
#     result = {}
    
#     for k, v in data.items():
#         if isinstance(v, int):
#             result[k] = v * 2
#         elif isinstance(v, str):
#             result[k] = v.upper()
#         else:
#             result[k] = v

#     return result

# print(process({"a": 5, "b": "hi", "c": 3.5}))

# ----------------------------------------------------- SET 09 -------------------------------------------------------------------------------------
# ---------------------------------------------- 9.1 -------------------------------------------------------------------
# numbers = []
# for i in range(1, 51):
#     if i % 7 == 0:
#         numbers.append(i)
# print("Numbers divisible by 7 from 1 to 50")
# print("->", numbers)

# words = ["hi", "python", "is", "great", "ok"]
# result = []
# for word in words:
#     if len(word) > 4:
#         result.append(word)
# print("Words longer than 4 letters from", words)
# print("->", result)

# words = ["madam", "python", "level", "code", "radar"]
# result = []
# for word in words:
#     if word == word[::-1]:
#         result.append(word)
# print("Palindromes from", words)
# print("->", result)

# --------------------------------------------- 9.2 --------------------------------------------------------------------
# Input =  [0, 1, "", "hello", None, [], [1,2], False, True, 0.0, "0"]
# output = list(filter(None, Input))
# print(output)
# # why did "0" survive but 0 did not?
# """ In python, None is used to remove the junk(false) values, it checks every element 
#     for example consider 0 it is false so python throws away 0
#     but when coming to "0" it is consider as a string(non-empty) which it is true so it remains in the list
#     even both "" and [] are thrown as they are false
# """
# # Output: [1, 'hello', [1, 2], True, '0'] 
    
# -------------------------------------------- 9.3 ---------------------------------------------------------------------
# students = [
#     {"name": "Ravi",   "marks": 78},
#     {"name": "Priya",  "marks": 92},
#     {"name": "Kiran",  "marks": 45},
#     {"name": "Divya",  "marks": 88},
#     {"name": "Suresh", "marks": 61},
# ]
# sum = 0
# for student in students:
#     sum += student["marks"]
# avg = sum / len(students)
# print(f'Class Average: {avg}')

# print("Above Average: ")
# for student in students:
#     if student["marks"] > avg:
#         print(student["name"], student["marks"])

# --------------------------------------------- 9.4 --------------------------------------------------------------------
# def is_prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2, n):   # To check whether a number is given, it requires mutliple conditions and loop
#         if n % i == 0:      # and a lambda should contain only a simple expression
#             return False    # so using a def makes the code more easier to read and understanble
#     return True

# numbers = list(range(1, 51))
# result = list(filter(is_prime, numbers))
# print(result)

# ---------------------------------------------- 9.5 -------------------------------------------------------------------
# result = filter(lambda x: x > 3, [1, 2, 3, 4, 5])
# print(list(result))  # here it prints [4, 5]
# print(list(result))  # but here it prints an empty list []

# """ what actually happened here is, filter() doesn't create a list, it creates an object called iterator and it returns each element
#     4 and 5. Then it reaches end which is exhausted. when asked to print in list for the first time it actually prints in a list
#     but for the second time, the iterator is already exhausted, so it returns a empty list 
# """
# # rectified version
# result = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5]))
# print(list(result))
# print(list(result))

# ------------------------------------------------------------- SET 10 --------------------------------------------------------------------------
# ---------------------------------------------- 10.1 ------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5]
# res1 = list(map(lambda x: x ** 2, numbers))
# print(f'Square of {numbers}            -> {res1}')

# s = ["1", "2", "3", "42"]
# res2 = list(map(int, s))
# print(f'{s} to integers    -> {res2}')

# s = ["ravi", "priya"]
# res3 = list(map(str.upper, s))
# print(f'{s} to upperacase      -> {res3}')

# s = ["hi", "python", "is"]
# res4 = list(map(len, s))
# print(f'Lengths of {s}    -> {res4}')

# ---------------------------------------------- 10.2 ------------------------------------------------------------------
# celsius = [0, 25, 37, 100, -40]
    
# fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
# print(fahrenheit)

# ---------------------------------------------- 10.3 ------------------------------------------------------------------
# names = ["Ravi", "Priya", "Kiran"]
# marks = [78, 92, 45]

# result = list(map(lambda name, mark: f"{name}: {mark}", names, marks)) 
# print(result)    # ['Ravi: 78', 'Priya: 92', 'Kiran: 45']

# # for different lengths
# names = ["Ravi", "Priya", "Kiran", "Siddhi"]
# marks = [78, 92, 45]

# result = list(map(lambda name, mark: f"{name}: {mark}", names, marks))
# print(result)   # ['Ravi: 78', 'Priya: 92', 'Kiran: 45']
# # Here Siddhi is ignored, because map() only iterates the minimum length of two lists and the remaining are ignored

# ---------------------------------------------- 10.4 ------------------------------------------------------------------
# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)
# print(f"Sum of [1,2,3,4,5] -> {total}")

# product = reduce(lambda x, y: x * y, numbers)
# print(f"Product of [1,2,3,4,5] -> {product}")

# numbers = [3, 7, 2, 9, 4]
# maximum = reduce(lambda x, y: x if x > y else y, numbers)
# print(f"Maximum of [3,7,2,9,4] -> {maximum}")

# words = ["Python", "is", "powerful"]
# sentence = reduce(lambda x, y: x + " " + y, words)
# print(f'Join ["Python","is","powerful"] -> {sentence}')

# words = ["hi", "python", "is"]
# longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
# print(f'Longest word in ["hi","python","is"] -> {longest}')

# ------------------------------------------------ 10.5 ----------------------------------------------------------------
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# result = reduce(
#     lambda d, word: {**d, word: d.get(word, 0) + 1},
#     words,
#     {}
# )
# print(result)

# ------------------------------------------------ 10.6 ----------------------------------------------------------------
# sales = [
#     {"product": "Laptop",   "price": 55000, "qty": 3,  "region": "South"},
#     {"product": "Mouse",    "price": 500,   "qty": 20, "region": "North"},
#     {"product": "Monitor",  "price": 12000, "qty": 5,  "region": "South"},
#     {"product": "Keyboard", "price": 1500,  "qty": 12, "region": "South"},
#     {"product": "Printer",  "price": 8000,  "qty": 2,  "region": "North"},
# ]

# south = filter(lambda item: item["region"] == "South", sales)
# south_revenue = map(lambda item: item["price"] * item["qty"], south)
# total_south = reduce(lambda x, y: x + y, south_revenue)
# print("Total South revenue: Rs", total_south)

# north = filter(lambda item: item["region"] == "North", sales)
# north_revenue = map(lambda item: item["price"] * item["qty"], north)
# total_north = reduce(lambda x, y: x + y, north_revenue)
# print("Total North revenue: Rs", total_north)

# south_total = sum(item["price"] * item["qty"] for item in sales if item["region"] == "South")
# north_total = sum(item["price"] * item["qty"] for item in sales if item["region"] == "North")

# ------------------------------------------------ 10.7 ----------------------------------------------------------------
# def sum_of_squares(numbers):
#     return reduce(
#         lambda x, y: x + y,
#         map(lambda x: x * x,
#             filter(lambda x: x % 2 == 0, numbers))
#     )

# print(sum_of_squares(range(1, 11)))
# print(sum_of_squares(range(1, 101)))

# -------------------------------------------------------------- SET 11 --------------------------------------------------------------------------
# ------------------------------------------------ 11.1 ----------------------------------------------------------------
# def make_power(n):
#     def power(x):
#         return x ** n
#     return power

# square = make_power(2)
# cube = make_power(3)

# print(square(5))
# print(cube(3))
# print(make_power(4)(2))

# ------------------------------------------------- 11.2 ---------------------------------------------------------------
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# c1 = make_counter()
# c2 = make_counter()

# print(c1(), c1(), c1())   
# print(c2(), c2())         
# print(c1())            

# --------------------------------------------------- 11.3 -------------------------------------------------------------
# def make_averager():
#     total = 0
#     count = 0
#     def average(num):
#         nonlocal total, count
#         total += num
#         count += 1
#         return total / count
#     return average

# avg = make_averager()

# print(avg(10))    
# print(avg(20))    
# print(avg(30))    
# print(avg(40))     

# ----------------------------------------------------- 11.4 -----------------------------------------------------------
# def make_stack():
#     stack = []

#     def push(item):
#         stack.append(item)
#         return f"Pushed {item}. Size: {len(stack)}"

#     def pop():
#         if len(stack) == 0:
#             return "Stack is empty"
#         item = stack.pop()
#         return f"Popped {item}. Size: {len(stack)}"

#     def size():
#         return len(stack)

#     return push, pop, size

# push, pop, size = make_stack()

# print(push(10))
# print(push(20))
# print(push(30))
# print(pop())
# print(pop())
# print(size())
# print(pop())
# print(pop())

# --------------------------------------------------------- 11.5 -------------------------------------------------------
# def once(func):
#     result = None
#     called = False

#     def wrapper():
#         nonlocal result, called
#         if not called:
#             result = func()
#             called = True
#         return result
#     return wrapper
# def expensive_setup():
#     print("Running setup...")
#     return "DONE"

# setup = once(expensive_setup)
# print(setup())
# print(setup())
# print(setup())

# ---------------------------------------------------------- 11.6 ------------------------------------------------------
# def create_wallet(name, balance):

#     def deposit(amount):
#         nonlocal balance
#         if amount > 0:
#             balance += amount
#             return f"Deposited {amount}. Balance: {balance}"
#         return "Deposit must be positive"
#     def withdraw(amount):
#         nonlocal balance
#         if amount > balance:
#             return f"Insufficient funds. Balance: {balance}"
#         balance -= amount
#         return f"Withdrew {amount}. Balance: {balance}"
#     def statement():
#         return f"{name}'s balance: {balance}"
#     return deposit, withdraw, statement

# deposit, withdraw, statement = create_wallet("Ravi", 1000)
# print(statement())  
# print(deposit(500))
# print(withdraw(2000))
# print(withdraw(300))
# print(deposit(-100))                          
# print(statement())                           # balance = 5000    # Cannot change the balance directly.

# The balance variable is hidden inside the closure and
# is accessible only through deposit(), withdraw(), and statement()

# ------------------------------------------------------------ SET 12 -------------------------------------------------------------------------------
# -------------------------------------------------- 12.1 --------------------------------------------------------------
# def uppercase(func):
#     def wrapper(name):
#         return func(name).upper()
#     return wrapper

# @uppercase
# def greet(name):
#     return f"hello, {name}"

# print(greet("ravi"))

# --------------------------------------------------- 12.2 -------------------------------------------------------------
# def count_calls(func):
#     def wrapper():
#         wrapper.count += 1
#         print(f"Call #{wrapper.count}")
#         func()

#     wrapper.count = 0
#     return wrapper

# @count_calls
# def say_hi():
#     print("Hi!")

# say_hi()
# say_hi()
# say_hi()
# print(say_hi.count)

# ---------------------------------------------------- 12.3 ------------------------------------------------------------




