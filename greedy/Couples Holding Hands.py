'''
https://leetcode.com/problems/couples-holding-hands/
'''

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        cnt = 0
        
        for idx,couple in enumerate(row):
            
            if idx%2==0:
                if couple%2==0:
                    couple_idx = row.index(couple+1)
                else:
                    couple_idx = row.index(couple-1)
                if couple_idx!=idx+1:
                    cnt+=1
                    tmp = row[couple_idx]
                    row[couple_idx]=row[idx+1]
                    row[idx+1]=tmp
        return cnt