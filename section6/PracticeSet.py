# list = ["apple", "banana", "cherry"]
# print(list[0])
# print(len(list))
# print(list)
# index = list.index("banana")
# list[index] = "orange"
# print(list)
## -----------------------------------------------------
# numbers = list(range(1,11))
# print("first three numbers: ", numbers[:3])
# print("first three numbers: ", numbers[-3:])
## -----------------------------------------------------
# numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)
# numbers.remove(2)
# print(numbers)
## -----------------------------------------------------
# list = ["Alice", "Bob", "Charlie"]
# list.insert(len(list), "David")
# print(list)
## -----------------------------------------------------
# coordinates = (10, 20)
# print(coordinates)
# #coordinates[0] = 50 #error
# temp = list(coordinates)
# temp[0] = 50
# coordinates = tuple(temp)
# print(coordinates) 
## -----------------------------------------------------
# my_set = {1,2,3,3,4}
# print(my_set) # skipped duplicate 3
# my_set.add(5)
# my_set.remove(2)
# # Check if 4 is in the set
# print("Is 4 in my_set?", 4 in my_set)

# print("Updated set:", my_set)

## -----------------------------------------------------
# a = {1, 2, 3}
# b = {3, 4, 5}

# c = a.union(b) # removes duplicate and combines both
# d = a.intersection(b) # common element
# e = a.difference(b) #(a - b)
# print(e)
# print(d)
# print(c)

## -----------------------------------------------------
# student = {"name":"John", "age":20, "grade":"A"}
# print(student["name"])
# student["grade"] = "A+"
# print(student["grade"])
# student["city"] = "Delhi"
# print(student["city"])

## -----------------------------------------------------
# friends = {"Devashish" : 12345, "Vishal" : 54321, "Gotiya" : 31524}
# print(friends.keys())
# print(friends.values())
# print(friends.items())

## -----------------------------------------------------
##Write a program that takes a list of numbers and removes all duplicates using a set.

# list = [1, 2, 3,3,4, 4, 5]
# no_duplicates = set(list)
# print(list)
# print(no_duplicates)
## -----------------------------------------------------
## Given a dictionary of products and their prices, find the product with the highest price.

# products = {"S23" : 40000, "S23 FE" : 30000, "S23 Ultra": 70000}
# # Find the product with the highest price
# highest_price_product = max(products, key=products.get)
# print("Product with highest price:", highest_price_product, "-", products[highest_price_product])
## -----------------------------------------------------
## Write a program that merges two dictionaries into one.
# First = {"Name": "John", "Age" : 22, "Salary" : 30000}
# Second = {"Name1" : "Srk", "Age1": 22,  "Salary1" : 30000}

# Merged = {**First, **Second}
# print(Merged)
