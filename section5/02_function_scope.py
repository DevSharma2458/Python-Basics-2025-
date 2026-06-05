def sum(a,b):
    c = a + b 
    return c

print(sum(3, 4))

'''Types of scope in python
1. Local scope- variables defined inside a function
2. Enclosing scope- function inside a function
3. Global scope- variables defined outside any function'''

#Global Scope 
def sum (a,b):
    print("Hey I am summing")
    c = a + b
    global z # Please modify the global variable z
    z = 0
    return c

z = 3
print(sum(3, 12))
print(sum(3,12))
print(z)
