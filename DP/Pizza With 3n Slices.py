'''
https://leetcode.com/problems/pizza-with-3n-slices/
'''
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
        total_pieces = len(slices)
        self.my_pieces = len(slices)//3
        
        return max(self.dp_build(slices[1:]),self.dp_build(slices[:-1]))
    
    def dp_build(self,arr):
        
        pieces = len(arr)
        dp = [[0]*pieces for i in range(pieces)]
        for i in range(pieces):
            for j in range(self.my_pieces):
                dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+arr[i])
                
        return dp[pieces-1][self.my_pieces-1]