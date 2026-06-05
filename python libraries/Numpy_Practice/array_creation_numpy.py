'''Designed for array manipulation and numerical computations.
Faster than python lists and optimized for handling large datasets
Supports vectorized operations enabling faster execution of mathematical operations over arrays.'''


'''
Common Type Specifiers in NumPy
Some commonly used type codes are:

i1, i2, i4, i8 -> signed integers (Can store both negative and positive numbers e.g., -5, 0, 10)
u1, u2, u4, u8 -> unsigned integers (Can store only non-negative numbers e.g., 0, 5, 100)
f4, f8 -> floating-point numbers (Store decimal values e.g., 3.14, -0.75)
c8, c16 -> complex numbers (Store numbers with real and imaginary parts e.g., 2+3j)
a, U -> strings (Store text values e.g. "NumPy")
'''
'''1D array'''
# A one dimentsional array is a type of linear array.

import numpy as np

# a = [1,2,3,4]

# arr = np.array(a)
# print("List in python: ",a) # [1,2,3,4]
# print("Numpy array in python :", arr) # [1 2 3 4]


'''Multi-Dimensional Array'''

# list_1 = [1,2,3,4]
# list_2 = [5,6,7,8]
# list_3 = [9,10,11,12]

# sample_array = np.array([list_1,list_2,list_3])
# print("Numpy multi dimensioanl arrray \n", sample_array)

'''Shape of array'''
# sample_array = np.array([[0,4,2],[1,2,3],[4,5,6],[7,8,9],[9,8,7]])

# print("Shape of the array: ",sample_array.shape)

'''numpy.dtype'''
# sample_array_1 = np.array([[0,4,2]])
# sample_array_2 = np.array([[0.2,0.4,2.4]])

# print("Data type of the array 1:", sample_array_1.dtype)
# print("Data type of array 2:", sample_array_2.dtype)

"""Different ways of creating a numpy array"""
#1. numpy.array()

# arr = np.array([1,2,3,4,5])
# print(arr)


#2. numpy.fromiter()- The fromiter() function create a new one-dimensional array from an iterable object.

# var = "Geeksforgeeks"

# arr = np.fromiter(var,dtype='U2')

# print(arr)


#3. numpy.arrange()- This is an inbuilt NumPy function that returns evenly spaced values within a given interval.

#np.arange(1,20,2,dtype = np.float32) # works like a room arange means range from 1 to 20 and jump 2 so it will print all odd numbers
# here dtype is optional


#4. This function returns evenly spaced numbers over a specified between two limits. 

# arr = np.linspace(3.5,10,3, dtype= np.int32) # 3.5 is start 10 is end and 3 is n --> gap = (end - start) / (n - 1) using this formula
# print(*arr) 

#5. numpy.empty()- This function create a new array of given shape and type without initializing value.

# arr = np.empty([4,3], dtype = np.int32,order ='f')
# print(arr)
# # The output will be randomely generated array
# # order in the sense how will data be stored --> C means row wise and F means column wise

#6. numpy.ones()- This function is used to get a new array of given shape and type filled with ones (1).

# arr = np.ones([4,3], dtype=np.int32,order='C')
# print(arr)

#7. numpy.zeros()- same as ones but filled with zeros

# arr = np.zeros([4,3],dtype=np.int32, order='f')
# print(arr)

