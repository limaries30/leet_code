"""https://leetcode.com/problems/maximum-subarray/"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i - 1] + nums[i])
            if nums[i] > cur_max:
                cur_max = nums[i]
        return cur_max