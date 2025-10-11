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
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")
else:
    print(f"The diversion is {a / b}")
