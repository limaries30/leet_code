'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        buy_state = [0]*len(prices)
        sell_state = [0]*len(prices)
        
        buy_state[0] = -prices[0]
        sell_state[0] = 0
        
        for i in range(1,len(prices)): 
            
            buy_state[i]=max(buy_state[i-1],sell_state[i-1]-prices[i])
            sell_state[i]=max(sell_state[i-1],prices[i]+buy_state[i-1]-fee)
            
        return sell_state[-1]
            