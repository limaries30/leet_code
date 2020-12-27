
'''
https://leetcode.com/problems/valid-tic-tac-toe-state/
'''

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        cnt={}
        cnt['X']=0
        cnt['O']=0
        
        for row in board:
            for element in row:
                if element!=' ':
                    cnt[element]+=1
        
        if abs(cnt['X']-cnt['O'])!=0 or (cnt['X']==cnt[O]):
            return False
        
        return True    