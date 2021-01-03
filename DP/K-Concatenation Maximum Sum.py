"https://leetcode.com/problems/k-concatenation-maximum-sum/"

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        sum_arr = sum(arr)
        max_sum_arr = self.maxSubarray(arr)
        max_sum_arr_two = self.maxSubarray(arr*2)
        
        MODULO = 10**9 + 7
        
        if k==1:
            return max_sum_arr%MODULO
        if sum_arr<0:
            return max(max_sum_arr,max_sum_arr_two)%MODULO
        else:
            return (max_sum_arr_two+(k-2)*sum_arr)%MODULO
        
    def maxSubarray(self,arr):
        local_max = -float('inf')
        global_max = -float('inf')
        for i in arr:
            local_max = max(local_max+i,i)
            global_max = max(local_max,global_max)
        return max(global_max,0)



class Solution:
    '''same solution(unreadable)'''
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        MODULO = 10 ** 9 + 7
        sum_arr = sum(arr)

        max_sum_arr = self.findMaxSubArraySum(arr * 2)

        return (
            ((k - 2) * max(sum_arr, 0) + max_sum_arr) % MODULO
            if k > 1
            else self.findMaxSubArraySum(arr)
        )

    def findMaxSubArraySum(self, arr):

        res = cur = 0
        for i in range(len(arr)):
            cur = max(arr[i], cur + arr[i])
            res = max(cur, res)
        return res