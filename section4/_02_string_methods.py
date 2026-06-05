# name = 'DevSharma' #strings are immutable

# a = len(name)
# print(a)

# print(name.upper())
# print(name.lower())
# print(name.replace('D', 'd'))
# print(name.capitalize())
# print(name.title())

#-------------------------
#They will remove the \n also
#this comes under whitespace characters
# text = " hello world "
# print(text.strip()) #removes spaces from both sides
# print(text.lstrip()) #removes spaces from left side
# print(text.rstrip()) #removes spaces from right side
#-------------------------
#finding and replacing
# text = "Python is fun"
# print(text.find('is')) #Output: 7
# print(text.find('fun', 8))#here 8 means index will start searching from 8th index and fun is at 10th index but if instead of 8 you choose 11 then logic wont find the "fun" and will end up saying "-1" as sign of value not found.
#-------------------------
# text = "Apples,Bananas,Cherries"
# print(text.split(',')) #Output: ['Apples', 'Bananas', 'Cherries']
# print(",".join(['Apples', 'Bananas', 'Cherries'])) #Output: Apples,Bananas,Cherries
#-------------------------
# text = "Python123"
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.startswith('P'))
# print(text.endswith('3'))
# print(text.count('t'))
# print(text.index('t'))

#-------------------------
# #STRING FORMATTING

template = "Dear {}, You are awesome. Take this {}$ bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marrie"
c1 = 300

s1 = template.format(a, a1)
print(s1)
# # F-strings
# print(f"{a} you are awesome and take this {a1}$ bag")