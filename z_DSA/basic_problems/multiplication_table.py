# def printTable(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# if __name__ == "__main__":
#     printTable(5)
#------------------------------------------------

# def printTable(n):
#     result = []
#     for i in range (1,11):
#         result.append(f"{n} X {i} = {n*i}")
#     return result

# if __name__ == "__main__":
#     print(printTable(5))

#---------------------------------------------------

# printTable() prints table of number and takes
# 1 required value that is number of whose teble to be printed
# and an optional input i whose default value is 1
# def printTable(n, i=1):

#     if (i == 11):  # base case
#         return
#     print(n, "*", i, "=", n * i)
#     i += 1  
#     printTable(n, i)

# if __name__ == "__main__":
#   n = 5
#   printTable(n)