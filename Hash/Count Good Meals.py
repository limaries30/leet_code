class Solution:
    '''O(N) hash'''
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = {}
        ans = 0
        
        for num in deliciousness:
            for j in range(22):
                if 2**j-num in cnt.keys():
                    ans += cnt[2**j-num]
            if num in cnt.keys():
                cnt[num]+=1
            else:
                cnt[num]=1
        return ans%(10**9 + 7)


class Solution:
    '''O(N^2) : Time Out'''
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = 0
        for i in range(len(deliciousness)):
            for j in range(i+1,len(deliciousness)):
                if self.isTwo(deliciousness[i],deliciousness[j]):
                    cnt += 1
        return cnt
    
    def isTwo(self,a,b):
        
        bi  = 1<<(len(bin(a+b))-3)
        return True if (a+b)&bi==a+b and a+b>0 else False
        