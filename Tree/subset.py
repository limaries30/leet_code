"""
https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.n = len(nums)
        self.nums = nums
        self.answer = []
        self.DFS(0, [])

        return self.answer

    def DFS(self, idx, result):

        if idx == self.n:
            self.answer.append(result)
            return

        tmp_result_1 = copy.copy(result)
        self.DFS(idx + 1, tmp_result_1)
        tmp_result_2 = copy.copy(result)
        tmp_result_2.append(self.nums[idx])
        self.DFS(idx + 1, tmp_result_2)
