'''Finding Duplicate Elements using Hashset '''
# # Time complexity O(n)
# # Space complexity O(n)
# def findDuplicates(arr):
#     seen = set() # used to store elemetns that we have already seen


#     for num in arr: # Traverse every element in array
        
#         if num in seen:
#             print(num)
#         else:
#             seen.add(num)

# arr = [1,2,3,2,4,5,1]
# findDuplicates(arr) 
# ----------------------------------------------------------------------------------
'''Sort 0s, 1s and 2s (Dutch National Flag)'''

# def sort012(arr):
#     low = 0 # keeps track of where next 0 should go
#     mid = 0 # mid is used to traverse array
#     high = len(arr) - 1 # keeps track where the next 2 should go

#     while mid <= high:

#         # Case 1: Current element is 0
#         if arr[mid] == 0:
#             # put 0 at the begenning 
#             arr[low], arr[mid] = arr[mid],arr[low]
#             # move both pointers forward
#             low += 1
#             mid += 1
#         # Case 2: Current element is 1 
#         elif arr[mid] == 1:

#             # 1 is already correct region
#             # simply move ahead
#             mid += 1
#         # Case 3: Cuurent element is 2
#         else:
#             # Put 2 at the end section
#             arr[mid],arr[high] = arr[high],arr[mid]
#             # reduce high pointer 
#             high -= 1

#     return arr

# ----------------------------------------------------------------------------------
'''Second Largest Element'''

# def secondLargest(arr):
    
#     # Largest number found so far
#     first = float('-inf')
    
#     # Second Largest number found so far
#     second = float('-inf')

#     # Traverse every element 
#     for num in arr:

#         #if current number is larger than largest
#         if num > first:

#             # Old largest becomes second largest
#             second = first

#             # Update Target
#             first = num

#         # Number is not largest
#         # but bigger than second largest
#         elif num > second and num != first:
#             second = num

#     return second # example arr = [5, 2, 8, 7, 1]
    
# ----------------------------------------------------------------------------------
'''Two Sum'''
# def twoSum(arr, target):

#     # Dictionary stores:
#     # number -> index
#     seen = {}

#     # Traverse array
#     for i, num in enumerate(arr):

#         # Value needed to reach target
#         diff = target - num

#         # If required number already exists
#         if diff in seen:

#             # Return indices
#             return [seen[diff], i]

#         # Store current number and index
#         seen[num] = i
# # arr = [2,7,11,15]
# # target = 9
# ----------------------------------------------------------------------------------
'''Check Vowels'''
# ch = input("Enter a character").lower()
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonants")
# ----------------------------------------------------------------------------------
'''Count Vowels'''
# text = 'cyntexa'
# vowels = 0
# consonants = 0

# for ch in text.lower():
#     if ch in "aeiou":
#         vowels+=1
#     else:
#         consonants+=1

# print('Vowels: ',vowels)
# print('consonants: ', consonants)
# ----------------------------------------------------------------------------------
'''Print First Vowel'''
# text = "cyntexa"
# for ch in text.lower():
#     if ch in 'aeiou':
#         print(ch)
#         break
# ----------------------------------------------------------------------------------
'''Remove all the vowels from text'''
# text = 'cyntexa'
# result = ""
# for ch in text.lower():
#     if ch not in 'aeiou':
#         result = ch
#         print(result)
# ----------------------------------------------------------------------------------
'''Count Frequency of Each vowel'''
# text = 'Programming'
# vowels = {
#     'a':0,
#     'e':0,
#     'i':0,
#     'o':0,
#     'u':0,
# }
# for ch in text.lower():
#     if ch in vowels:
#         vowels[ch] += 1

# print(vowels)
# ----------------------------------------------------------------------------------
'''Count max vowel'''
# text = 'beautiful'
# count = {
#     'a':0,
#     'e':0,
#     'i':0,
#     'o':0,
#     'u':0,
# }
# for ch in text.lower():
#     if ch in count:
#         count[ch] += 1

# print(count)

# max_vowel = 'a' # assume
# for vowel in count:
#     if count[vowel] > count[max_vowel]:
#         max_vowel = vowel
# print(max_vowel,count[vowel])
# ----------------------------------------------------------------------------------
'''Replace every vowel with '*' '''
# text = "cyntexa"
# result = ""
# for ch in text.lower():
#     if ch in 'aeiou':
#         result += '*'
#     else:
#         result += ch

# print(result)
# ----------------------------------------------------------------------------------
''' Check if Two Strings Have Same Number of Vowels '''

# s1 = "cat"
# s2 = "bell"

# count1 = 0
# count2 = 0

# # Count vowels in first string
# for ch in s1.lower():
#     if ch in "aeiou":
#         count1 += 1

# # Count vowels in second string
# for ch in s2.lower():
#     if ch in "aeiou":
#         count2 += 1

# # Compare counts
# if count1 == count2:
#     print("Yes")
# else:
#     print("No")
# ----------------------------------------------------------------------------------
'''Reverse Only Vowels'''

# text = "education"

# arr = list(text)
# left = 0
# right = len(arr) - 1
# while left < right:

#     while left < right and arr[left].lower() not in 'aeiou':
#         left += 1
#     while left < right and arr[right].lower() not in 'aeiou':
#         right -= 1

#     arr[left], arr[right] = arr[right], arr[left]

#     left+=1
#     right-=1


# print("".join(arr))
# ----------------------------------------------------------------------------------
'''Find Longest Continuous Sequence of Vowels'''

# text = 'beautiful'

# current = 0
# longest = 0
# for ch in text.lower():
#     if ch in 'aeiou':
#         current += 1

#         if current > longest:
#             longest = current 
#     else:
#         current = 0

# print(longest)

# ----------------------------------------------------------------------------------
'''Count words starting with a vowel'''

# text = 'apple is not an orange and is an apple only'

# count = 0

# words = text.split()

# for word in words:
#     if word[0].lower() in 'aeiou':
#         count += 1
# print(count)
# ----------------------------------------------------------------------------------
'''Find Percentage of Vowels in a String'''

# text = 'education'

# vowels = 0

# for ch in text.lower():
#     if ch in 'aeiou':
#         vowels+=1

# percentage = (vowels / len(text)) * 100

# print(percentage)
# ----------------------------------------------------------------------------------
'''Check if a Binary Number is Valid'''
# binary = "101101"

# valid = True

# for digit in binary:
#     if digit not in "01":
#         valid = False
#         break

# if valid:
#     print("Valid Binary")
# else:
#     print("Invalid Binary")
# ----------------------------------------------------------------------------------
'''Convert Binary to Decimal'''
# binary = '1011'

# decimal = 0 
# power = 0

# # start from right side 
# for digit in reversed(binary):
#     if digit == "1":
#         decimal += 2 ** power

#     power += 1

# print(decimal)
# ----------------------------------------------------------------------------------
'''Convert Decimal to Binary'''
num = 11

binary = ""

# keep dividing by 2
while num > 0:
    #save remainder
    binary = str(num%2) + binary
    #move to next step 
    num = num // 2

print(binary)
'''
Explanation:

11 ÷ 2 = 5 remainder 1

5 ÷ 2 = 2 remainder 1

2 ÷ 2 = 1 remainder 0

1 ÷ 2 = 0 remainder 1

Read remainders from bottom to top:

1011

Idea:

Divide by 2 repeatedly.
Store remainders.
'''
# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------