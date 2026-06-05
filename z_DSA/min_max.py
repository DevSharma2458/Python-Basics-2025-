'''Find the minimum and maximum number from array'''
# Greedy Approach

def findminmax(arr, n):
    
    mini = arr[0]
    maxi = arr[0]
    for i in range(0,n):
        if arr[i] < maxi:
            mini = arr[i]
        
        elif arr[i] > maxi:
            maxi = arr[i]
        
    return [mini, maxi]


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    N = len(arr)
    ans = findminmax(arr, N)
    print(f"Max is: {ans[1]}")
    print(f"Min is: {arr[0]}")

# Library Functions

def findMin(arr, n):
    return min(arr)

def findMax(arr, n):
    return max(arr)

arr = [1,2,3,4,5]
N = len(arr)

print("Maximum is:",findMax(arr,N))
print("Minimum is:",findMin(arr, N))

#Minimum comparisons

# Python3 code to implement the idea

# array is used to return
# two values from minMax()
# min = arr[0], max = arr[1]
minmax = [0,0]

# Function to get the minimum and the maximum
def getMinAndMax(arr,n):

    # If array has even number of elements
    # then initialize the first two elements
    # as minimum and maximum
  if (n % 2 == 0):
    if (arr[0] > arr[1]):
      minmax[0] = arr[0]
      minmax[1] = arr[1]
    else:
      minmax[0] = arr[0]
      minmax[1] = arr[1]

      # Set the starting index for loop
    i = 2

    # If array has odd number of elements
    # then initialize the first element as
    # minimum and maximum
  else:
    minmax[0] = arr[0]
    minmax[1] = arr[0]

     # Set the starting index for loop
    i = 1

    # In the while loop, pick elements in
    # pair and compare the pair with max
    # and min so far
    while (i < n - 1):
        if (arr[i] > arr[i + 1]):
            if (arr[i] > minmax[1]):
                minmax[1] = arr[i]

            if (arr[i + 1] < minmax[0]):
                minmax[0] = arr[i + 1]
        else:
            if (arr[i + 1] > minmax[1]):
                minmax[1] = arr[i + 1]

            if (arr[i] < minmax[0]):
                minmax[0] = arr[i]

        # Increment the index by 2 as
        # two elements are processed in loop
        i += 2

# Driver code
arr = [ 5,1, 2, 3, 4, 9,8 ]
N = len(arr)

# Function call
getMinAndMax(arr, N);

print( "Maximum is: " , minmax[1] )
print( "Minimum is: " , minmax[0] )

        