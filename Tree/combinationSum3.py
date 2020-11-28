"""
https://leetcode.com/problems/combination-sum-iii/
왜 내꺼는 이렇게 느리지...
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        self.k = k
        self.n = n
        self.answer = []

        self.dfs([], 1)

        return self.answer

    def dfs(self, res, current):

        if len(res) >= self.k or current > 9:
            if sum(res) == self.n and len(res) == self.k:
                self.answer.append(res.copy())
            return

        res.append(current)
        self.dfs(res, current + 1)
        res.pop()
        self.dfs(res, current + 1)
