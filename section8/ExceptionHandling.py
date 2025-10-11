# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a + b}")

#     except ValueError:
#         print("Please dont perform bad typecasts")

#     except ZeroDivisionError:
#         print("Hey dont divide by 0")

#     except Exception as e: #Carries error info 
#         print("Enter valid value", e)

#After running the above code use ctrl + C to end the terminal from infinite while loop

##------------------------------------------------------------------
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# if b == 0:
#     raise ValueError("Please dont divide by 0")
# else:
#     print(f"The diversion is {a / b}")

##------------------------------------------------------------------
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# try:
#     c = a/b
#     print(c)

# except Exception as e:
#     print(e)

# finally:
#     print("This will always be printed")

##------------------------------------------------------------------

# def divide(a, b):
#     try:
#         c = a/b
#         print(c)

#     except Exception as e:
#         print(e)

#     finally: # we used finally because normal print wont run in this function so finally is being used to make it run no matter if the condition is being satisfied or not.
#         print("This will always be printed")

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# divide(a, b)