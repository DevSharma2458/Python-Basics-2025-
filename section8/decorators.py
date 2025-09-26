'''A decorator is a function that adds extra functionality to another function without changing its code.

Decorator is a function that takes a function, it creates a new function inside its body (wrapper). Them it returns that new function.
'''



def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed the function...")
    return wrapper

@decorator # by including @decorator we can print the wrapper statements by using say_hello()
def say_hello():
    print("Hello!")
say_hello()

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





