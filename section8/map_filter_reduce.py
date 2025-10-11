# #-------------------------------------------------------------
# # Map
# numbers = [1, 2, 3, 4, 45, 21]

# def square(x):
#     return x * x

# new = list(map(square, numbers))
# print(new)

# # -------------------------------------------------------------
# # Filter

# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
# a = [1, 3, 5, 234, 34, 32, 6543, 23, 2, 5, 6, 7, 43]    
# new = list(filter(is_greater_than_9, a))
# print(new)

## Alternatively 
# a = [1, 3, 5, 234, 34, 32, 6543, 23, 2, 5, 6, 7, 43]
# new = list(map(lambda x: x > 9 ,a))
# print(new)
## More Example
# numbers = [1, 2, 3, 45, 4, 21]
# new = list(map(lambda x: x * x ,numbers))
# print(new)

##-------------------------------------------------------------
## Reduce

# from functools import reduce

# a = [1, 2, 3, 4, 5, 6]

# def sum(a, b):
#     return a + b

# c = reduce(sum, a)
# print(c)
##-------------------------------------------------------------

##-------------------------------------------------------------