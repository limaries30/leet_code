'''https://leetcode.com/problems/knight-probability-in-chessboard/'''

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        self.K = K
        self.N = N

        self.child = 0

        self.memo = {}
        self.step(r,c,0)

        return self.child*((1/8)**K)
        
        
    def step(self,x,y,n):
        

        if x<0 or x>=self.N or y<0 or y>=self.N:
            return 0
        
        if n==self.K:
            self.child+=1
            return 1
        
        if (x,y,n) in self.memo.keys():
            self.child += self.memo[(x,y,n)]
            return self.memo[(x,y,n)]
        
        res = 0 
        moves = [-2,-1,1,2]
        for i in moves:
            for j in moves:
                if abs(i)!=abs(j):
                    res+=self.step(x+i,y+j,n+1)
                    
        self.memo[(x,y,n)]=res
        return res