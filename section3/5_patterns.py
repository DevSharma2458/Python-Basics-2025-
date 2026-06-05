"""
* * *
* * *
* * *
"""
# for i in range(3): #row
#     for j in range(3): #coloumn
#         print("*", end=" ")
#     print()
 #------------------------------
'''
*
* *
* * *
* * * *
'''

# for i in range(1,5):
#     for j in range(i):
#         print("*", end=" ")
#     print()
#-------------------------------

'''
* * * *
* * *
* *
*
'''
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#---------------------------------

'''
1
1 2
1 2 3
'''

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#-----------------------------------

'''
A
A B
A B C
'''

# for i in range(1,4):
#     for j in range(65, 65 + i):
#         print(chr(j), end=" ")
#     print()

#------------------------------------
'''
A B C D 
A B C
A B
A
'''

# for i in range(4,0,-1):
#     for j in range(65, 65 + i):
#         print(chr(j), end=" ")
#     print()

#---------------------------------------

'''
      *
    * *
  * * *
* * * *

'''
# n = 4
# for i in range(1,n + 1): # we can use (1,5)
#     print("  " * (n - i) + "*" * i)

#------------------------------------------

'''
    *
  * * *
* * * * *
'''

# n = 4
# for i in range(1,5):
#     print(" "*(n-i)+"*"*(2*i-1)) # * values from 1,3,5 and not 1,2,3,4,5 cause it is an triangle

#-------------------------------------------
'''
1
2 3
4 5 6
'''
# num = 1
# for i in range(1,4):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

#-------------------------------------------
'''
1
2 2
3 3 3
'''
# for i in range(1,4):
#     for j in range(i):
#         print(i,end=" ")
#     print()
#-------------------------------------------
'''
A
B C
D E F
'''
# ch = 65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(ch),end="")
#         ch+=1
#     print()

#-------------------------------------------
'''
* * * *
*     *
*     *
* * * *
'''
# n = 4
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#-------------------------------------------

'''
1 2 3 4
1 2 3
1 2
1
'''
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#-------------------------------------------
'''
1 2 3
1 2 3
1 2 3
'''

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()
#-------------------------------------------
'''
3 2 1
3 2
3
'''
# for i in range(3,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#-------------------------------------------
'''
1 *
2 * *
3 * * *
'''
# for i in range(4):
#     print(i,end=" ")
#     for j in range(i):
#         print("*", end=" ")

#     print()
#-------------------------------------------
'''
*
* *
*   *
* * * *
'''

n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==i or i==n:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
#-------------------------------------------
'''
A A A
B B B
C C C
'''
# for i in range(3):
#     for j in range(65,68):
#         print(chr(j),end=" ")
#     print()
#-------------------------------------------
'''
*   *   *
  *   *
*   *   *
  *   *
'''
# rows = 4
# cols = 5
# for i in range(rows):
#     for j in range(cols):
#         if (i + j) % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
