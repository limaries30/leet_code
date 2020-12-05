class Solution:
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