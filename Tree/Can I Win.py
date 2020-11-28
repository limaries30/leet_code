'''
https://leetcode.com/problems/can-i-win/submissions/
'''
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        nums = [i+1 for i in range(maxChoosableInteger)]
        if sum(nums)<desiredTotal:
            return False
        self.memo = {}
        
        result = self.dfs(nums,desiredTotal)
        
        return result
        
    def dfs(self,nums,desiredTotal):
        
        hash_key = str(nums)
        
        if hash_key in self.memo.keys():
            return self.memo[hash_key]
        
        
        if nums and desiredTotal <= nums[-1]:
            self.memo[hash_key]=True
            return True
        

        for idx,num in enumerate(nums):
            result = self.dfs(nums[:idx]+nums[idx+1:],desiredTotal-num)
            if not result:
                self.memo[hash_key]=True
                return True
        
        self.memo[hash_key]=False
        
        return False
                
        