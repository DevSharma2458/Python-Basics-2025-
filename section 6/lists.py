# marks = [54, 54, "Hello", False, 2.3, 12]
# # Lists are oredered, mutable, allows duplicate elements
# print(marks[0]) #54
# print(marks) 
# print(marks[2:4]) #Hello

'''List Methods'''

# marks = [54, 54, 23, 12, 45]
# extra_marks = [67, 89] 
# marks.append(63) #Adds 63 to the end of the list
# print(marks)
# marks.pop() #Removes the last element of the list
# print(marks)
# marks.sort() #Sorts the list
# print(marks)
# marks.reverse() #Reverses the list
# print(marks)
# marks.insert(2, 100) #Inserts 100 at index 2
# print(marks)
# marks.remove(54) #Removes the first occurence of 54
# print(marks)
# marks.extend(extra_marks) #Extends the list by adding elements from extra_marks
# print(marks)
# print(marks.index(100)) #Returns the index of the first occurence of 100

'''List Comprehensions'''
"""
a = 5
table = []

for i in range(1,11):
    table.append(5*i)
now instead of this we can use list comprehensions    
"""
table = [5*i for i in range(1,11)]

print(table)