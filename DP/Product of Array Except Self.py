'''
238. Product of Array Except Self
Medium

5809

469

Add to List

Share
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

Accepted
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1]*n
        R = [1]*n
        ans = [0]*n
        for i in range(n-1):
            L[i+1]=L[i]*nums[i]
            
        for i in range(n-1,0,-1):
            R[i-1]=R[i]*nums[i]
            ans[i]=R[i]*L[i]
        ans[0]=R[0]*L[0]
            
        return ans