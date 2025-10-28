class Employee:
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

