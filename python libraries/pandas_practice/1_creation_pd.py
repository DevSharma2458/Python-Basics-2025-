import pandas as pd 
 
 #DATAFRAME
mydataset = {
'cars' : ["BMW", "Volvo", "Ford"],
'passings' : [3,7,2] 
}

myvar2 = pd.DataFrame(mydataset)
print(myvar2)

#SERIES
a = [1,7,2]
myvar1 = pd.Series(a)
print(myvar1)

