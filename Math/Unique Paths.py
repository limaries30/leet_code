"""
https://leetcode.com/problems/unique-paths/
"""
class Solution:
'''dp solution'''
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*n for i in range(m)]
        
        for i in range(n):
            dp[0][i]=1
        for i in range(m):
            dp[i][0]=1
        
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
                
        return dp[m-1][n-1]


class Solution:
    '''memoization'''
    def uniquePaths(self, m: int, n: int) -> int:
        
        self.visited = {}
    
        return self.dfs(m-1,n-1)
    
    def dfs(self,i,j):
        
        if i==0 or j==0:
            return 1
        
        if (i,j) in self.visited.keys():
            return self.visited[(i,j)]
    
        res =  self.dfs(i-1,j)+self.dfs(i,j-1)
        self.visited[(i,j)]=res
        return res
        
        

class Solution:
'''simple math'''
    def uniquePaths(self, m: int, n: int) -> int:

        return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))
