class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = 0
        holding = False

        # buy lowest
        # sell highest

        for i in range(len(prices) - 1):
            if holding:
                if prices[i] > prices[i + 1]:
                    # sell
                    profit += prices[i] - prices[buy]
                    holding = False
                else:
                    print("keep holding")
                    # keep holding
            else:
                if prices[i + 1] > prices[i]:
                    buy = i
                    holding = True
                else:
                    print("do nothing")
                    # do nothing
        if holding:
            profit += prices[len(prices) - 1] - prices[buy]
        return profit

        










