"""
https://leetcode.com/problems/pizza-with-3n-slices/
"""


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        start_end_sum = slices[0] + slices[-1]
        quota = len(slices) // 3

        return max(self.dp(slices[:-1], quota), self.dp(slices[1:], quota))

    def dp(self, slices, quota):

        arr = [[0] * (quota + 1) for i in range(len(slices) + 1)]
        # arr[0][0]=slices[0]
        for i in range(1, len(slices) + 1):
            for j in range(1, quota + 1):
                if i == 1:
                    arr[i][j] = slices[i - 1]
                    continue
                arr[i][j] = max(arr[i - 2][j - 1] + slices[i - 1], arr[i - 1][j])
        return arr[-1][-1]
