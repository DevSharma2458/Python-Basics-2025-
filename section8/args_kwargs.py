## Args basically collect all the arguements and creates tuple 

# def sum(*args):
#     print(args)
#     total = 0
#     for item in args:
#         total += item
#     return total

# print(sum(342, 2, 7))

##----------------------------------------
## Kwargs is a dictionary with all the key value pairs which were passed to marks

# def marks(**kwargs):
#     for item in kwargs.keys():
#         print(f" The marks of {item} is {kwargs[item]}")

# marks(shubham = 34, viram = 54, jack = 34, Marie = 90, Priya = 45)

## ----------------------------------------

## Using both in one code 
## Condition is that use args first then kwargs

def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill = 32, marie = 31)