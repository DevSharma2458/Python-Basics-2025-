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

# # a = Animal("Dog")
# # a.speak()
# d = Dog("Bruno")
# d.speak
# print(d.location) 
#-------------------------------------------------------
class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now...")

class Dog(Animal): #Inheritance
    def speak(self):
        super().speak()
        print("Woof!")

class Cat(Animal):
    location = "France"
    def speak(self):
        super().speak()
        print("Meow!")  


d = Dog("Bruno")
d.speak()
print("The Dog is from",d.location) 
e = Cat("Isabelle" )
e.speak()
print("The Cat is from" , e.location)