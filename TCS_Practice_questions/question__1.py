'''
Problem Description -: Given an array Arr[ ] of N integers and a positive integer K. The task is to cyclically rotate the array clockwise by K.
Note : Keep the first of the array unaltered. 
Example 1:
5  —Value of N
{10, 20, 30, 40, 50}  —Element of Arr[ ]
2  Value of K
Output : 40 50 10 20 30

Example 2:
4  —Value of N
{10, 20, 30, 40}  —Element of Arr[]
1  Value of K
Output : 40 10 20 30
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        self.k = k

        n = len(self.nums)
        self.k = self.k % n   # important if k > n
        return self.nums[-self.k:] + self.nums[:-self.k]
# def rotate(arr, k):
#     n = len(arr)
#     k = k % n   # important if k > n
#     return arr[-k:] + arr[:-k]

# Example
arr = [10, 20, 30, 40, 50]
k = 2



































