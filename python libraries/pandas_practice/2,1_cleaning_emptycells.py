import pandas as pd

df = pd.read_csv('data_csv')

'''Duplicate using df.dropna() only'''
# new_df = df.dropna() # will copy the data and any changes made to this will not affect the original csv
# print(new_df.to_string())

#---------------------------------------\

'''If you want to change the original data then use inplace = True'''

# df.dropna(inplace=True) # will make changes to the original dataset

#---------------------------------------------

'''Replace Empty values'''
'''fillna() method allows us to replace empty cells with a value'''
# df.fillna(130, inplace=True) 

'''replace only for specified columns'''

# df.fillna({"Calories": 130},inplace=True)

'''Replace Using Mean, Median, or Mode'''

'''MEAN()'''

# x = df["Calories"].mean() # the avg value 
# df.fillna({"Calories": x}, inplace = True) #replace null values with avg (mean())

'''MEDIAN()'''
# x = df["Calories"].median() # median value by sorting
# df.fillna({"Calories":x}, inplace=True) # replace null values with median value

'''MODE()'''
# x = df["Calories"].mode() #value that appers mostly
# df.fillna({"Calories":x}, inplace=True) # will replace null values with the value that appears most frequently

