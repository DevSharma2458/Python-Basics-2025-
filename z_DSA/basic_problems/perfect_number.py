'''
Perfect Numbers
Difficulty: EasyAccuracy: 17.21%Submissions: 252K+Points: 2
Given a number n, check if the number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

Examples:

Input: n = 6
Output: true 
Explanation: Factors of 6 are 1, 2, 3 and 6. Excluding 6 their sum is 6 which is equal to n itself. So, it's a Perfect Number.
Input: n = 10
Output: false
Explanation: Factors of 10 are 1, 2, 5 and 10. Excluding 10 their sum is 8 which is not equal to n itself. So, it's not a Perfect Number.
Input: n = 15
Output: false
Explanation: Factors of 15 are 1, 3, 5, 15. Excluding 15 their sum is 9 which is not equal to n itself. So, it's not a Perfect Number.
Constraints:
1 ≤ n ≤ 109
'''

n = int(input("Enter to check if the number is perfect or not: "))

def perfect_num(n):
    if n == 1: # base case that 1 cannot be factorised 
        return False
    
    factor_sum = 1 # taking it 1 because every number greater then 1 has 1 as its factor always
    i = 2 # taking i = 2 because 1 is already stored in factor sum and not taking 0 because divide by zero is error
    while i * i <= n: # finding sqaure root like sqrt(36) is 6 so ex if n = 36 then 6*6 = 36 where loop ends or ex if n = 28 then 4*4 is 16 5*5 is 25 (but 5 is not a factor) 6*6 is 36 which is greater then 28 
        if n % i == 0: # here we are finding factors
            factor_sum += i # if factor found then storing in factor_sum

            #also need to find the partner factor 
            #ex n = 28 and for the first iteration i = 2 for this its partner factor is 14 cause 28 divide by 2 is 14 so we need to store 14 too but in the case of 36 we got two 6s we need to take only one 

            if i != n // i:
                factor_sum += n // i

        i+=1

    return factor_sum == n # check wheather factor_sum is equal to n or not

print(perfect_num(n))