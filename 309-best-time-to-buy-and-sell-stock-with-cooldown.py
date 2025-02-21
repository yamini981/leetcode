class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state machine - very unique problem
        sold = float('-inf')
        held = float('-inf')
        reset = 0

        for price in prices:
            oldSold = sold
            
            # if our state is sold, that means we just sold what we hold
            sold = held + price

            # if our state is held, we are either already holding, or we just bought
            held = max(held, reset - price)

            # if our state is reset, we are either just resting again, or we just sold
            reset = max(reset, oldSold)

        return max(sold, reset)

