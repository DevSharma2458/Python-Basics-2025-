"Stack here means we are combining two different arrays into one"
import numpy as np
# like two 1D arrays into 1 2D array.

# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print(np.stack((a, b), axis=0))
# print(np.stack((a, b), axis=1))
# print(np.stack((a, b), axis=-1))
''' OUTPUT
[[1 2 3]
 [4 5 6]]
[[1 4]
 [2 5]
 [3 6]]
[[1 4]
 [2 5]
 [3 6]]'''


# x = np.array([[1, 2, 3],
#               [4, 5, 6]])

# y = np.array([[7, 8, 9],
#               [10, 11, 12]])

# print(np.stack((x, y), axis=0))
# print(np.stack((x, y), axis=1))
# print(np.stack((x, y), axis=2))

'''OUTPUT
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
[[[ 1  2  3]
  [ 7  8  9]]

 [[ 4  5  6]
  [10 11 12]]]
[[[ 1  7]
  [ 2  8]
  [ 3  9]]

 [[ 4 10]
  [ 5 11]
  [ 6 12]]]'''


# m = np.array([[[1, 2], [3, 4]],
#               [[5, 6], [7, 8]]])

# n = np.array([[[10, 20], [30, 40]],
#               [[50, 60], [70, 80]]])

# print("Print 1-",np.stack((m, n), axis=0))
# print("Print 2-",np.stack((m, n), axis=1))
# print("Print 3-",np.stack((m, n), axis=2))
# print("Print 4-",np.stack((m, n), axis=3))
'''OUTPUT
[[[[ 1  2]
   [ 3  4]]

  [[ 5  6]
   [ 7  8]]]

 [[[10 20]
   [30 40]]

  [[50 60]
   [70 80]]]]
   #------------------
[[[[ 1  2]
   [ 3  4]]

  [[10 20]
   [30 40]]]

 [[[ 5  6]
   [ 7  8]]

  [[50 60]
   [70 80]]]]
   #--------------
[[[[ 1  2]
   [10 20]]

  [[ 3  4]
   [30 40]]]

 [[[ 5  6]
   [50 60]]

  [[ 7  8]
   [70 80]]]]
   #-------------
[[[[ 1 10]
   [ 2 20]]

  [[ 3 30]
   [ 4 40]]]

 [[[ 5 50]
   [ 6 60]]

  [[ 7 70]
   [ 8 80]]]]'''

'''ARRAY SPLITTING'''

#1) numpy.split() is used to divide an array into equal-sized subarrays. The number of splits must perfectly divide the size of the array along the chosen axis. If equal division is not possible, NumPy will raise an error.

# arr = np.arange(6)
# res = np.split(arr,2)
# print(res)

# 2) numpy.array_split() works like split(), but it allows uneven splitting. This is useful when the array size does not divide evenly by the number of splits. NumPy will distribute the extra elements automatically.

# arr = np.arange(13)
# res = np.array_split(arr, 2)
# print(res)

# 3) numpy.vsplit() performs vertical splitting, meaning it divides a matrix row-wise (along axis=0). It works only on arrays with 2 or more dimensions.

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# res = np.vsplit(arr, 2)
# print(*res)
# Explanation: vsplit(matrix, 2) splits into 2 vertical (row-wise) partsand each part contains 2 rows

# 4) numpy.hsplit() performs horizontal splitting, which divides the array column-wise (axis=1). This is helpful when separating feature columns in datasets.
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# res = np.hsplit(arr, 2)
# print(res)
# Explanation: hsplit(array, 2) splits into 2 equal column groups and each output contains 2 columns

# 5) numpy.dsplit() is used for 3D arrays. It splits the array along the third axis (axis=2). This is useful when working with stacked matrices, images, or multi-channel data.
# arr = np.arange(24).reshape((2, 3, 4))
# res = np.dsplit(arr, 2)
# print(res)

'''
Output

[array([[[ 0,  1],
        [ 4,  5],
        [ 8,  9]],

       [[12, 13],
        [16, 17],
        [20, 21]]]), array([[[ 2,  3],
        [ 6,  7],
        [10, 11]],

       [[14, 15],
        [18, 19],
        [22, 23]]])]
   Explanation: Array shape is (2, 3, 4) and dsplit(..., 2) splits last axis into 2 equal parts. Each result contains half of the last dimension     
'''