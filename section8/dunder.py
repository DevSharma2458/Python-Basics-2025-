'''Dunder means double under score'''
# class Employee:
#     company = "HP"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self): # str is dunder method
#         return f"The name is {self.name} and the salary is {self.salary}"

#     def __repr__(self): # also a dunder method like str but used most by developers mostly to debug 
#         return f"name: {self.name}\nsalary: {self.salary}"
    
#     def __len__(self): 
#         return len(self.name)

# e = Employee("Dev", 435666)
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))
# print(len(e))
##---------------------------------------------------------------------

'''
__str__ is called automatically when you print an object.
It lets you decide what message to show instead of the default memory address.

__len__ lets your object work with len() just like a list or string.

__add__ runs automatically when we use + between two objects.
        So here, it will add their salaries.

__eq__
Used when you compare two objects with ==
'''

# __add__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        
        n1 = self.name + other.name
        s1 = self.name + str(f"{self.salary}")
        return n1, s1
       

e1 = Employee("Jack", 5000)
e2 = Employee("Jill", 6000)

print(e1 + e2)   # same as e1.__add__(e2)

#__len__
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Jack", "Jill", "John"])
print(len(team))  # 👉 3

# __eq__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __eq__(self, other):
        return self.salary == other.salary

e1 = Employee("Jack", 5000)
e2 = Employee("Jill", 5000)
e3 = Employee("John", 6000)

print(e1 == e2)  # 👉 True
print(e1 == e3)  # 👉 False

# __repl__
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Employee(name='{self.name}', salary={self.salary})"

    def __str__(self):
        return f"{self.name} earns {self.salary} per month"

e = Employee("Jack", 5000)
print(e)       # calls __str__  👉 Jack earns 5000 per month
print(repr(e)) # calls __repr__ 👉 Employee(name='Jack', salary=5000)







