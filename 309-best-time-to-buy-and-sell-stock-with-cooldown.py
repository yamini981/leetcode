class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state machine - very unique problem
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            oldSold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, oldSold)

        return max(sold, reset)

