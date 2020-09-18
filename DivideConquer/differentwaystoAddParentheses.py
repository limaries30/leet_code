"""
https://leetcode.com/problems/different-ways-to-add-parentheses/
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.
"""


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        if input.isdigit():
            return [input]
        result = []

        for idx, item in enumerate(input):
            if item in "-+*":
                res1 = self.diffWaysToCompute(input[:idx])
                res2 = self.diffWaysToCompute(input[idx + 1 :])
                for i in res1:
                    for j in res2:
                        result.append(eval(str(i) + item + str(j)))

        return result