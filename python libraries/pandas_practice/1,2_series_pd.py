import pandas as pd

# a = [1,2,3]
# myvar = pd.Series(a)
# print(myvar)

#-----------------------------

'''Creating Index Labels'''

# a = [1,7,2]
# myvar = pd.Series(a, index = ["x","y","z"])
# print(myvar)

# print(myvar["y"])

#-----------------------------

'''key/value objects as series'''

calories = {"day1":420, "day2":380, "day3":390}
myvar = pd.Series(calories)
print(myvar)

'''now creating index for each of these'''

myvar = pd.Series(calories, index = ["x"])

