import pandas as pd 

data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]   
}

# df = pd.DataFrame(data)
# print(df["calories"].loc[0]) # will return the first value from calories 
# print(df.loc[0]) # will return the first values from both the columns
# print(df.loc[[0,1]]) #will print the first and second values from both the columns

#--------------------------------------------------

'''creating index value'''
# df = pd.DataFrame(data, index = ["day1","day2","day3"])
# print(df)
# print(df.loc["day2"])
#---------------------------------------------------


