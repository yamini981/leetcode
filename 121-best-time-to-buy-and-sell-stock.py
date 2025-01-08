class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0

        sell = 1
        buy = 0
        while sell < len(prices):
            # sell - buy = profit
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                bestProfit = max(bestProfit, prices[sell] - prices[buy])
            
            sell += 1
        
        return bestProfit

