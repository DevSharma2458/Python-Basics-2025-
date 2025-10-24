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
class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

a = MathUtils
print(a.add(3, 54))
a.description()
        
#-----------------------------------------------------------