""" in terminal do cd section9 then run code
 Read Operation """
# f = open("dev.txt", "r")

# content = f.read()

# print(content)

# f.close()

""" Reading text line by line 
"""
# f = open("dev.txt", "r")

# for line in f:
#     print(line)

# f.close()

""" reading file using the with operation """

with open("dev.txt", "r") as f: #context manager
    content = f.read()
    print(content)
#  No need to f.close() the file it will automatically will be closed 

""" Write Operation"""

# # Write to a file called Jon Doe.txt It should contain data about John Doe.

# f = open("John Doe.txt", "w") # if you are working with binary files you need to put "t" in wt or rt 
# # It will create the file automatically named John Doe.txt and will insert the below text in it.
# # and whenever we are writing to a file make sure that the file doesnt contain any data cause all the data will be overridden by what you write next
# string = ''' John Dow is a  nice guy. He lives in Nyc and he works with Python 
# His favorite package is Pandas'''


# f.write(string)

# f.close()

""" Append Operation"""
# # It will not override the previous text and will add the new text to it 
# f = open("John Doe.txt", "a")

# string = '''
# John Doe initially lived in Phoenix, Arizona. He is a very nice guy

# '''
# f.write(string)
# f.close()










