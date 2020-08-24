'''
https://leetcode.com/problems/network-delay-time/
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
'''
class Solution:
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        inf = float("inf") 
        ch = [[inf]*N for i in range(N)]
        for i in times:
            ch[i[0]-1][i[1]-1]=i[2]
        for k in range(N):
            ch[k][k]=0
            for i in range(N):
                for j in range(N):
                    tmp = ch[i][k]+ch[k][j]
                    cur = ch[i][j]
                    if tmp<cur:
                        ch[i][j]=tmp
        
        if inf in ch[K-1]:
            return -1
        else:
            return max(ch[K-1])
