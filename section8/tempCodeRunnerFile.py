class Employee:
#     company = "HP"
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     # Instance Method (default)
#     def print_info(self):
#         info = f"The name is {self.name} and the salary is {self.salary}"
#         print(info)

#     def sum(self,a, b): # here self is being passed because e2 is calling it so there will be three arguments and if you dont pass self it will give error that two arguments are being passed and three were given in e2.sum(5,23) 
#         # for an instance if suppose e2 is an heavy object and you want to pass e2 as an arguement then see the next method
#         return a+b
    
# e1 = Employee("Jack", 34555)
# e2 = Employee("Jill", 34555)
# # print(Employee.company)
# e1.print_info()
# e2.print_info()
# print(e2.sum(5,23))