# class Employee:
#     company = "HP"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# e1 = Employee("Jack", 34555)
# e2 = Employee("Jill", 34555)
# print(e1.name)
# print(e2.company)
## -------------------------------------------
''' In an instance method whatever is calling self either e1 or e2 they will be stored or refered to self for an example if e1 is calling Employee then self = e1 in print_info(self)
Now copy of a Employee.print_info(self)'s self belongs to e1 
'''
# An instance simply means a copy of a class — a real object created from the class blueprint.
# An instance method is a function that belongs to the instance (object).

# It always has self as its first parameter.
# self automatically refers to the object that called the method.
# class Employee:
#     company = "HP"
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     # Instance Method (default)
#     def print_info(self): # Python would have no idea which object’s name you mean — e1’s or e2’s?
#     # So self acts as the identity card of the object calling the method.

#         info = f"The name is {self.name} and the salary is {self.salary}"
#         print(info)

#     def sum(self,a, b): 
#         ''' here self is being passed because e2 is calling it so there will be three arguments and if you dont pass self it will give error that two arguments are being passed and three were given in e2.sum(5,23) 

#      for an instance if suppose e2 is an heavy object and you want to pass e2 as an arguement then see the next method '''
#         return a + b
    
#     def mul(self, a, b):
       
#         return a * b
    
# e1 = Employee("Jack", 34555)
# e2 = Employee("Jill", 34555)
# # print(Employee.company)
# e1.print_info()
# e2.print_info()
# print(e2.sum(5,23))
# print(e1.mul(5, 5))
## -------------------------------------------
# class Employee:
#     company = "HP"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     # Instance Method (default)
#     def print_info(self):
#         info = f"The name is {self.name} and the salary is {self.salary}"
#         print(info)

#     #Static Method
#     @staticmethod # now we dont need to pass self here because static method is not related to any instance it is related to class
#     def sum(a, b): 
#         return a+b

#     # Class Method
#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company

#     def print_company(self):
#         print(f"The company name is {self.company}")

# e1 = Employee("Jack", 34555)
# e2 = Employee("Jill", 34555)
# # print(Employee.company)
# e1.print_info()
# e2.print_info()
# print(e2.sum(5,23))
# e1.print_company()
# e1.change_company("Delloite")
# e1.print_company()
# print(Employee.company)
# --------------------------------------------------------------------

class MathUtils:
    description = "This is a utility class for math operations."
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
  
    '''so basically if i dont put () in m = MathUtils then m == MathUtils which can directly affect the class (cause not m is just another name for MathUtils) but if i use () then the object will use the Blueprint of the class (This is what we call instance method) and if i am using () this then i need to put @staticmethod for the particular function that does not need any arguement or parameter(cause if i dont put @staticmethod then it will pass 'self' as first parameter then ask for name and salary, which i dont want to pass that is why i use @staticmethod)'''

    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod # If i remove this then the changes will be made only for that particular object and not the whole class (basically it uses self as cls and makes the blueprint and changes particularly for that object but if we use @classmethod then the changes in one object will definitly apply to all other objects)
    def change_description(cls, new_description):
        cls.description = new_description
        return new_description
    
    def show_detail(self):
        print(f"{self.description}")

m = MathUtils("jolly", 5000)    

m1 = MathUtils("jack", 5000) # Instance Method being used (storing MathUtils() in m where () with parameters is required...... basically what instance is that you are storing class while also giving paramaters and storing that in a new variable and from next time you use that particular variable to perform operations)

m2 = MathUtils("jill", 5000)


''' here i need to pass name and salary as parameters to store that in m which is compulsory step''' 
print(m.add(5,3))
m.show_detail()
m.change_description("We believe in smart work!")
m.show_detail()
m1.show_detail()

# No object being created and we are calling it directly from the class because we dont need any parameter or arguement in that particular condition 

# ✅ Call static method directly from class
print(MathUtils.add(5, 3))

# ✅ Call class method directly from class
MathUtils.show_detail()





