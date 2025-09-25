'''Fibonacci series using recursion
fib(n) = fib(n-2) + fib(n-1) where  n-2 will take previous to previous value and n-1 will take previous value'''

def fib(n):
    #Base Case of recursion
    if(n == 0 or n== 1):
        return n
    return fib(n-2) + fib(n-1)

n = int(input("Enter a number: "))
print(fib(n))