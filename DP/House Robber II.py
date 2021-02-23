    class Solution:
        def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        return max(self.findMax(nums[1:]),self.findMax(nums[:-1]))
    
    def findMax(self,nums):
        
        dp = [0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        
        for j in range(2,len(nums)):
            dp[j]=max(dp[j-2]+nums[j],dp[j-1])
        
        return dp[-1]