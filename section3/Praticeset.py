# n = int(input("Enter a number: "))
# if n > 0:
#     print("Positive number")
# elif n < 0:
#     print("Negative number")
# else:
#     print("Zero")
#-------------------------------------------
# age = int(input("Enter your age: "))
# if age > 18:
#     print("You can Vote")
# elif age < 0:
#     print("Invalid age")
# else:
#     print("You cannot Vote")
#-------------------------------------------
# n = int(input("Enter a number: "))
# if n % 2 ==0:
#     print("Even number")
# elif n == 0:
#     print("Zero")
# elif n % 2 != 0:
#     print("Odd number")        
# else:
#     print("Invalid input")

# # another approach    
# # Ask user for input
# try:
#     # Try converting input to integer
#     n = int(input("Enter a number: "))

#     # Check number type
#     if n == 0:
#         print("Zero")
#     elif n % 2 == 0:
#         print("Even number")
#     elif n % 2 != 0:
#         print("Odd number")
#     else:
#         print("Invalid input")  # (This else might never trigger, but good for structure)

# # If conversion fails (e.g., user entered a string like "hello")
# except ValueError:
#     print("Invalid input! Please enter a numeric value.")
#-------------------------------------------    
# Match Case
#Ask the user to enter a day number 1 - 7 and print the corresponding day name.
# day = int(input("Enter a day number (1-7): "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number! Please enter a number between 1 and 7.")
# print("Thank you for using the day finder!")
#-------------------------------------------
# Value1 = int(input("Enter first value: "))
# Value2 = int(input("Enter second value: "))

# operation = input("Enter operation (+, -, *, /): ")

# match operation:
#     case "+":
#         result = Value1 + Value2
#         print(f"The sum of {Value1} and {Value2} is {result}")
#     case "-":
#         result = Value1 - Value2
#         print(f"The difference between {Value1} and {Value2} is {result}")
#     case "*":
#         result = Value1 * Value2
#         print(f"The product of {Value1} and {Value2} is {result}")
#     case "/":
#         if Value2 != 0:
#             result = Value1 / Value2
#             print(f"The division of {Value1} by {Value2} gives {result}")
#         else:
#             print("Error: Division by zero is not allowed.")
#     case _:
#         print("Invalid operation! Please enter one of +, -, *, /.")
#------------------------------------------
# for i in range ( 1 , 11):
#     print(i)
#-------------------------------------------
# n = int(input("Enter a number: "))    
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
#-------------------------------------------
#Calculate the sum of  1 to 100 using a for loop.
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(f"The sum of 1 to 100 is {sum}")
#----------------------------------------------
#print the following pattern using a for loop
# '''
# *
# * *
# * * *
# * * * *
# '''
# for i in range(1,5):
#     print("* " * i)
#-------------------------------------------
# n = 1
# while n <= 10:
#     print(n)
#     n += 1
#-------------------------------------------
# password = 1234
# user_input = int(input("Enter the passowrd:  "))
# while user_input != password:
#     print("Wrong Password! Try Again.")
#     user_input = int(input("Enter the password:  "))
# print("Correct Password! You are logged in.")
#-------------------------------------------
#Use a while lopp to reverse a given number 
# num = 45522
# print(int(str(num)[::-1]))
#-------------------------------------------
# for i in range(1,11):
#     print(i)
#     if i == 7:
#         break
#-------------------------------------------
# Use a for loop to print numbers from 1 to 10, but skip the number 5 using the continue statement.
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
#-------------------------------------------
# for i in range(1,11):
#     if i == 3:
#         pass
#     print(i)
# #Alternative

# for i in range(1, 6):
#     match i:
#         case 1:
#             print(1)
#         case 2:
#             print(2)
#         case 3:
#             pass
#         case 4:
#             print(4)
#         case 5:
#             print(5)