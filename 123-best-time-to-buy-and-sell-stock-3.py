# NOT OPTIMAL!!!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # a little bit of cheating - I know DP is involved somehow
        # what if we literally just bought and sold at every point and stored it?
        bestProfit = 0
        dp = {}

        def dfs(i, t, h):
            if (t == 0):
                return 0
            if (i == len(prices)):
                return 0
            if ((i, t, h)) in dp:
                return dp[(i, t, h)]
            

            # do nothing
            doNothing = dfs(i + 1, t, h)
            if h:
                # sell
                doSomething = prices[i] + dfs(i + 1, t - 1, False)
            else:
                # buy
                doSomething = -prices[i] + dfs(i + 1, t, True)
                
            bestProf = max(doSomething, doNothing)
            dp[(i, t, h)] = bestProf
            return bestProf

            
        
        return dfs(0, 2, False)
