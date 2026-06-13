'''
Given a positive integer n, count all pairs of ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = n.

Example :

Input: n = 9 
Output: 2
Explanation: There are two solutions: (a=1, b=2) and (a=2, b=1).
Input: n = 27
Output: 1
Explanation: Thereis only one solution: (a=3, b=0). 
Constraints:
1 <= n <= 105
'''
n = int(input("Enter a number"))
def pairCubeCount(n):
    count = 0 
    max_a = int(n ** (1/3)) + 1

    for a in range(1, max_a + 1):
        remaining = n - a**3

        if remaining < 0:
            break

        b = round(remaining ** (1/3))

        if b >= 0 and b ** 3 == remaining:
            count += 1

    return count 

print(pairCubeCount(n))