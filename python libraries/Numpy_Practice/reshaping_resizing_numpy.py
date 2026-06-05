import numpy as np

'''Reshaping 1D array into 2D'''

# a = np.array([1,2,3,4,5,6,7,8,9])
# r = a.reshape(3,3)
# print(r)

''' Reshaping 1D array into 3D'''

# a = np.array([1,2,3,4,5,6,7,8])
# r = a.reshape(2,2,2) #2 rows 2 columns 2 arrays
# print(r)

'''Reshaping array by not giving column value so it wil calculate on its own by providing -1 in that'''

# a = np.array([1,2,3,4,5,6,7,8,9])
# r = a.reshape(3,-1) # divides array size with no. of rows to create column
# print(r)

'''RESIZE ARRAY- WILL ADD ELEMENTS AUTOMATICALLY'''
# arr = np.array([1, 2, 3, 4, 5, 6])
# arr.resize((3, 3))
# print(arr) 
# #OUTPUT  [[1 2 3]
# #        [4 5 6]
# #        [0 0 0]]

