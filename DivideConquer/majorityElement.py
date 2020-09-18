"""
https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        majority_num = len(nums) // 2
        for i in nums:
            if i in cnt.keys():
                cnt[i] += 1
            else:
                cnt[i] = 1
            if cnt[i] > majority_num:
                return i