n = input("Enter any number or string to check if it is a palindrome: ")

def check_palindrome(n):
    n = n.replace("-", "")
    return n == n[::-1]
print(check_palindrome(n))