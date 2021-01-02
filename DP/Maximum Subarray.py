"""https://leetcode.com/problems/maximum-subarray/"""


class Solution:
    """divide and conquer"""

    def maxSubArray(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        self.nums = nums
        return self.divideConquer(low, high)

    def divideConquer(self, low, high):
        if high - low <= 1:
            return max([self.nums[low], self.nums[high], sum(self.nums[low : high + 1])])
        mid = int((low + high) / 2)

        return max(
            [
                self.divideConquer(low, mid - 1),
                self.divideConquer(mid + 1, high),
                self.crossMaxSum(low, mid, high),
            ]
        )

    def crossMaxSum(self, low, mid, high):

        left_max = self.maxSuccessiveSum(mid - 1, low, -1)
        right_max = self.maxSuccessiveSum(mid + 1, high, 1)
        return right_max + left_max + self.nums[mid]

    def maxSuccessiveSum(self, start, end, delta):
        arr_max = 0
        arr_sum = 0
        for i in range(start, end + delta, delta):
            arr_sum += self.nums[i]
            if arr_sum > arr_max:
                arr_max = arr_sum
        return arr_max


class Solution:
    """dp"""

    def maxSubArray(self, nums: List[int]) -> int:
        local_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            local_max = max(nums[i], local_max + nums[i])
            global_max = max(global_max, local_max)
        return global_max