import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices = ["add", "sub", "div", "mul"], help = "Operation  to perform")

args = parser.parse_args()

# print(args)

if(args.operation == "add"):
    print(f"The Addition of these two numbers are: {args.num1 + args.num2}")
elif(args.operation == "sub"):
    print(f"The Substracion of these two numbers are: {args.num1 - args.num2}")
elif(args.operation == "mul"):
    print(f"The Multiplication of these two numbers are: {args.num1 * args.num2}")    
elif(args.operation == "div"):
    print(f"The Division of these two numbers are: {args.num1 / args.num2}")

else:
    print("Some Error Occured")

''' 
In Terminal Write this 

python section9\command_line.py 4 9 add
'''

