class FirstSolution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

        m = len(nums1)
        n = len(nums2)
        
        nums1.extend(nums2)
        nums1.sort()

        a,b = divmod(m+n,2)
        if b==0:
            return (nums1[a-1]+nums1[a])/2
        else:
            return nums1[a]


class SecondSolution:
    def findMedianSortedArrays(self, nums1,nums2):

        m = len(nums1)
        n = len(nums2)
        
        a,b = divmod(m+n,2)

        mi,ni =0,0
        prev = 0
        
        while True:
            
            if mi+ni == a: 
                mi,ni,prev_next = self.Compare(mi,ni,nums1,nums2)   
                if b==0:
                    print(prev,prev_next)
                    prev_next = (prev+prev_next)/2

                return prev_next
            
            mi,ni,prev = self.Compare(mi,ni,nums1,nums2)

            
    def Compare(self,mi,ni,num1,num2):
        
            ele_m = self.GetNext(mi,num1)
            ele_n = self.GetNext(ni,num2)

            if ele_m<ele_n:
                prev = ele_m
                mi+=1
            else:
                prev = ele_n
                ni+=1                
            return mi,ni,prev  
        
    def GetNext(self,idx,num_list):
        
        if idx >= len(num_list):
            return 100000000000000
        else:
            return num_list[idx]

secondsol = SecondSolution()
asnwer = secondsol.findMedianSortedArrays([100000],[100001])

print(asnwer)