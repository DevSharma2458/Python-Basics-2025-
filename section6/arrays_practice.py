'''array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.'''
import array as arr

# a = arr.array("i",[1,2,3])

# print(a[0])
# a.append(5)
# print(a)

'''Array in Python can be created by importing an array module. array( data_type , value_list ) is used to create array in Python with data type and value list specified in its arguments.'''

# a = arr.array('i',[1,2,3])
# for i in range(0,3):
#     print(a[i],end=" ")
#-------------------------------------
# a = arr.array('i', [1,2,3])
# print(*a)

# a.insert(1,4)
# print(*a)

'''Key diff is in insert you have to specify the index number and in append it will add at the end of the array'''

# a.append(7)
# print(*a)

'''Accessing elements in array'''
# a = arr.array('i',[12,34,34,345,6])
# print(a[0])

# b = arr.array('d',[34.56,435.43,1])
# print(b[0])
# print(b[2])

'''Removing an element from the array -->
 1) remove() 2) pop()'''

# a = arr.array('i',[1,2,3,4])
# a.remove(1) # remove first occurance of 1
# print(a)

# a.pop(2) # remove item at index 2
# print(a)

'''Slicing in array'''
# import array as arr
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = arr.array('i', a)

# res = b[3:8]
# print(*res)

# res = a[5:]
# print(res)

# res = a
# print(res)

'''Searching elements in an array'''
# a = arr.array('i',[1,2,3,4])
# print(a.index(2)) # index 1 pe pehli bar 2 ara hai
'''Updating element in array'''
# a = arr.array('i',[1,2,3,4])
# a[2]=5
# print(*a)

'''Diffrent operations in python array'''
# a = arr.array('i',[1,2,3,4])
# count()

# count=a.count(2)
# print(count)

# reverse()
# reverse=a.reverse()
# print(*a)

'''Extending element from array'''
# a = arr.array('i',[1,2,3,4])
# a.extend([5,6,7,8,9,10])
# print(*a)

