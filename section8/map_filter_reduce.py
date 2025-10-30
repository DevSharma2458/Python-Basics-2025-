# #-------------------------------------------------------------
# # Map - Returns 1 arguement = Returns New list (after applying) - Applies function to all
# “map() applies one function to all the items in a list. It’s like saying ‘do this operation for every element automatically.’”

# numbers = [1, 2, 3, 4, 45, 21]

# def square(x):
#     return x * x

# new = list(map(square, numbers))
# print(new)

# # -------------------------------------------------------------
# # Filter - Returns True or False - Returns Filtered list - Keeps only True values
# filter() is used to keep only those elements that satisfy a condition (True).
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
## Reduce - Takes 2 arguements - Returns single value - Combines all into one
# reduce() keeps combining elements of a list into one single value. (It’s not built-in — you have to import it from functools.)
# from functools import reduce

# a = [1, 2, 3, 4, 5, 6]

# def sum(a, b):
#     return a + b

# c = reduce(sum, a)
# print(c)
##-------------------------------------------------------------

##-------------------------------------------------------------