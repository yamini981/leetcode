class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            currBest = -1
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    if currBest == -1:
                        currBest = dp[i - coin] + 1
                    else:
                        currBest = min(currBest, dp[i - coin] + 1)
            
            dp[i] = currBest
        
        return dp[amount]
                    