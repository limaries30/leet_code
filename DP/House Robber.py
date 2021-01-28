class Solution:
    '''https://leetcode.com/problems/house-robber/'''
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0]*n
        
        if n==0:
            return 0
        dp[0] = nums[0]
        if n<2:
            return max(nums)
        dp[1]=max(nums[1],nums[0])

        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            
        return max(dp)