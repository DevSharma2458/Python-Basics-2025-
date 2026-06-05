'''Two Types of modules in Python:
- Built-in modules (list of built in modules in python from python docs)
- User-defined modules'''


import math
import os
import mymodule  #importing user-defined module
import requests
print(math.sqrt(16))

mymodule.hello()
mymodule.is_even(8)
r = requests.get('https://www.google.com')
print(r.text)