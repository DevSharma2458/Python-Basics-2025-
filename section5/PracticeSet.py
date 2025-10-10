# def greet():
#     print("Hello, Python Learning!")

# greet()
# #-------------------------------------------
# def square(num):
#     print (num * num)

# square(5)

# #-------------------------------------------
# def full_name(first, last):
#     print(first,last)

# full_name("Dev", "Sharma")
# #-------------------------------------------
# def calculate_area(length, width = 10):
#     return length * width

# print(f"The area of this rectangle is {calculate_area(13, 20)}")
# print(calculate_area(13))
# #-------------------------------------------
# add = lambda a, b: a + b
# print(add(3, 5))
# #-------------------------------------------
# #Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares
# square = lambda x: x*x
# list1 = [1, 2, 3, 4, 5]
# print(list(map(square, list1)))
# #------------------------------------------
# #Facotrial of a number 
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return factorial (n - 1) * n

# print(factorial(7))
# #------------------------------------------
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return n%10 + sum_of_digits(n//10)

# print(sum_of_digits(3437))
# #------------------------------------------
# import math
# print(math.sqrt(144))
# radian_value = math.radians(90)
# result = math.sin(radian_value)
# print(result)
# #------------------------------------------
# import requests
# a = requests.get("https://api.github.com/")
# print(a.json())
# #------------------------------------------
# def increment():
#     counter = 0
#     counter += 1
#     print(counter)

# increment()
# increment()
# increment()
# # Alternatively if to increment when ever it is being called 
# counter = 0
# def increment():
#     global counter
#     counter += 1
#     print(counter)

# increment()
# increment()
# increment()
# #------------------------------------------
# def multiply(a, b):
#     '''This will multiply two numbers '''
#     c = a * b
#     return c
# print(multiply.__doc__)

# #------------------------------------------
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2) 


# def fibonacci(n):
#     print(f"First {n} Fibonnaci number are: ")
#     for i in range(n):
#         print(fib(i), end = " ")

# fibonacci(10)
# #------------------------------------------
# def safe_divide(a, b):
#     if b == 0:
#         print("Cannot divide by zero")
#     else:
#         c = a/b
#         print(c)
    
# safe_divide(2, 2)    
# #------------------------------------------
# from modules import mymodule
# mymodule.is_even(10)
# #------------------------------------------
