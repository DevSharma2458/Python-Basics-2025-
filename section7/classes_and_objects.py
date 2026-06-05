'''Class ia a blueprint or a template'''
'''Objects is specific instance created from the template (class)'''

# class Employee:
#     company = "HP"

#     def get_salary(self): #self is important here becuase self is a way to reference the object of the class which is being created
#         print(self)
#         return 34000

# e1 = Employee() # An object of class Employee is created here
# print(e1.get_salary()) #Employee e's get salary method is called

# e2 = Employee()
# print(e2.get_salary())
# print(e2.company)


class Dog:
    species = "Canine" # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Bunty",2)

print(dog1.name)
        
print(dog1.__dict__)




