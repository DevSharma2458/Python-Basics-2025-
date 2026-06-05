import pandas as pd
##### READING CSV ######
# df = pd.read_csv('data.csv')

# print(df.to_string())
# '''using to_string() will print all the data from the csv'''
# '''using only print(df) will print the first 5 rows and last five rows only not whole dataset'''


# print(pd.options.display.max_rows) # above 60 rows it will only display the first 5 and last 5 rows so 60 is the limit set to max_rows


# pd.options.display.max_rows = 9999 # manually changing the number of max_rows()
# df = pd.read_csv('data.csv')

# ###### READING JSON ######

# df = pd.read_json('data.json')

# print(df.to_string()) # to read all data as we used to do in csv

'''Disctionary as JSON'''

# data = {
#   "Duration":{
#     "0":60,
#     "1":60,
#     "2":60,
#     "3":45,
#     "4":45,
#     "5":60
#   },
#   "Pulse":{
#     "0":110,
#     "1":117,
#     "2":103,
#     "3":109,
#     "4":117,
#     "5":102
#   },
#   "Maxpulse":{
#     "0":130,
#     "1":145,
#     "2":135,
#     "3":175,
#     "4":148,
#     "5":127
#   },
#   "Calories":{
#     "0":409,
#     "1":479,
#     "2":340,
#     "3":282,
#     "4":406,
#     "5":300
#   }
# }

# df = pd.DataFrame(data)
# print(df)