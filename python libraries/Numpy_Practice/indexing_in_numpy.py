import numpy as np
'''Creating a numpy array'''
# arr = np.array([1,2,3,4,'dev'])
# print(arr)

# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr)

# arr = np.array((1,2,3,4))
# print(arr)
'''
Initialize a Python NumPy Array Using Special Functions
NumPy provides several built-in functions to generate arrays with specific properties.

np.zeros(): Creates an array filled with zeros.
np.ones(): Creates an array filled with ones.
np.full(): Creates an array filled with a specified value.
np.arange(): Creates an array with values that are evenly spaced within a given range.
np.linspace(): Creates an array with values that are evenly spaced over a specified interval.
'''

# a0 = np.zeros((2, 3))
# a1 = np.ones((3, 3))
# af = np.full((2, 2), 7)
# ar = np.arange(0, 10, 2)  # start, stop, step
# la = np.linspace(0, 1, 5)  # start, stop, num

# print("Zero Array:","\n",a0)
# print("Ones Array:","\n",a1)
# print("Constant Array:","\n",af)
# print("Range Array:","\n",ar)
# print("Linspace Array:","\n",la)


'''Create Python Numpy Arrays Using Random Number Generation
NumPy provides functions to create arrays filled with random numbers.

np.random.rand(): Creates an array of specified shape and fills it with random values sampled from a uniform distribution over [0, 1).
np.random.randn(): Creates an array of specified shape and fills it with random values sampled from a standard normal distribution.
np.random.randint(): Creates an array of specified shape and fills it with random integers within a given range.'''

# ar = np.random.rand(2, 3)
# an = np.random.randn(2, 2)
# ai = np.random.randint(1, 10, size=(2, 3))  

# print(ar)
# print(an)
# print(ai)

'''Create Python Numpy Arrays Using Matrix Creation Routines
NumPy provides functions to create specific types of matrices.

np.eye(): Creates an identity matrix of specified size.
np.diag(): Constructs a diagonal array.
np.zeros_like(): Creates an array of zeros with the same shape and type as a given array.
np.ones_like(): Creates an array of ones with the same shape and type as a given array.'''

# im = np.eye(3)
# da = np.diag([1, 2, 3])
# a0 = np.zeros_like(da)
# a1 = np.ones_like(da)

# print(im)
# print(da)
# print(a0)
# print(a1)
'''Accessing the Arrray Index'''
# 1D array
# arr = np.arange(1,20) 
# print(arr[0])

# 2D array
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
# print(matrix[1,2]) # 0,"1" row  means second row and 2 means 0,1,"2" 3rd element which brings second row third element which is "6".

#3D array
'''3D Arrays: It can be visualized as a stack of 2D arrays, we need three indices-

Depth: Specifies the 2D slice.
Row: Specifies the row within the slice.
Column: Specifies the column within the row.'''
# cube = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])

# print(cube[1,2,0])

'''Booelan indexing'''
# arr = np.array([1,2,7,8])
# # print(arr[arr>2])
# # and or not
# print(arr[(arr>1) & (arr<8)])

'''Fancy indexing - Advance Indexing''' 
# arr = np.array([10, 20, 30, 40, 50])
# indices = [0, 2, 4]
# print(arr[indices])

'''Integer Array Indexing'''
# arr = np.array([10, 20, 30, 40, 50])
# print(arr[[0, 2, 4]])


