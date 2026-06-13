'''
LCM of two numbers
Difficulty: EasyAccuracy: 64.08%Submissions: 16K+Points: 2
You are given two positive integers a and b Your task is to compute and return the Least Common Multiple (LCM) of the two numbers.
The LCM of two integers is the smallest positive integer that is divisible by both a and b.

Examples:

Input: a = 12, b = 18
Output: 36
Explanation: LCM of 12 and 18 is 36
Input: a = 5, b = 11
Output: 55
Explanation: LCM of 5 and 11 is 55
Constraints:
1 ≤ a, b ≤ 104
'''

import math
a = int(input("Enter a nuber"))
b = int(input("Enter second number"))
def lcm(a,b):
    return (a*b) // math.gcd(a,b)

print(lcm(a,b))