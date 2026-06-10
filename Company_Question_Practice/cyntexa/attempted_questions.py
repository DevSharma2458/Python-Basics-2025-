'''
print a Z pattern 
12345
   4
  3
 2
12345
'''
# n = 5
# for num in range(1, n+1):
#     print(num,end=" ")

# print()

# for i in range(1,n):
#     print(" "*(n-i), end=" ")

#     print(i)

# for num in range(1,n+1):
#     print(num,end=" ")

'''
1
1*
1*2
1*2*
1*2*3
'''

# n = 5

# for row in range(1, n+1):
#     result = ""

#     for i in range(1,row+1):
#         if i % 2 != 0:
#             result += str((i + 1) // 2)
        
#         else:
#             result += "*"

#     print(result)

'''
matrix = [
    ['*', '.', '.'],
    ['.', '*', '*'],
    ['.', '*', '.']
]
'''
# matrix = [
#     ['*', '.', '.'],
#     ['.', '*', '*'],
#     ['.', '*', '.']
# ]
# rows = len(matrix)
# cols = len(matrix[0])

# # check every column
# for col in range(cols):
#     bottom = rows - 1
    
#     for row in range(rows - 1, -1, -1):
#         if matrix[row][col] == '*':
#             matrix[row][col] = '.'
#             matrix[bottom][col] = '*'
#             bottom -= 1

# for row in matrix:
#     print(row)

'''
s = "x10y20z0a30b0"
target = 30
'''
# s = "x10y20z0a30b0"
# target = 30

# nums = []
# num = ""

# # Extract numbers manually
# for ch in s:

#     # Build the number if digit found
#     if ch.isdigit():
#         num += ch

#     else:
#         # Number completed
#         if num:
#             nums.append(int(num))
#             num = ""

# # Add last number if present
# if num:
#     nums.append(int(num))

# # nums = [10, 20, 0, 30, 0]

# result = []
# seen = set()

# # Check adjacent pairs
# for i in range(len(nums) - 1):

#     first = nums[i]
#     second = nums[i + 1]

#     # Pair sum should equal target
#     if first + second == target:

#         # Sort so [0,30] and [30,0] are treated same
#         pair = tuple(sorted([first, second]))

#         # Add only unique pairs
#         if pair not in seen:
#             seen.add(pair)
#             result.append([first, second])

# print(result)

'''
take n as input check if it is a sqrt of any number and the number found is sqrt of any other number or not. Do this till n = 1 and return the number of steps done 
Rule 
1-if n is even and not a sqrt then divide by 2
2-if n is odd and not a sqrt then multiply by 3 and + 1
'''

# import math

# n = int(input("Enter a number: "))

# steps = 0

# # Keep going until 1 is reached
# while n != 1:

#     # Find square root
#     root = int(math.sqrt(n))

#     # Check if n is a perfect square
#     if root * root == n:

#         # Replace n with its square root
#         n = root

#     # If not a perfect square and even
#     elif n % 2 == 0:

#         # Divide by 2
#         n = n // 2

#     # If not a perfect square and odd
#     else:

#         # Apply 3n + 1 rule
#         n = 3 * n + 1

#     # One operation completed
#     steps += 1

# print("Steps =", steps)

'''
Given two array both unsorted and restriced to use built-in functions and other libs so you have to ignore the negative values and merge both sorted arrays and then return a sorted array
'''
arr1 = [5, -2, 8, 1]
arr2 = [7, -4, 3, 6]

merged = []

# Process first array
for num in arr1:

    # Convert negative to positive
    if num < 0:
        num = -num

    merged.append(num)

# Process second array
for num in arr2:

    # Convert negative to positive
    if num < 0:
        num = -num

    merged.append(num)

# Bubble Sort

n = len(merged)

# Number of passes
for i in range(n):

    # Compare adjacent elements
    for j in range(n - i - 1):

        # Swap if left element is bigger
        if merged[j] > merged[j + 1]:

            merged[j], merged[j + 1] = merged[j + 1], merged[j]

print(merged)