'''A getter is just a method we write to safely read a private variable instead of accessing it directly.'''

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# e = Employee("Jack Doe", 34555)
# e.projects = 6
# print(e.projects)
#---------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    def set_first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    
e = Employee("Jack Doe", 34555)
print(e.first_name())
e.set_first_name("John")
print(e.name)
#----------------------------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property    
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    
e = Employee("Jack Doe", 34555)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "John"
print(e.name)

'''
# Code Flow / Execution Steps:
# 1. Python reads the Employee class and stores it in memory.
# 2. Decorators are applied:
#    - @property: makes first_name() behave like a readable attribute.
#    - @first_name.setter: links the setter method to first_name.
# 3. Object creation: e = Employee("Jack Doe", 34555)
#    - __init__() is called
#    - e.name = "Jack Doe", e.salary = 34555
# 4. Accessing first_name: print(e.first_name)
#    - Python sees first_name is a property → calls getter method
#    - self.name.split(" ") → ["Jack", "Doe"]
#    - Returns l[0] → "Jack"
#    - print() outputs "Jack"
# 5. Updating first_name: e.first_name = "John"
#    - Python sees first_name has a setter → calls setter method
#    - self.name.split(" ") → ["Jack", "Doe"]
#    - new_name = f"{first} {l[1]}" → "John Doe"
#    - Updates self.name = "John Doe"
# 6. Printing updated name: print(e.name)
#    - Outputs "John Doe"
# 7. Key points:
#    - @property allows reading without parentheses.
#    - @first_name.setter allows writing using assignment syntax.
#    - new_name is a local variable used to build the updated name.
'''
