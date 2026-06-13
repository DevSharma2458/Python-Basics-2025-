'''
Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

Examples :

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the Closest Number to 13 which is divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15 and divisible by 6, but -18 has the maximum absolute value. So, output is -18.
'''

n = int(input("Enter n: "))
m = int(input("Enter m: "))

def closest_number(n,m):

    quotient = n // m
    low_value = quotient * m
    high_value = (quotient + 1 ) * m

    if abs(low_value - n) < abs(high_value - n):
        return low_value
    elif abs(low_value - n) > abs(high_value - n):
        return high_value
    else:
        if low_value < high_value:
            return low_value
        else:
            return high_value
        
print(closest_number(n,m))