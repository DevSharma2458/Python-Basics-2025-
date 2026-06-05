'''A decorator is a function that adds extra functionality to another function without changing its code.

Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Then it returns that new function.
'''



# def decorator(func):
#     def wrapper():
#         print("I am about to execute a function...")
#         func()
#         print("I have executed the function...")
#     return wrapper

# @decorator # by including @decorator we can print the wrapper statements by using say_hello()
# def say_hello():
#     print("Hello!")
# say_hello()

# # say_hello()    #normal printing say_hello without including @decorator
# Method of Printing the f() function which contains wrapper 
# f = decorator (say_hello) 
# f()

''' 
# Explaination
first see f = decorator (say_hello)
which passes the say_hello to the def decoration's "func"

now the func = say_hello

then it see the def wrapper and according to it prints the whole body and in between when you saw func() in the wrapper that is the say_hello being called over there

'''


#----------------------------------------------------
'''Decorators with Aguements'''

# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator

# @repeat(7)
# def say_hello(a):
#     print(f"Hello! {a}" )

# say_hello("Dev")    


'''
Explaination

1- Python sees @repeat(7) → calls repeat(7) first.

2- Inside repeat(7) → returns the decorator function (with n = 7).

3- decorator(say_hello) is called → func = say_hello.

4- Inside decorator → defines wrapper(a) and returns it.

5- Now say_hello = wrapper → the original function is wrapped.

6- Calling say_hello("Dev") → actually calls wrapper("Dev").

7- Inside wrapper(a) → Python binds a = "Dev".

8- For loop runs 7 times (n=7) → each time it calls func(a) → original say_hello(a) runs.

9- Inside original say_hello → a = "Dev", so it prints Hello! Dev.
'''

# def decorator(func):
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#     return wrapper

# @decorator
# def greet():
#     print("Hello, World!")
# greet()

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper

# @decorator
# def greet(name, age):
#     return f"{name} is {age}"


# print(greet(name="Bunty",age=5))

'''Types Of Decorators'''
'1- Function Decorators'

# def simple_decorator(x):
#     def wrapper():
#         print("Before Execution")
#         x()
#         print("After Execution")

#     return wrapper

# @simple_decorator
# def greet():
#     print("Hello World")
# greet()

'2- Method   Decorators'
# def method_decorator(func):
#     def wrapper(self):
#         print("Before execution")
#         func(self)
#         print("After execution")
#         return func
#     return wrapper

# class MyClass:
#     @method_decorator
#     def say_hello(self):
#         print("hello!")

# obj = MyClass()
# obj.say_hello()

'3- Class    Decorators'
# def fun(cls):
#     cls.class_name = cls.__name__
#     return cls

# @fun
# class Person:
#     pass
# print(Person.class_name)

'''Built-in Decorators'''
'''@Staticmethod- It is used to define a method that doesn't operate on an instance of class (i.e., it doesn't use self). Static methods are called on class itself, not on an instance of class.'''
# class MathOperations:
#     @staticmethod
#     def add(x, y):
#         return x + y

# # Using the static method
# res = MathOperations.add(5, 3)
# print(res)

'''@classmethod-It is used to define a method that operates on class itself (i.e., it uses cls). Class methods can access and modify class state that applies across all instances of class.

Example: This code defines a class Employee with a class variable raise_amount and a class method set_raise_amount that updates this variable for entire class.'''
# class Employee:
#     raise_amount = 1.05
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

# # Using the class method
# Employee.set_raise_amount(1.11)
# print(Employee.raise_amount)
'''Explanation:

1-set_raise_amount is a class method defined with @classmethod decorator.
2-It can modify class variable raise_amount for class Employee and all its instances.'''

'''@property- It is used to define a method as a property, which allows you to access it like an attribute. This is useful for encapsulating implementation of a method while still providing a simple interface.

Example: This code defines a circle class demonstrating @property for controlled attribute access, allowing safe updates to radius.'''
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError("Radius cannot be negative")

#     @property
#     def area(self):
#         return 3.14159 * (self._radius ** 2)

# # Using the property
# c = Circle(5)
# print(c.radius) 
# print(c.area)    
# c.radius = 10
# print(c.area)

'''Chaining Multiple Decorators'''
'''Chaining decorators means applying multiple decorators to same function. Each decorator wraps function in sequence, adding layered behavior.

Example: This example shows how chaining decorators works by applying two decorators in different orders to see how output changes.'''

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner

# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner

# @decor
# @decor1
# def num1():
#     return 10

# @decor1
# @decor
# def num2():
#     return 10

# print(num1())
# print(num2())













