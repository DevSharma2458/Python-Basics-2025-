n = int(input("Enter a number"))

def isprime(n):
    if (n<=1):
        return False
    else:
        for i in range(2,n):
            if(n%i == 0):
                return False
                break

        else:
            return True    
        
  
print(isprime(n))    