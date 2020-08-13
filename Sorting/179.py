class Solution:
    
    def largestNumber(self, nums) -> str:
        self.nums = nums
        pt = 0
        pi = len(nums)-1
        
        self.QS(pt,pi)
        
        ans = list(map(str,nums))
        if ans[0]=="0":
            return "0"
        return ''.join(ans)
    
    def QS(self,pt,pi):
        if pt>=pi:
            return
        start = pt
        end = pi
        pivot = self.nums[pi]
        for i in range(pt,pi):
            if self.compare(self.nums[i],pivot):
                self.swap(i,pt)
                pt+=1

        self.swap(pt,end)
        self.QS(start,pt-1)
        self.QS(pt+1,end)

    def swap(self,x,y):
        tmp = self.nums[x]
        self.nums[x]=self.nums[y]
        self.nums[y]=tmp  

    def compare(self,x:int,y:int):
        if int(str(x)+str(y))>int(str(y)+str(x)):
            return True
        else:
            return False
ans = Solution().largestNumber([1,3,2,5])