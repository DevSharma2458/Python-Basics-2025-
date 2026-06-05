'''Types of polymorphism

1- Method Overloading- Complile-time Polymorphism
2- Method Overriding-  Runtime Polymorphism
'''

# # Method Overloading - Compile-time polymorphism means deciding which method or operation to run during compilation, usually through method or operator overloading.
# Languages like Java or C++ support this. But Python doesn’t because it’s dynamically typed it resolves method calls at runtime, not during compilation. So, true method overloading isn’t supported in Python, though similar behavior can be achieved using default or variable arguments.

# Example: This code demonstrates method overloading in Python using default and variable-length arguments. The multiply() method works with different numbers of inputs, mimicking compile-time polymorphism.

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))


# # Method Overriding - Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.

# In Python, this happens through Method Overriding a child class provides its own version of a method already defined in the parent class. Since Python is dynamic, it supports this, allowing same method call to behave differently for different object types.

# Example: This code shows runtime polymorphism using method overriding. The sound() method is defined in base class Animal and overridden in Dog and Cat. At runtime, correct method is called based on object's class.

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())