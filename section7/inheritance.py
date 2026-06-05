# class Animal:
#     location = "Australia"
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Generic animal sound")


# class Dog(Animal): #Inheritance
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")        

# a = Animal("Dog")
# a.speak()
# d = Dog("Bruno")
# d.speak()
# print(d.location) 


#-------------------------------------------------------

# class Animal: # Parent class (superclass)
#     location = "Australia"
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Speaking now...")

# class Dog(Animal): #Inheritance
#     def speak(self):
#         super().speak()
#         print("Woof!")

# class Cat(Animal):
#     location = "France"
#     def speak(self):
#         super().speak()
#         print("Meow!")  


# d = Dog("Bruno")
# d.speak()
# print("The Dog is from",d.location) 
# e = Cat("Isabelle" )
# e.speak()
# print("The Cat is from" , e.location)

#------------------------------------------------
# class Animals:

#     location = "India"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print("Animal Name:",self.name ,",", "Animal Age:",self.age, "Location:", Animals.location)
    
#     def speak(self):
#         print("I gotta roar!")
# class Dog(Animals):

#     def speak(self):
#         super().info()
#         super().speak()
#         print(self.name,"Woof!")

# class Cat(Animals):
#     def speak(self):
#         super().info()
#         super().speak()
#         print(self.name,"Meow!")

# Dog1 = Dog("Bruno",2)

# # print(Dog1.__dict__)
# Dog1.speak()

# # Cat1 = Cat("Isabel",1)
# # print(Cat1.name, end=" ")
# # print(Cat1.age)
# # print(Cat1.__dict__)

'''Types of inheritance'''

'''Single Inheritance'''
# class Person:
#     def __init__(self,name):
#         self.name = name
# class Employee(Person):
#     def show_role(self):
#         print(self.name,"is an employee")
        
# emp = Employee("Sarah")
# print("Name:", emp.name)
# emp.show_role()
'''Multiple Inheritance'''
# class Person:
#     def __init__(self,name):
#         self.name = name

# class Job:
#     def __init__(self, salary):
#         self.salary = salary

# class Employee:
#     def __init__(self,name,salary):
#         Person.__init__(self, name)
#         Job.__init__(self,salary)

#     def details(self):
#         print(self.name,"earns",self.salary)
        

# emp = Employee("Subhash",900000)
# emp.details()
'''Multi Level Inheritance'''
# class Person:
#     def __init__(self,name):
#         self.name = name
        
# class Employee(Person):
#     def show_role(self):
#         print(self.name ,"is an employee")

# class Manager(Employee):
#     def department(self, dept):
#         print(self.name, "manages", dept,"department")

# mgr = Manager("Joy")
# mgr.department("HR")
# mgr.show_role()

'''Hierarchial Inheritance'''
# class Person:
#     def __init__(self,name):
#         self.name = name
# class Employee(Person):
#     def role(self):
#         print(self.name,"is an Employee")

# class Intern(Person):
#     def role(self):
#         print(self.name,"is an intern")

# emp = Employee("Joy")
# emp.role()

# intern = Intern("Jeremy")
# intern.role()
    
'''Hybrid Inheritance'''

# class Person:
#     def __init__(self, name):
#         self.name = name
# class Employee(Person):
#     def role(self):
#         print(self.name,"is an Employee")
# class Project:
#     def __init__(self, project_name):
#         self.project_name = project_name
        
# class TeamLead(Employee,Project):
#     def __init__(self, name, project_name):
#         Employee.__init__(self, name)
#         Project.__init__(self, project_name)

#     def detials(self):
#         print(self.name,"leads project:",self.project_name)

# lead = TeamLead("Sophia","Ai Development")
# lead.role()
# lead.detials()