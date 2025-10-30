# def logger(func):
#     def wrapper():
#         print("The function is called")
#         return func
#     return wrapper

# @logger
# def say_hello():
#     print("Hello")

# say_hello()
## -----------------------------------------
# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         end = time.time()
#         print(f"Function took {end - start:.4f} seconds to execute")
#         return result
#     return wrapper

# @timer
# def sum_numbers():
#     total = sum(range(1, 1_000_001))
#     print("Sum: ", total)

# sum_numbers()
# # Alternative
# from time import time
# def timer(func):
#     def wrapper(n):
#         t1 = time()
#         result = func(n)
#         t2 = time()
#         print( t2- t1)
#         return result
#     return wrapper

# @timer
# def sum_1m(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# a = sum_1m(1000000)
# print(a)
#-----------------------------------------------------------
# class Employee:
#     def __init__(self, salary):
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary
    
#     @salary.setter
#     def salary(self, value):
#         if(value<0):
#             print("Dont set salary negative value")
#         else:
#             self._salary = value
# e = Employee(3)
# e.salary = -67
# print(e.salary)
# e.salary = 67
# print(e.salary)
#-----------------------------------------------------------
# class MathUtils:
#     def __init__(self):
#         pass

#     @staticmethod
#     def add(a, b):
#         return a + b
#     @classmethod
#     def description(cls):
#         print("This is a utility class for math operations.")

# a = MathUtils
# print(a.add(3, 54))
# a.description()
        
#-----------------------------------------------------------

# #here we didnt use __len__ because it only returns 1 integer and not more than one so for getting multiple lengths we made a custom function and used loop to access the data 
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"{self.title} by {self.author}"

#     def get_len_details(self):
#         title_length = f"The length of Title is {len(self.title)}"
#         author_length =  f"The length of Author is {len(self.author)}"
#         total_length = f"The Total length is {len(self.title) + len(self.author)}"
#         return title_length, author_length, total_length


# b1 = Book("Chandni Raat","Piyush Mishra")
# b2 = Book("Two Souls", "Arvind Tiwari" )


# # You can do this same for book 2
# print(b1)
# details = b1.get_len_details()
# for info in details:
#     print(info)

#---------------------------------------------------------------------

# try:
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))

#     if number1 < 0 or number2 < 0:
#         raise ValueError("No Negative numbers allowed")  # manually raise an error

#     print(number1 / number2)

# except ValueError as e:
#     print(e)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

#-----------------------------------------------------------------------
# # map ---------------------
# numbers = [1, 2, 3, 4, 5] 

# def cube(x):
#     return x ** 3

# cubes = list(map(cube, numbers))
# print(cubes)

# # filter ---------------------
# numbers = [10, 11, 12, 13, 14]

# def even(x):
#     while True:
#        return x % 2 == 0

# even_number = list(filter(even, numbers))
# print(even_number)

# # reduce ---------------------
# from functools import reduce

# numbers = [1, 2, 3, 4] 
 
# def product(x, y):
#     return x + y

# sum = (reduce(product, numbers))
# print(sum)

#-----------------------------------------------------------------------
# while (data := input("Enter any number")):
#     print(data)
#     if data == "quit":
#         break

# # q2 ------------
# words = ["python", "rocks", "ai"]

# lengths = [length for word in words if (length := len(word)) >= 4]

# print(lengths)


#-----------------------------------------------------------------------

# def sum_all(*args):
#     print(args)
#     total = 0
#     for item in args:
#         total += item
#     return total

# print(sum_all(3,4,3,4,1))

## Alternative 

# def sum_all(*args):
#     total = sum(args)
#     return total
# print(sum_all(1, 2, 3))   

## Alternative

# def sum_all(*args):
#     return sum(args)

# print(sum_all(3, 4, 3, 4, 1))  # → 15

'''
So why use the loop version?

Use the loop version when:

You’re learning how iteration works.

You want to add extra logic, like ignoring negatives or printing intermediate steps:

def sum_all(*args):
    total = 0
    for item in args:
        if item > 0:  # skip negatives
            total += item
    return total

    
Use sum(args) when:
You just want the total quickly and simply.

'''

# def print_details(**kwargs):
#     print(kwargs)

# print_details(name = "Dev", age = 22, country = "India")
 ## Output 
 ## {'name': 'Dev', 'age': 22, 'country': 'India'}
 
# def print_details(**kwargs):
#     print(kwargs)
    
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# print_details(name = "Dev", age = 22, country = "India")

## Output
'''
{'name': 'Dev', 'age': 22, 'country': 'India'}
name = Dev
age = 22
country = India
'''

# # ARGS and KWARGS example 

# def cafe_order(*items, **customer):
#     print("Order summary:")
#     for item in items:
#         print(f"- {item}")

#     print("\nCustomer details:")
#     for key, value in customer.items():
#         print(f"{key} : {value}")

# cafe_order("Coffee", "Brownie", "Water", name="Arjun", table=5, payment="Card")

## More Optimised with user Input

def cafe_order(*items, **customer):
    print("\n🧾 Order summary:")
    for item in items:
        print(f"- {item}")

    print("\n👤 Customer details:")
    for key, value in customer.items():
        print(f"{key} : {value}")


# ----- Taking user input -----
# Taking menu items (split by comma)
menu_items = input("Enter the items you want to order (comma-separated): ")
items_list = [item.strip() for item in menu_items.split(",")]

# Taking customer details
name = input("Enter your name: ")
table = input("Enter your table number: ")
payment = input("Enter payment method (Cash/Card/UPI): ")

# Calling the function
cafe_order(*items_list, name=name, table=table, payment=payment)














