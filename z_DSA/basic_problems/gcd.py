'''
GCD of two numbers
Difficulty: BasicAccuracy: 51.03%Submissions: 214K+Points: 1
Given two positive integers a and b, find GCD of a and b.

Note: Don't use the inbuilt gcd function

Examples:

Input: a = 20, b = 28
Output: 4
Explanation: GCD of 20 and 28 is 4
Input: a = 60, b = 36
Output: 12
Explanation: GCD of 60 and 36 is 12
Constraints:
1 ≤ a, b ≤ 109
'''

a = int(input("Enter a number"))
b = int(input("Enter a number"))
def gcd(a,b):
    while b != 0:
        a,b = b, a % b

    return a

print(gcd(a,b))