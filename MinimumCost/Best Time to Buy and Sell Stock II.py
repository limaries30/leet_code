class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = len(prices)
        state = 0
        output = 0
        for num in range(nums - 1):
            if prices[num] < prices[num + 1]:
                output += prices[num + 1] - prices[num]
        return output
