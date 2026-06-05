'''Print the elements of Matrix'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     for num in row:
#         print(num, end = " ")
        
#--------------------------------------------------------------
'''Sum of all elements'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result = 0
# for row in matrix:
#     for num in row:
#         result+= num
# print(result)
#--------------------------------------------------------------
'''Find largest element'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# largest = matrix[0][0]

# for row in matrix:
#     for num in row:
#         if largest < num:
#             largest = num
# print(largest)
#--------------------------------------------------------------
'''Row Sum'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     row_sum = 0
#     for num in row:
#         row_sum+=num
#     print(row_sum)
#--------------------------------------------------------------
'''Column Sum'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# rows = len(matrix)
# cols = len(matrix[0])

# for col in range(cols):
#     col_sum = 0
#     for row in range(rows):
#         col_sum += matrix[row][col]
#     print(col_sum)
#--------------------------------------------------------------
'''Main Diagonal Sum'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# total = 0
# for i in range(len(matrix)):
#     total += matrix[i][i]

# print(total)
#--------------------------------------------------------------
'''Secondary Diagonal Sum'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# n = len(matrix)
# total = 0
# for i in range(n):
#     total += matrix[i][n-1-i] 
# print(total)
#--------------------------------------------------------------
'''Matrix Tanspose'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# rows  = len(matrix)
# cols = len(matrix[0])

# for col in range(cols):
#     for row in range(rows):
#         print(matrix[row][col], end=" ")

#     print()
#--------------------------------------------------------------
'''Matrix Search'''
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# target = 5
# found = False
# for row in matrix:
#     for num in row:
#         if num == target:
#             found = True
#             break
#     if found:
#         break

# if found:
#     print("Found")
# else:
#     print("Not Found")
#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------

#--------------------------------------------------------------
