'''Encapsulation means hiding internal details of a class and only exposing what’s necessary. It helps to protect important data from being changed directly and keeps the code secure and organized.'''

# class Employee:
#     def __init__(self,name,salary,bonus):
#         self.name = name # public
#         self.__salary = salary # private
#         self._bonus = bonus # protected

# emp = Employee("Fedrick",50000,5000)
# print(emp.name)
# print(emp._bonus) 
# print(emp.salary) # will give error cause it is not usable
#print(emp.__salary) # will give you error cause it is private attribute cant be accessed

''' Types of Access Modifiers '''
#1- Public
# class Employee:
#     def __init__(self,name):
#         self.name = name

#     def display_name(self):
#         print(self.name)

# emp = Employee("John")
# emp.display_name()

        
#2- Protected
# class Employee:
#     def __init__(self,name,age):
#         self.name = name # public
#         self._age = age # protected

# class SubEmployee(Employee):
#     def show_age(self):
#         print("Age:",self._age)

# emp = SubEmployee("Ross",30)
# print(emp.name)
# emp.show_age() # But python is not so strict with protected attribute

#3- Private

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary

#     def show_salary(self):
#         print("Salary:",self.__salary)

# emp = Employee("Robert",60000)
# print(emp.name)
# emp.show_salary()
# print(emp.__salary) # Error no attribte (cause you cant access it directly)
# print(emp.salary) # Error no attribute

# Combination Example
# class BankAccount:
#     def __init__(self):
#         self.balance = 1000

#     def _show_balance(self):
#         print(f"Balance: ₹{self.balance}")  # Protected method

#     def __update_balance(self, amount):
#         self.balance += amount             # Private method

#     def deposit(self, amount):
#         if amount > 0:
#             self.__update_balance(amount)  # Accessing private method internally
#             self._show_balance()           # Accessing protected method
#         else:
#             print("Invalid deposit amount!")
            
# account = BankAccount()
# account._show_balance()      # Works, but should be treated as internal
# #print account.__update_balance(500)  # Error: private method
# account.deposit(500)         # Uses both methods internally


'''Getters and Setters used to access and modify private variables'''
# class Employee:
#     def __init__(self):
#         self.__salary = 50000  # Private attribute

#     def get_salary(self):    # Getter method
#         return self.__salary

#     def set_salary(self, amount):   # Setter method
#         if amount > 0:
#             self.__salary = amount
#         else:
#             print("Invalid salary amount!")

# emp = Employee()
# print(emp.get_salary())  # Access salary using getter

# emp.set_salary(60000)   # Update salary using setter
# print(emp.get_salary())