'''
Nth Fibonacci Number
Difficulty: EasyAccuracy: 22.3%Submissions: 410K+Points: 2
Find the n-th Fibonacci number for a given non-negative integer n.
The Fibonacci sequence is defined as:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n ≥ 2
Examples :

Input: n = 5
Output: 5
Explanation: The 5th Fibonacci number is 5.
Input: n = 0
Output: 0 
Explanation: The 0th Fibonacci number is 0.
Input: n = 1
Output: 1
Explanation: The 1st Fibonacci number is 1.
Constraints:
0 ≤ n ≤ 30
'''

n =  int(input("Enter nuber: "))

def nth_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    first = 0
    second = 1

    for i in range(2,n+1):
        current = first + second
        first = second
        second = current

    return second

print(nth_fibonacci(n))