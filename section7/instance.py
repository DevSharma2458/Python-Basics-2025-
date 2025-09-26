class Employee:

    company = "HP"

    def __init__(self, salary, name, bond, company): # this calls constructor
        self.salary = salary #Create an instace attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")


e1 = Employee(3400, "john", 3, "Tesla")
print(e1.company) # will print instace attribute whenever present
print(Employee.company) # This will alwasy print the class attribute


'''Object Introspection'''
print(dir(e1))








